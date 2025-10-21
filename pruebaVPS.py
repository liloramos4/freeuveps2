"""
pruebaVPS.py - Cliente SSHX para Windows 11
============================================

Este script permite conectarse a un servidor SSHX desde Windows 11.
Proporciona una interfaz fácil para gestionar conexiones remotas.

Uso:
    python pruebaVPS.py

Autor: Generado con Claude Code
Fecha: 2025-10-21
"""

import os
import sys
import subprocess
import urllib.request
import platform
import json
from pathlib import Path
import time

class SSHXClient:
    """Cliente SSHX para Windows 11"""

    def __init__(self):
        self.config_dir = Path.home() / ".sshx"
        self.config_file = self.config_dir / "config.json"
        self.sshx_executable = self.config_dir / "sshx.exe"
        self.ensure_config_dir()

    def ensure_config_dir(self):
        """Crea el directorio de configuración si no existe"""
        self.config_dir.mkdir(exist_ok=True)

    def check_platform(self):
        """Verifica que estamos en Windows"""
        if platform.system() != "Windows":
            print("⚠️  Este script está diseñado para Windows 11")
            print(f"   Sistema detectado: {platform.system()}")
            return False
        return True

    def download_sshx(self):
        """Descarga el cliente SSHX para Windows"""
        print("📥 Descargando SSHX para Windows...")

        # URL del cliente SSHX para Windows
        url = "https://sshx.io/get"

        try:
            # Descargamos el script de instalación
            print("   Obteniendo script de instalación...")
            response = urllib.request.urlopen(url)
            install_script = response.read().decode('utf-8')

            # Nota: En Windows necesitamos WSL o usar PowerShell
            print("\n⚠️  SSHX requiere WSL (Windows Subsystem for Linux) o PowerShell")
            print("\n📋 Opciones para instalar SSHX en Windows 11:")
            print("\n   OPCIÓN 1 - Usar WSL (Recomendado):")
            print("   1. Abre PowerShell como Administrador")
            print("   2. Ejecuta: wsl --install")
            print("   3. Reinicia tu PC")
            print("   4. Ejecuta en WSL: curl -sSf https://sshx.io/get | sh")

            print("\n   OPCIÓN 2 - Usar Git Bash:")
            print("   1. Instala Git para Windows: https://git-scm.com/download/win")
            print("   2. Abre Git Bash")
            print("   3. Ejecuta: curl -sSf https://sshx.io/get | sh")

            print("\n   OPCIÓN 3 - Conectarse a servidor existente:")
            print("   Este script puede conectarse a un servidor SSHX ya ejecutándose")
            print("   en Google Colab u otro sistema Linux")

            return True

        except Exception as e:
            print(f"❌ Error al descargar SSHX: {e}")
            return False

    def save_connection(self, url, name="default"):
        """Guarda una conexión SSHX"""
        config = self.load_config()

        connections = config.get("connections", {})
        connections[name] = {
            "url": url,
            "timestamp": time.time(),
            "last_used": time.time()
        }

        config["connections"] = connections
        config["last_connection"] = name

        self.save_config(config)
        print(f"✅ Conexión '{name}' guardada")

    def load_config(self):
        """Carga la configuración"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {}

    def save_config(self, config):
        """Guarda la configuración"""
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)

    def list_connections(self):
        """Lista las conexiones guardadas"""
        config = self.load_config()
        connections = config.get("connections", {})

        if not connections:
            print("📋 No hay conexiones guardadas")
            return

        print("\n📋 Conexiones guardadas:")
        print("-" * 60)
        for name, conn in connections.items():
            last_used = time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.localtime(conn['last_used']))
            print(f"  • {name}")
            print(f"    URL: {conn['url']}")
            print(f"    Último uso: {last_used}")
            print()

    def connect_wsl(self, url):
        """Conecta a SSHX usando WSL"""
        print(f"\n🔗 Conectando a: {url}")
        print("   Usando WSL...")

        # Extraemos el ID de sesión de la URL
        # Formato: https://sshx.io/s/WlfhyC1F1t#kVTAZ6tyn1dY3G
        session_id = url.split('/s/')[-1].split('#')[0]

        try:
            # Comando para conectar usando WSL
            cmd = f'wsl sshx join {session_id}'
            print(f"\n📡 Ejecutando: {cmd}")
            print("   (Presiona Ctrl+C para salir)\n")

            subprocess.run(cmd, shell=True)

        except KeyboardInterrupt:
            print("\n\n👋 Desconectado")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("\n💡 Verifica que WSL esté instalado:")
            print("   PowerShell (Admin): wsl --install")

    def connect_gitbash(self, url):
        """Conecta a SSHX usando Git Bash"""
        print(f"\n🔗 Conectando a: {url}")
        print("   Usando Git Bash...")

        session_id = url.split('/s/')[-1].split('#')[0]

        # Buscamos Git Bash
        git_bash_paths = [
            r"C:\Program Files\Git\bin\bash.exe",
            r"C:\Program Files (x86)\Git\bin\bash.exe",
        ]

        git_bash = None
        for path in git_bash_paths:
            if os.path.exists(path):
                git_bash = path
                break

        if not git_bash:
            print("❌ Git Bash no encontrado")
            print("   Descarga: https://git-scm.com/download/win")
            return

        try:
            cmd = f'"{git_bash}" -c "sshx join {session_id}"'
            print(f"\n📡 Ejecutando conexión...")
            print("   (Presiona Ctrl+C para salir)\n")

            subprocess.run(cmd, shell=True)

        except KeyboardInterrupt:
            print("\n\n👋 Desconectado")
        except Exception as e:
            print(f"\n❌ Error: {e}")

    def connect_browser(self, url):
        """Abre la conexión SSHX en el navegador"""
        print(f"\n🌐 Abriendo en navegador: {url}")

        try:
            import webbrowser
            webbrowser.open(url)
            print("✅ Navegador abierto")
            print("\n💡 Puedes usar SSHX desde el navegador web")
            print("   No requiere instalación local")
        except Exception as e:
            print(f"❌ Error al abrir navegador: {e}")

    def interactive_menu(self):
        """Menú interactivo"""
        print("\n" + "="*60)
        print("  🚀 SSHX Client para Windows 11")
        print("="*60)

        while True:
            print("\n📋 Menú Principal:")
            print("  1. Conectar con nueva URL")
            print("  2. Conectar a sesión guardada")
            print("  3. Listar conexiones guardadas")
            print("  4. Instalar/Configurar SSHX")
            print("  5. Abrir en navegador")
            print("  0. Salir")

            choice = input("\n👉 Selecciona una opción: ").strip()

            if choice == "1":
                url = input("\n🔗 Introduce la URL de SSHX: ").strip()
                if not url:
                    print("❌ URL vacía")
                    continue

                name = input("💾 Nombre para esta conexión (Enter=default): ").strip()
                if not name:
                    name = "default"

                self.save_connection(url, name)

                print("\n¿Cómo quieres conectar?")
                print("  1. WSL (Recomendado)")
                print("  2. Git Bash")
                print("  3. Navegador Web")

                method = input("\n👉 Método: ").strip()

                if method == "1":
                    self.connect_wsl(url)
                elif method == "2":
                    self.connect_gitbash(url)
                elif method == "3":
                    self.connect_browser(url)
                else:
                    print("❌ Opción inválida")

            elif choice == "2":
                config = self.load_config()
                connections = config.get("connections", {})

                if not connections:
                    print("\n📋 No hay conexiones guardadas")
                    continue

                print("\n📋 Conexiones disponibles:")
                conn_list = list(connections.keys())
                for i, name in enumerate(conn_list, 1):
                    print(f"  {i}. {name} - {connections[name]['url']}")

                try:
                    idx = int(input("\n👉 Número de conexión: ")) - 1
                    if 0 <= idx < len(conn_list):
                        name = conn_list[idx]
                        url = connections[name]['url']

                        # Actualizamos último uso
                        connections[name]['last_used'] = time.time()
                        config['connections'] = connections
                        self.save_config(config)

                        print("\n¿Cómo quieres conectar?")
                        print("  1. WSL")
                        print("  2. Git Bash")
                        print("  3. Navegador Web")

                        method = input("\n👉 Método: ").strip()

                        if method == "1":
                            self.connect_wsl(url)
                        elif method == "2":
                            self.connect_gitbash(url)
                        elif method == "3":
                            self.connect_browser(url)
                    else:
                        print("❌ Número inválido")
                except ValueError:
                    print("❌ Entrada inválida")

            elif choice == "3":
                self.list_connections()

            elif choice == "4":
                self.download_sshx()

            elif choice == "5":
                url = input("\n🔗 Introduce la URL de SSHX: ").strip()
                if url:
                    self.connect_browser(url)

            elif choice == "0":
                print("\n👋 ¡Hasta luego!\n")
                break

            else:
                print("❌ Opción inválida")

def main():
    """Función principal"""
    print("🚀 Iniciando SSHX Client para Windows 11...\n")

    client = SSHXClient()

    # Verificamos la plataforma
    if not client.check_platform():
        print("\n💡 Este script funciona mejor en Windows 11")
        print("   Pero puede funcionar en Windows 10 con WSL")

    # Menú interactivo
    try:
        client.interactive_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Programa terminado\n")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
