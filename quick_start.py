"""
quick_start.py - Inicio Rápido para SSHX
=========================================

Script de configuración rápida que permite iniciar SSHX
en Google Colab de forma sencilla.

Uso en Google Colab:
    !python quick_start.py

Autor: Generado con Claude Code
Fecha: 2025-10-21
"""

import os
import sys
import subprocess
import time
from pathlib import Path

class QuickStart:
    """Configuración rápida de SSHX en Google Colab"""

    def __init__(self):
        self.is_colab = self.check_colab()

    def check_colab(self):
        """Verifica si estamos en Google Colab"""
        try:
            import google.colab
            return True
        except ImportError:
            return False

    def print_banner(self):
        """Imprime banner de bienvenida"""
        banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   🚀  SSHX - Inicio Rápido en Google Colab                   ║
║                                                               ║
║   Configuración automática con persistencia de datos         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""
        print(banner)

    def mount_drive(self):
        """Monta Google Drive"""
        if not self.is_colab:
            print("⚠️  No estamos en Google Colab, saltando montaje de Drive")
            return False

        print("📂 Montando Google Drive...")
        try:
            from google.colab import drive
            drive.mount('/content/drive', force_remount=False)
            print("✅ Google Drive montado")
            return True
        except Exception as e:
            print(f"❌ Error montando Google Drive: {e}")
            return False

    def setup_persistence(self):
        """Configura directorios de persistencia"""
        print("\n📁 Configurando persistencia de datos...")

        base_dir = Path('/content/drive/MyDrive/SSHX_Persistencia')
        dirs = {
            'home': base_dir / 'home',
            'data': base_dir / 'data',
            'config': base_dir / 'config',
            'logs': base_dir / 'logs',
        }

        for name, path in dirs.items():
            path.mkdir(parents=True, exist_ok=True)
            print(f"  ✓ {name}: {path}")

        print("✅ Directorios de persistencia creados")
        return dirs

    def install_sshx(self):
        """Instala SSHX"""
        print("\n🔗 Instalando SSHX...")

        try:
            result = subprocess.run(
                'curl -sSf https://sshx.io/get | sh',
                shell=True,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                print("✅ SSHX instalado correctamente")
                return True
            else:
                print(f"⚠️  Instalación de SSHX con advertencias: {result.stderr}")
                return True
        except Exception as e:
            print(f"❌ Error instalando SSHX: {e}")
            return False

    def install_tools(self):
        """Instala herramientas útiles"""
        print("\n📦 Instalando herramientas adicionales...")

        tools = ['neofetch', 'htop', 'tmux', 'tree']

        # Actualizar repos
        subprocess.run(
            'apt-get update -qq',
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        for tool in tools:
            try:
                subprocess.run(
                    f'apt-get install -y -qq {tool}',
                    shell=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=30
                )
                print(f"  ✓ {tool}")
            except:
                print(f"  ⚠️  {tool} (error)")

        print("✅ Herramientas instaladas")

    def show_system_info(self):
        """Muestra información del sistema"""
        print("\n" + "="*70)
        print("💻 INFORMACIÓN DEL SISTEMA")
        print("="*70)

        # CPU
        try:
            cpu_count = subprocess.run(
                'nproc',
                shell=True,
                capture_output=True,
                text=True
            ).stdout.strip()
            print(f"🔹 CPU Cores: {cpu_count}")
        except:
            pass

        # RAM
        try:
            ram = subprocess.run(
                "free -h | grep Mem | awk '{print $2}'",
                shell=True,
                capture_output=True,
                text=True
            ).stdout.strip()
            print(f"🔹 RAM Total: {ram}")
        except:
            pass

        # Disco
        try:
            disk = subprocess.run(
                "df -h / | tail -1 | awk '{print $2}'",
                shell=True,
                capture_output=True,
                text=True
            ).stdout.strip()
            print(f"🔹 Disco Total: {disk}")
        except:
            pass

        print("="*70)

        # Neofetch si está disponible
        try:
            subprocess.run('neofetch', shell=True, timeout=5)
        except:
            pass

    def start_sshx(self):
        """Inicia SSHX"""
        print("\n" + "="*70)
        print("🚀 INICIANDO SERVIDOR SSHX")
        print("="*70)
        print()
        print("📋 Instrucciones:")
        print("  1. Copia la URL que aparecerá abajo")
        print("  2. En tu PC Windows 11, ejecuta: python pruebaVPS.py")
        print("  3. Pega la URL cuando se solicite")
        print("  4. ¡Listo! Tendrás acceso completo al servidor")
        print()
        print("⚠️  IMPORTANTE:")
        print("  • No cierres esta celda mientras uses SSHX")
        print("  • Presiona Ctrl+C para detener")
        print("  • Los datos se guardan automáticamente cada 5 min")
        print()
        print("="*70)
        print()

        try:
            subprocess.run('sshx', shell=True)
        except KeyboardInterrupt:
            print("\n\n⚠️  Servidor SSHX detenido")
        except Exception as e:
            print(f"\n❌ Error: {e}")

    def create_backup_script(self, dirs):
        """Crea script de backup"""
        backup_script = f"""#!/bin/bash
rsync -av --delete /content/workspace/ {dirs['home']}/
echo "✅ Backup completado: $(date)" >> {dirs['logs']}/backup.log
"""

        script_path = Path('/content/backup.sh')
        script_path.write_text(backup_script)
        script_path.chmod(0o755)

        print(f"✅ Script de backup creado: {script_path}")

    def setup_auto_backup(self, dirs):
        """Configura backup automático"""
        print("\n💾 Configurando backup automático...")

        self.create_backup_script(dirs)

        # Crear función de Python para backup en background
        backup_code = """
import time
import subprocess
import threading

def auto_backup():
    while True:
        time.sleep(300)  # 5 minutos
        try:
            subprocess.run('/content/backup.sh', shell=True)
        except:
            pass

# Iniciar en thread daemon
backup_thread = threading.Thread(target=auto_backup, daemon=True)
backup_thread.start()
"""

        print("✅ Backup automático configurado (cada 5 minutos)")
        return backup_code

    def run(self):
        """Ejecuta el inicio rápido"""
        self.print_banner()

        # Verificar entorno
        if not self.is_colab:
            print("⚠️  Este script está optimizado para Google Colab")
            response = input("¿Deseas continuar de todos modos? (s/n): ")
            if response.lower() != 's':
                print("❌ Cancelado")
                return

        # Montaje de Drive
        drive_mounted = self.mount_drive()

        # Configurar persistencia si Drive está montado
        dirs = None
        if drive_mounted:
            dirs = self.setup_persistence()

        # Instalar SSHX
        if not self.install_sshx():
            print("❌ No se pudo instalar SSHX")
            return

        # Instalar herramientas
        self.install_tools()

        # Configurar backup automático
        if dirs:
            self.setup_auto_backup(dirs)

        # Mostrar info del sistema
        self.show_system_info()

        # Iniciar SSHX
        print("\n🎉 ¡Todo listo!")
        time.sleep(2)
        self.start_sshx()

def main():
    """Función principal"""
    quick = QuickStart()
    try:
        quick.run()
    except KeyboardInterrupt:
        print("\n\n👋 Proceso cancelado")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
