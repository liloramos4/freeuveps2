# 🚀 SSHX en Google Colab con Persistencia

**Proyecto de Servidor VPS Virtual con SSHX y Google Colab**

Este proyecto te permite ejecutar un servidor Linux completo en Google Colab con acceso SSH desde tu PC Windows 11, aprovechando los **96 cores y 344 GB de RAM** disponibles en instancias TPU v5e, con **persistencia de datos** entre sesiones.

---

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación Rápida](#instalación-rápida)
- [Uso Detallado](#uso-detallado)
- [Persistencia de Datos](#persistencia-de-datos)
- [Solución de Problemas](#solución-de-problemas)
- [FAQ](#faq)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

---

## ✨ Características

- ✅ **Servidor SSHX** en Google Colab con acceso desde cualquier lugar
- ✅ **Persistencia de datos** usando Google Drive
- ✅ **96 cores y 344 GB RAM** (con TPU v5e)
- ✅ **Cliente para Windows 11** (`pruebaVPS.py`)
- ✅ **Backup automático** cada 5 minutos
- ✅ **Restauración automática** al reiniciar
- ✅ **Instalación de herramientas** (neofetch, htop, tmux, etc.)
- ✅ **Interfaz amigable** con menús interactivos
- ✅ **Sin configuración compleja** - funciona de inmediato

---

## 📦 Requisitos

### En tu PC (Windows 11):

- **Python 3.7+** ([Descargar aquí](https://www.python.org/downloads/))
- **WSL (Windows Subsystem for Linux)** - Recomendado
  - Instalación: Abre PowerShell como Admin y ejecuta:
    ```powershell
    wsl --install
    ```
- **Alternativa**: Git Bash ([Descargar aquí](https://git-scm.com/download/win))

### En Google Colab:

- Cuenta de Google
- Google Drive con espacio disponible (recomendado: 10 GB libres)
- Selección de runtime TPU v5e con High-RAM (opcional pero recomendado)

---

## 🚀 Instalación Rápida

### Opción 1: Notebook de Google Colab (Recomendado)

1. **Descarga el notebook**:
   - Descarga `Google_Colab_SSHX_Persistente.ipynb`
   - Súbelo a tu Google Drive

2. **Abre el notebook** en Google Colab

3. **Configura el runtime**:
   - Runtime → Change runtime type
   - Hardware accelerator: **TPU**
   - Runtime shape: **High-RAM**

4. **Ejecuta las celdas** en orden (Ctrl+F9 para ejecutar todas)

5. **Copia la URL** de SSHX que aparecerá

### Opción 2: Inicio Rápido con Script

En Google Colab:

```python
# Descargar y ejecutar
!curl -sSL https://raw.githubusercontent.com/[tu-usuario]/freeuveps2/main/quick_start.py -o quick_start.py
!python quick_start.py
```

### En tu PC Windows 11:

1. **Descarga `pruebaVPS.py`**:
   ```bash
   curl -O https://raw.githubusercontent.com/[tu-usuario]/freeuveps2/main/pruebaVPS.py
   ```

2. **Ejecuta el cliente**:
   ```bash
   python pruebaVPS.py
   ```

3. **Sigue las instrucciones** en pantalla

---

## 📖 Uso Detallado

### 1. Iniciar SSHX en Google Colab

#### Método A: Usando el Notebook

Ejecuta cada celda del notebook en orden:

```
Paso 1: Montar Google Drive ← Autoriza cuando se solicite
Paso 2: Configurar Entorno   ← Restaura datos previos
Paso 3: Instalar Herramientas ← Instala neofetch, htop, etc.
Paso 4: Iniciar SSHX          ← ¡Copia la URL que aparece!
```

#### Método B: Usando el Script Rápido

```python
!python quick_start.py
```

**Salida esperada:**
```
╔═══════════════════════════════════════════════════════════════╗
║   🚀  SSHX - Inicio Rápido en Google Colab                   ║
╚═══════════════════════════════════════════════════════════════╝

📂 Montando Google Drive...
✅ Google Drive montado

📁 Configurando persistencia de datos...
✅ Directorios de persistencia creados

🔗 Instalando SSHX...
✅ SSHX instalado correctamente

🚀 INICIANDO SERVIDOR SSHX
====================================================================

🔗 URL de Conexión:

   https://sshx.io/s/WlfhyC1F1t#kVTAZ6tyn1dY3G

====================================================================
```

### 2. Conectar desde Windows 11

#### Opción A: WSL (Recomendado)

1. **Abre PowerShell** o Terminal de Windows

2. **Ejecuta el cliente**:
   ```bash
   python pruebaVPS.py
   ```

3. **Selecciona**:
   - Opción **1**: Conectar con nueva URL
   - Pega la URL de SSHX
   - Elige método **1**: WSL

#### Opción B: Git Bash

1. **Abre Git Bash**

2. **Ejecuta**:
   ```bash
   python pruebaVPS.py
   ```

3. **Selecciona**:
   - Opción **1**: Conectar con nueva URL
   - Método **2**: Git Bash

#### Opción C: Navegador Web

1. **Ejecuta**:
   ```bash
   python pruebaVPS.py
   ```

2. **Selecciona**:
   - Opción **5**: Abrir en navegador
   - Pega la URL

3. **Tu navegador** se abrirá con una terminal web

### 3. Usar el Servidor Remoto

Una vez conectado, tendrás acceso completo al servidor:

```bash
# Ver información del sistema
neofetch

# Ver procesos
htop

# Navegar al workspace
cd /content/workspace

# Crear archivos (se guardarán automáticamente)
echo "Hola desde Google Colab" > test.txt

# Instalar paquetes (se guardarán con backup)
pip install numpy pandas

# Ejecutar scripts
python mi_script.py
```

---

## 💾 Persistencia de Datos

### Cómo Funciona

Los datos se sincronizan automáticamente entre:

```
Google Colab (/content/workspace) ←→ Google Drive (SSHX_Persistencia)
         ↓                                    ↓
  Sesión actual                        Almacenamiento permanente
```

### Estructura de Directorios en Google Drive

```
MyDrive/
└── SSHX_Persistencia/
    ├── home/          ← Tus archivos de trabajo
    ├── data/          ← Datos adicionales
    ├── config/        ← Configuraciones
    └── logs/          ← Logs de sesiones y backups
```

### Backup Automático

- **Frecuencia**: Cada 5 minutos
- **Método**: `rsync` (sincronización incremental)
- **Log**: Guardado en `logs/backup.log`

### Backup Manual

**Desde el Notebook:**
```python
# Ejecuta la celda "Paso 5: Backup Manual"
```

**Desde la terminal SSHX:**
```bash
# Ejecutar script de backup
/content/auto_backup.sh

# O usar el comando (si configuraste el perfil)
backup
```

### Restauración Automática

Al iniciar una nueva sesión, el sistema:

1. Detecta datos en Google Drive
2. Copia todo de vuelta a `/content/workspace`
3. Restaura tu entorno exactamente como lo dejaste

```
✅ Restaurados 42 elementos
   - Scripts: 15
   - Datos: 20
   - Configuraciones: 7
```

---

## 🛠️ Solución de Problemas

### Problema: SSHX no se instala

**Síntomas:**
```
❌ Error al instalar SSHX
```

**Soluciones:**

1. **Reinicia el runtime** de Colab:
   - Runtime → Restart runtime

2. **Verifica la conexión**:
   ```python
   !curl -I https://sshx.io
   ```

3. **Instalación manual**:
   ```python
   !curl -sSf https://sshx.io/get | sh -s -- --force
   ```

### Problema: Google Drive no se monta

**Síntomas:**
```
⚠️ Google Drive no está montado
```

**Soluciones:**

1. **Monta manualmente**:
   ```python
   from google.colab import drive
   drive.mount('/content/drive', force_remount=True)
   ```

2. **Autoriza** cuando se solicite (ventana emergente)

3. **Verifica permisos** de tu cuenta de Google

### Problema: No se restauran los datos

**Síntomas:**
```
ℹ️ No hay datos de sesión anterior
```

**Diagnóstico:**

```python
# Verifica si hay datos en Drive
!ls -lh /content/drive/MyDrive/SSHX_Persistencia/home/
```

**Soluciones:**

1. **Primera sesión**: Es normal, no hay datos aún

2. **Backup previo**: Verifica que ejecutaste backup antes de cerrar

3. **Restauración manual**:
   ```bash
   rsync -av /content/drive/MyDrive/SSHX_Persistencia/home/ /content/workspace/
   ```

### Problema: Conexión lenta desde Windows

**Síntomas:**
- Terminal se congela
- Comandos tardan en ejecutarse

**Soluciones:**

1. **Verifica tu internet**:
   ```bash
   ping google.com
   ```

2. **Reinicia SSHX** en Colab

3. **Usa el navegador** (Opción C) si WSL/Git Bash son lentos

4. **Cambia de región** de Colab si es posible

### Problema: WSL no está instalado

**Síntomas:**
```
❌ WSL no encontrado
```

**Solución:**

1. **Abre PowerShell como Administrador**

2. **Ejecuta**:
   ```powershell
   wsl --install
   ```

3. **Reinicia tu PC**

4. **Verifica**:
   ```powershell
   wsl --version
   ```

### Problema: La URL de SSHX no aparece

**Síntomas:**
- Script ejecutándose pero sin URL

**Soluciones:**

1. **Espera 30 segundos** - A veces tarda

2. **Revisa el output completo** - Busca `https://sshx.io/s/`

3. **Reinicia la celda** (Ctrl+C y ejecuta de nuevo)

4. **Verificación manual**:
   ```bash
   sshx --help
   ```

---

## ❓ FAQ

### ¿Es gratis?

**Sí**, Google Colab ofrece acceso gratuito con algunas limitaciones:
- **Tiempo de sesión**: Hasta 12 horas
- **Recursos**: Depende de disponibilidad
- **GPU/TPU**: Acceso limitado en plan gratuito

**Colab Pro** (de pago) ofrece:
- Sesiones más largas
- Más recursos garantizados
- Prioridad en GPU/TPU

### ¿Cuánto espacio necesito en Google Drive?

Depende de tus datos:
- **Mínimo**: 1 GB
- **Recomendado**: 10 GB
- **Para proyectos grandes**: 50+ GB

### ¿Puedo usar esto para machine learning?

**¡Por supuesto!** Es ideal para:
- Entrenar modelos
- Procesamiento de datos
- Notebooks de Jupyter
- Experimentos con GPU/TPU

Ejemplo:
```python
# Instalar PyTorch
!pip install torch torchvision

# Verificar GPU
import torch
print(f"GPU disponible: {torch.cuda.is_available()}")
print(f"GPU: {torch.cuda.get_device_name(0)}")
```

### ¿Los datos son seguros?

**Sí**:
- **Google Drive**: Encriptado y privado de tu cuenta
- **SSHX**: Conexiones seguras con tokens únicos
- **Sesiones**: Efímeras, se borran al cerrar

**Recomendaciones**:
- No compartas la URL de SSHX públicamente
- Haz logout de Google al terminar en PCs compartidos
- Usa contraseñas fuertes en tu cuenta de Google

### ¿Puedo ejecutar 24/7?

**No** en Colab gratuito:
- Sesiones máximo de 12 horas
- Se desconecta si no hay actividad

**Alternativas**:
- **Colab Pro**: Sesiones más largas
- **Scripts keep-alive**: Simular actividad
- **VPS real**: Para servicios 24/7

### ¿Funciona en Mac o Linux?

**Sí**, pero `pruebaVPS.py` está optimizado para Windows 11.

**En Mac/Linux**, conecta directamente:
```bash
# Instalar SSHX
curl -sSf https://sshx.io/get | sh

# Conectar (reemplaza con tu URL)
sshx join WlfhyC1F1t
```

### ¿Puedo personalizar las herramientas instaladas?

**¡Claro!** Edita el notebook o `quick_start.py`:

```python
# En quick_start.py, línea ~120
tools = ['neofetch', 'htop', 'tmux', 'tree', 'tu-herramienta']
```

O instala manualmente en SSHX:
```bash
sudo apt install nombre-paquete
```

### ¿Cómo actualizo SSHX?

```bash
curl -sSf https://sshx.io/get | sh -s -- --force
```

---

## 🎯 Casos de Uso

### 1. Desarrollo Web

```bash
# Instalar Node.js
!curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
!apt-get install -y nodejs

# Crear proyecto
cd /content/workspace
npx create-react-app mi-app
cd mi-app
npm start
```

### 2. Machine Learning

```python
# Entrenar modelo con GPU
import tensorflow as tf

# Verificar GPU
print(tf.config.list_physical_devices('GPU'))

# Tu código de entrenamiento...
```

### 3. Procesamiento de Datos

```bash
# Instalar herramientas
pip install pandas numpy scipy matplotlib

# Procesar dataset grande
python mi_analisis.py grandes_datos.csv
```

### 4. Servidor de Archivos

```bash
# Descargar archivo grande
cd /content/workspace
wget https://ejemplo.com/archivo-grande.zip

# Se guardará automáticamente en Drive
# Accesible en próximas sesiones
```

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

### Cómo contribuir:

1. **Fork** el repositorio
2. **Crea** una rama: `git checkout -b feature/mi-mejora`
3. **Commit**: `git commit -m 'Añadir característica X'`
4. **Push**: `git push origin feature/mi-mejora`
5. **Pull Request**: Crea un PR describiendo tus cambios

### Ideas para contribuir:

- Mejorar la documentación
- Añadir soporte para otros OS
- Optimizar backup/restauración
- Añadir más herramientas preinstaladas
- Crear tests automatizados
- Mejorar la interfaz de `pruebaVPS.py`

---

## 📄 Licencia

Este proyecto es de código abierto.

**Generado con [Claude Code](https://claude.com/claude-code)**

---

## 🔗 Enlaces Útiles

- [SSHX Official](https://sshx.io/)
- [Google Colab](https://colab.research.google.com/)
- [WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [Python Download](https://www.python.org/downloads/)
- [Git for Windows](https://git-scm.com/download/win)

---

## 📞 Soporte

¿Problemas? ¿Preguntas?

- **Issues**: Abre un issue en GitHub
- **Documentación**: Lee este README completo
- **SSHX**: Consulta https://sshx.io/docs

---

## 🎉 Agradecimientos

- **SSHX Team** - Por la increíble herramienta
- **Google Colab** - Por recursos gratuitos
- **Comunidad Open Source** - Por inspiración y soporte

---

## 📊 Estado del Proyecto

- ✅ Versión 1.0 - Funcionalidad básica
- ✅ Cliente Windows 11
- ✅ Persistencia de datos
- ✅ Backup automático
- 🔄 En desarrollo: Interfaz gráfica
- 🔄 Planeado: Soporte para múltiples usuarios

---

## 🚦 Inicio Rápido - Resumen

```bash
# 1. En Google Colab
!python quick_start.py

# 2. Copia la URL de SSHX

# 3. En tu PC Windows 11
python pruebaVPS.py

# 4. Pega la URL y ¡listo!
```

**¡Disfruta de tus 96 cores y 344 GB de RAM!** 🚀

---

<div align="center">

**Hecho con ❤️ usando Claude Code**

[⬆ Volver arriba](#-sshx-en-google-colab-con-persistencia)

</div>
