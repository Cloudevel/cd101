FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# Herramientas del curso cubiertas en los notebooks
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Python / Jupyter
    python3-pip \
    # Editores y procesamiento de texto (notebooks 06-09)
    vim \
    gawk \
    # Diagnóstico y monitoreo (notebook 13)
    htop \
    procps \
    sysstat \
    lsof \
    # Red y DNS (notebooks 22-23)
    dnsutils \
    iputils-ping \
    traceroute \
    mtr \
    net-tools \
    # Transferencia de datos (notebook 23)
    curl \
    wget \
    rsync \
    # Utilidades generales
    tree \
    && rm -rf /var/lib/apt/lists/*

# Jupyter con kernel de Bash
RUN pip3 install --break-system-packages jupyter bash_kernel \
    && python3 -m bash_kernel.install

# Notebooks con limitaciones en contenedor (solo referencia):
#   17 — proceso de arranque  (sin GRUB ni initramfs real)
#   18 — kernel y módulos     (kernel es el del host)
#   19 — volúmenes y discos   (fdisk/lsblk exponen discos del host)
#   20 — systemd              (no corre como PID 1)
#   28 — ufw                  (requiere CAP_NET_ADMIN)
