#!/usr/bin/env python3
"""Ejecuta los cuadernos del curso con nbclient y resume el resultado.

Uso:
    python3 scripts/ejecutar_cuadernos.py [--omitir ARCHIVO] [--timeout S] [cuaderno ...]

- Sin cuadernos explícitos, recorre ``[0-9][0-9]_*.ipynb`` de la raíz.
- ``--omitir`` apunta a un archivo de texto con un cuaderno por línea (los
  comentarios empiezan con ``#``); esos cuadernos no se ejecutan y se cuentan
  como omitidos.
- Cada cuaderno usa el kernel declarado en sus metadatos.
- Las celdas con la etiqueta ``skip-execution`` no se ejecutan (por ejemplo,
  editores interactivos). Las celdas con la etiqueta ``raises-exception``
  pueden terminar en error sin que el cuaderno falle (lo admite nbclient).
- En los cuadernos con kernel de Python, cada línea ``!comando`` se comprueba
  con ``_exit_code``: un comando del sistema que termina con error hace fallar
  la celda (IPython, por sí solo, no lo considera un error).
- Ningún cuaderno se guarda: las salidas solo se usan para el resumen.
- Los cuadernos se ejecutan en una copia temporal del repositorio, para que los
  archivos de práctica que crean no ensucien el árbol de trabajo.
"""

from __future__ import annotations

import argparse
import glob
import os
import shutil
import sys
import tempfile
import time

import nbformat
from nbclient import NotebookClient

ETIQUETA_OMITIR = "skip-execution"
COMPROBACION = "if _exit_code != 0: raise RuntimeError(f'El comando terminó con código {_exit_code}')"


def leer_omitidos(ruta: str | None) -> dict[str, str]:
    omitidos: dict[str, str] = {}
    if not ruta:
        return omitidos
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            nombre, _, motivo = linea.partition("#")
            omitidos[nombre.strip()] = motivo.strip()
    return omitidos


def verificar_comandos(celda) -> None:
    """Añade, tras cada línea ``!comando``, una comprobación de su código de salida."""
    if "raises-exception" in celda.get("metadata", {}).get("tags", []):
        return
    nuevas = []
    sangria = None  # sangría del comando ! en curso (puede seguir en varias líneas con \\)
    for linea in celda.source.splitlines():
        nuevas.append(linea)
        if sangria is None and linea.lstrip().startswith("!"):
            sangria = linea[: len(linea) - len(linea.lstrip())]
        if sangria is not None and not linea.rstrip().endswith("\\"):
            nuevas.append(f"{sangria}{COMPROBACION}")
            sangria = None
    celda.source = "\n".join(nuevas)


def ejecutar(ruta: str, timeout: int) -> tuple[bool, str, int]:
    nb = nbformat.read(ruta, as_version=4)
    antes = len(nb.cells)
    nb.cells = [c for c in nb.cells if ETIQUETA_OMITIR not in c.get("metadata", {}).get("tags", [])]
    celdas_omitidas = antes - len(nb.cells)
    kernel = nb.metadata.get("kernelspec", {}).get("name", "python3")
    if nb.metadata.get("kernelspec", {}).get("language", "python") == "python":
        for celda in nb.cells:
            if celda.cell_type == "code":
                verificar_comandos(celda)
    cliente = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name=kernel,
        allow_errors=False,
        resources={"metadata": {"path": os.path.dirname(os.path.abspath(ruta))}},
    )
    try:
        cliente.execute()
    except Exception as exc:  # noqa: BLE001
        return False, f"{type(exc).__name__}: {str(exc)[-800:]}", celdas_omitidas
    return True, "", celdas_omitidas


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("cuadernos", nargs="*")
    parser.add_argument("--omitir", help="archivo con la lista de cuadernos que no se ejecutan")
    parser.add_argument("--timeout", type=int, default=180, help="segundos máximos por celda")
    args = parser.parse_args()

    cuadernos = args.cuadernos or sorted(glob.glob("[0-9][0-9]_*.ipynb"))
    cuadernos = [os.path.abspath(c) for c in cuadernos]
    omitidos = leer_omitidos(args.omitir)
    raiz = os.getcwd()
    # La copia conserva el nombre del directorio (algunas celdas usan rutas como ../cd101).
    temporal = tempfile.mkdtemp(prefix="cuadernos-")
    copia = os.path.join(temporal, os.path.basename(raiz))
    shutil.copytree(raiz, copia, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".git"))
    pasan, fallan, saltados = [], [], []

    for ruta in cuadernos:
        nombre = os.path.basename(ruta)
        if nombre in omitidos:
            saltados.append(nombre)
            print(f"[OMITIDO] {nombre}: {omitidos[nombre]}", flush=True)
            continue
        inicio = time.monotonic()
        ok, error, n_omit = ejecutar(os.path.join(copia, os.path.relpath(ruta, raiz)), args.timeout)
        duracion = time.monotonic() - inicio
        extra = f", {n_omit} celdas con {ETIQUETA_OMITIR}" if n_omit else ""
        if ok:
            pasan.append(nombre)
            print(f"[OK] {nombre} ({duracion:.1f} s{extra})", flush=True)
        else:
            fallan.append(nombre)
            print(f"[FALLA] {nombre} ({duracion:.1f} s{extra})\n{error}", flush=True)

    shutil.rmtree(temporal, ignore_errors=True)
    print(f"\nResumen: {len(pasan)} pasan, {len(fallan)} fallan, {len(saltados)} omitidos.")
    for nombre in fallan:
        print(f"  - falla: {nombre}")
    return 1 if fallan else 0


if __name__ == "__main__":
    sys.exit(main())
