
# cd101 "Introducción a GNU/Linux desde la línea de comandos".

Notebooks de [Jupyter](https://jupyter.org) que incluyen los apuntes del curso cd101 "Introducción a GNU/Linux desde la línea de comandos" de [Cloudevel®](https://cloudevel.com).

## Contenido.

| Notebook | Tema |
|----------|------|
| [01](01_introduccion.ipynb) | Introducción a GNU/Linux |
| [02](02_sistemas_de_computo.ipynb) | Sistemas de cómputo |
| [03](03_la_linea_de_comandos.ipynb) | La línea de comandos |
| [04](04_directorios_y_archivos.ipynb) | Directorios y archivos |
| [05](05_jerarquía_de_directorios.ipynb) | Jerarquía de directorios |
| [06](06_flujos_de_texto_filtros_y_pipes.ipynb) | Flujos de texto, filtros y pipes |
| [07](07_expresiones_regulares_y_grep.ipynb) | Expresiones regulares y grep |
| [08](08_introduccion_a_vim.ipynb) | Los editores vim y sed |
| [09](09_gawk.ipynb) | El procesador de texto gawk |
| [10](10_usuarios_y_grupos.ipynb) | Usuarios y grupos |
| [11](11_permisos_y_propietarios_de_archivos.ipynb) | Permisos y propietarios de archivos |
| [12](12_procesos_trabajos_y_daemons.ipynb) | Procesos, trabajos y daemons |
| [13](13_diagnostico_y_monitoreo.ipynb) | Diagnóstico y monitoreo del sistema |
| [14](14_find_y_xargs.ipynb) | Los comandos find y xargs |
| [15](15_introduccion_a_bash_scripting.ipynb) | Introducción a Bash scripting |
| [16](16_entorno_del_shell.ipynb) | Entorno del shell con Bash |
| [17](17_proceso_de_arranque.ipynb) | El proceso de arranque del sistema |
| [18](18_kernel_modulos_y_dispositivos.ipynb) | El kernel de Linux, módulos y dispositivos |
| [19](19_volumenes_y_particiones.ipynb) | Volúmenes y particiones |
| [20](20_gestion_de_servicios_con_systemd.ipynb) | Gestión de servicios con systemd |
| [21](21_chroot_y_contenedores.ipynb) | chroot y contenedores |
| [22](22_introduccion_a_redes.ipynb) | Introducción a redes |
| [23](23_sesiones_remotas_y_transmision_de_datos.ipynb) | Sesiones remotas y transmisión de datos |
| [24](24_virtualizacion.ipynb) | Virtualización |
| [25](25_compresion_de_archivos.ipynb) | Compresión de archivos |
| [26](26_distribucion_de_software.ipynb) | Distribución de software |
| [27](27_fechas_horas_y_temporizadores.ipynb) | Fechas, horas y temporizadores |
| [28](28_seguridad_basica.ipynb) | Seguridad básica |

## Entornos de ejecución.

### Entorno del alumno (recomendado).

Para ejecutar la totalidad del curso se requiere una máquina virtual con una distribución basada en *Debian*, preferentemente **Ubuntu 24.04 LTS**. Algunas notebooks requieren acceso real al kernel, al proceso de arranque, a dispositivos de bloque y a *systemd*, lo cual no es posible en un contenedor estándar.

| Notebooks | Requieren VM | Razón |
|-----------|:---:|-------|
| 17 — proceso de arranque | SI | GRUB e initramfs reales |
| 18 — kernel y módulos | SI | Acceso a módulos del kernel del sistema |
| 19 — volúmenes y particiones | SI | fdisk/lsblk sobre discos reales |
| 20 — systemd | SI | systemd como PID 1 |
| 28 — ufw | SI | Requiere CAP_NET_ADMIN |
| Resto de notebooks | no | Compatibles con contenedor |

### Entorno de mantenimiento (devcontainer).

Para editar y mantener el material del curso existe una configuración de [Dev Container](https://containers.dev/) en `.devcontainer/`. Incluye Jupyter con el kernel de Bash y todas las herramientas de los notebooks compatibles con contenedor. Puede usarse con **VSCode** o con **GitHub Codespaces**.

## El kernel de Bash para Jupyter.

Las notebooks se ejecutan utilizando el [kernel de Bash](https://github.com/takluyver/bash_kernel).

## Clonación del repositorio.

Para clonar el repositorio en su sistema de archivos local, ejecute desde una terminal:

``` bash
git clone https://github.com/Cloudevel/cd101.git
```

## Licencia.

Esta obra está bajo una [Licencia Creative Commons Atribución 4.0 Internacional](https://creativecommons.org/licenses/by/4.0/).

&copy; José Luis Chiquete Valdivieso. 2017-2026.
