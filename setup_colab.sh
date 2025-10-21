#!/bin/bash
#
# setup_colab.sh - Script de Configuración Automática para Google Colab
# =====================================================================
#
# Este script configura automáticamente el entorno de Google Colab
# con SSHX y persistencia de datos.
#
# Uso:
#   !curl -sSL https://raw.githubusercontent.com/[tu-usuario]/[tu-repo]/main/setup_colab.sh | bash
#
# Autor: Generado con Claude Code
# Fecha: 2025-10-21

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para imprimir con color
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_header() {
    echo ""
    echo "======================================================================"
    echo "$1"
    echo "======================================================================"
    echo ""
}

# Verificar si estamos en Google Colab
check_colab() {
    if [ ! -d "/content" ]; then
        print_error "Este script está diseñado para ejecutarse en Google Colab"
        exit 1
    fi
    print_success "Entorno Google Colab detectado"
}

# Actualizar sistema
update_system() {
    print_info "Actualizando repositorios del sistema..."
    apt-get update -qq > /dev/null 2>&1
    print_success "Repositorios actualizados"
}

# Instalar herramientas esenciales
install_tools() {
    print_header "📦 INSTALANDO HERRAMIENTAS"

    local tools=(
        "neofetch:Información del sistema"
        "htop:Monitor de procesos"
        "tmux:Multiplexor de terminal"
        "vim:Editor de texto"
        "git:Control de versiones"
        "curl:Transferencia de datos"
        "wget:Descargador de archivos"
        "rsync:Sincronización de archivos"
        "tree:Visualizador de directorios"
        "ncdu:Analizador de espacio en disco"
    )

    for tool_info in "${tools[@]}"; do
        IFS=':' read -r tool desc <<< "$tool_info"
        print_info "Instalando $tool - $desc"

        if apt-get install -y -qq "$tool" > /dev/null 2>&1; then
            print_success "$tool instalado"
        else
            print_warning "Error instalando $tool (continuando...)"
        fi
    done
}

# Instalar SSHX
install_sshx() {
    print_header "🔗 INSTALANDO SSHX"

    if command -v sshx &> /dev/null; then
        print_info "SSHX ya está instalado"
        sshx --version
    else
        print_info "Descargando e instalando SSHX..."
        curl -sSf https://sshx.io/get | sh

        if command -v sshx &> /dev/null; then
            print_success "SSHX instalado correctamente"
        else
            print_error "Error al instalar SSHX"
            exit 1
        fi
    fi
}

# Configurar directorios de trabajo
setup_directories() {
    print_header "📁 CONFIGURANDO DIRECTORIOS"

    # Directorio de trabajo
    local work_dir="/content/workspace"
    mkdir -p "$work_dir"
    cd "$work_dir"
    print_success "Directorio de trabajo: $work_dir"

    # Directorios para datos persistentes (si Google Drive está montado)
    if [ -d "/content/drive/MyDrive" ]; then
        local drive_base="/content/drive/MyDrive/SSHX_Persistencia"
        mkdir -p "$drive_base"/{home,data,config,logs}
        print_success "Directorios de persistencia creados en Google Drive"
        echo "$drive_base" > /tmp/drive_base_path
    else
        print_warning "Google Drive no está montado"
        print_info "Monta Google Drive primero para habilitar persistencia"
    fi
}

# Configurar perfil de Bash
setup_bash_profile() {
    print_header "⚙️  CONFIGURANDO PERFIL DE BASH"

    cat >> ~/.bashrc << 'EOF'

# === Configuración SSHX ===
export WORKSPACE="/content/workspace"
export PS1='\[\033[01;32m\]\u@colab\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# Aliases útiles
alias ll='ls -alh'
alias la='ls -A'
alias l='ls -CF'
alias ..='cd ..'
alias ...='cd ../..'
alias workspace='cd /content/workspace'
alias drive='cd /content/drive/MyDrive'

# Función para backup rápido
backup() {
    if [ -d "/content/drive/MyDrive/SSHX_Persistencia" ]; then
        rsync -av --delete /content/workspace/ /content/drive/MyDrive/SSHX_Persistencia/home/
        echo "✅ Backup completado"
    else
        echo "❌ Google Drive no está montado"
    fi
}

# Función para restaurar datos
restore() {
    if [ -d "/content/drive/MyDrive/SSHX_Persistencia/home" ]; then
        rsync -av /content/drive/MyDrive/SSHX_Persistencia/home/ /content/workspace/
        echo "✅ Datos restaurados"
    else
        echo "⚠️  No hay datos para restaurar"
    fi
}

# Mostrar información al iniciar
echo "🚀 Bienvenido a SSHX en Google Colab"
echo "📁 Workspace: /content/workspace"
echo ""
echo "Comandos útiles:"
echo "  backup   - Guardar datos en Google Drive"
echo "  restore  - Restaurar datos de Google Drive"
echo "  workspace - Ir al directorio de trabajo"
echo ""

EOF

    source ~/.bashrc
    print_success "Perfil de Bash configurado"
}

