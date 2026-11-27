FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# Herramientas de los cuadernos compatibles con un contenedor.
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    vim \
    gawk \
    htop \
    procps \
    sysstat \
    lsof \
    dnsutils \
    iputils-ping \
    traceroute \
    mtr \
    net-tools \
    curl \
    wget \
    rsync \
    tree \
    && rm -rf /var/lib/apt/lists/*

# Jupyter con kernel de Bash
RUN pip3 install --break-system-packages jupyter bash_kernel \
    && python3 -m bash_kernel.install

# El entorno principal es Ubuntu 24.04 en GitHub Codespaces, con el usuario vscode.
# Jupyter no se inicia como root ni escucha en 0.0.0.0.
#
# Solo estos ejercicios requieren una máquina Ubuntu 24.04 con systemd como PID 1
# (no corren en GitHub Codespaces):
#   - ssh.service y ssh.socket
#   - sshd_config.d, con sshd -t y recarga del servicio
#   - ufw
#   - timedatectl / systemd-timesyncd
#   - systemctl status cron