# Mostrar información del sistema
show_system_info() {
    print_header "💻 INFORMACIÓN DEL SISTEMA"

    print_info "CPU Cores: $(nproc)"
    print_info "RAM Total: $(free -h | grep Mem | awk '{print $2}')"
    print_info "Disco Disponible: $(df -h / | tail -1 | awk '{print $4}')"

    if command -v neofetch &> /dev/null; then
        echo ""
        neofetch
    fi
}

# Crear script de inicio de SSHX
create_sshx_launcher() {
    print_header "🚀 CREANDO LANZADOR DE SSHX"

    cat > /usr/local/bin/start-sshx << 'EOF'
#!/bin/bash

echo "🚀 Iniciando SSHX Server..."
echo ""
echo "⚠️  IMPORTANTE:"
echo "   - Copia la URL que aparecerá abajo"
echo "   - Úsala en pruebaVPS.py desde tu PC Windows 11"
echo "   - No cierres esta terminal"
echo ""
echo "Presiona Ctrl+C para detener"
echo ""
echo "─────────────────────────────────────────────────────────────"
echo ""

# Ejecutar SSHX
sshx

EOF

    chmod +x /usr/local/bin/start-sshx
    print_success "Lanzador creado: start-sshx"
}

# Crear servicio de backup automático
create_auto_backup() {
    print_header "💾 CONFIGURANDO BACKUP AUTOMÁTICO"

    cat > /usr/local/bin/auto-backup << 'EOF'
#!/bin/bash

DRIVE_BASE="/content/drive/MyDrive/SSHX_Persistencia"
WORKSPACE="/content/workspace"

if [ ! -d "$DRIVE_BASE" ]; then
    echo "⚠️  Google Drive no está montado"
    exit 1
fi

echo "💾 Iniciando backup automático..."
rsync -av --delete "$WORKSPACE/" "$DRIVE_BASE/home/" 2>&1 | tee -a "$DRIVE_BASE/logs/backup.log"
echo "✅ Backup completado: $(date)" | tee -a "$DRIVE_BASE/logs/backup.log"

EOF

    chmod +x /usr/local/bin/auto-backup
    print_success "Script de backup creado: auto-backup"
}

# Resumen final
show_summary() {
    print_header "✅ CONFIGURACIÓN COMPLETADA"

    echo "🎉 Tu entorno está listo para usar SSHX con persistencia"
    echo ""
    echo "📋 Próximos pasos:"
    echo ""
    echo "1️⃣  Iniciar SSHX:"
    echo "   $ start-sshx"
    echo ""
    echo "2️⃣  Conectar desde Windows 11:"
    echo "   > python pruebaVPS.py"
    echo ""
    echo "3️⃣  Guardar datos:"
    echo "   $ backup"
    echo ""
    echo "4️⃣  Restaurar datos:"
    echo "   $ restore"
    echo ""
    echo "💡 Comandos útiles creados:"
    echo "   • start-sshx     - Inicia el servidor SSHX"
    echo "   • auto-backup    - Backup manual a Google Drive"
    echo "   • backup         - Alias rápido para backup"
    echo "   • restore        - Restaurar datos de Google Drive"
    echo ""
    echo "📚 Recursos:"
    echo "   • Workspace: /content/workspace"
    echo "   • Google Drive: /content/drive/MyDrive/SSHX_Persistencia"
    echo ""
    echo "⚠️  Recuerda: Ejecuta 'backup' antes de cerrar la sesión"
    echo ""
    print_success "¡Disfruta de tus $(nproc) cores y $(free -h | grep Mem | awk '{print $2}') de RAM!"
}

# Función principal
main() {
    print_header "🚀 CONFIGURACIÓN AUTOMÁTICA DE SSHX EN GOOGLE COLAB"

    check_colab
    update_system
    install_tools
    install_sshx
    setup_directories
    setup_bash_profile
    create_sshx_launcher
    create_auto_backup
    show_system_info
    show_summary
}

# Ejecutar
main
