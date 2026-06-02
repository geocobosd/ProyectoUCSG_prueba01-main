# 🚀 Guía de Deployment - ProyectoUCSG

## Paso a Paso: GitHub + Streamlit Cloud

---

## 📋 PREREQUISITOS

Antes de comenzar, asegúrate de tener:

✅ **Git instalado** - [Descargar Git](https://git-scm.com/downloads)  
✅ **Cuenta en GitHub** - [github.com](https://github.com)  
✅ **Proyecto listo** - Todos los archivos en su lugar  

---

## 🔧 PASO 1: PREPARAR GITHUB

### Opción A: Crear Nuevo Repositorio en GitHub (Recomendado)

1. Ve a https://github.com/new
2. Llena los datos:
   - **Repository name**: `ProyectoUCSG` (o como prefieras)
   - **Description**: "Análisis de Churn Bancario con Streamlit"
   - **Public**: ✓ (importante: debe ser público para Streamlit Cloud)
   - **Add .gitignore**: No (ya lo tenemos)
   - **License**: MIT (opcional)

3. Click en **"Create repository"**

4. Copia la URL del repositorio (ej: `https://github.com/tuusuario/ProyectoUCSG.git`)

---

## 💻 PASO 2: CONFIGURAR GIT LOCALMENTE

Abre **PowerShell**, **Terminal** o **Git Bash** en la carpeta del proyecto:

```bash
# 1. Navegar a la carpeta del proyecto
cd "g:\Mi unidad\CASA GRANDE\MAESTRIA\Inteligencia Artificial y Ciencia de Datos\Materias\EJEMPLOS\ProyectoUCSG_prueba01-main\ProyectoUCSG_prueba01-main"

# 2. Inicializar git (si no está iniciado)
git init

# 3. Configurar tu usuario de Git (primera vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@gmail.com"

# 4. Agregar el repositorio remoto
git remote add origin https://github.com/tuusuario/ProyectoUCSG.git

# 5. Verificar que está conectado
git remote -v
```

---

## 📤 PASO 3: SUBIR PROYECTO A GITHUB

```bash
# 1. Agregar todos los archivos
git add .

# 2. Ver qué se va a subir (opcional, para verificar)
git status

# 3. Hacer commit inicial
git commit -m "feat: initial project setup - professional streamlit app"

# 4. Cambiar rama a 'main' (si es necesario)
git branch -M main

# 5. Pushear a GitHub
git push -u origin main
```

**Si te pide autenticación:**
- GitHub ya no acepta contraseñas
- Usa **Personal Access Token (PAT)** o **SSH**

### Opción 1: Usar Personal Access Token (Más fácil)

1. Ve a GitHub → Settings → Developer settings → Personal access tokens
2. Click en "Generate new token"
3. Selecciona: `repo`, `workflow`
4. Genera y copia el token
5. Cuando Git pida contraseña, pega el token

### Opción 2: Usar SSH (Más seguro)

```bash
# Generar clave SSH
ssh-keygen -t ed25519 -C "tu.email@gmail.com"

# Agregar a SSH agent
ssh-add ~/.ssh/id_ed25519

# Copiar la clave pública
# Windows: Get-Content ~/.ssh/id_ed25519.pub | Set-Clipboard
# Mac/Linux: cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard

# Ir a GitHub → Settings → SSH keys → Add new
# Pegar la clave
```

---

## ✅ PASO 4: VERIFICAR EN GITHUB

1. Ve a tu repositorio en GitHub: `https://github.com/tuusuario/ProyectoUCSG`
2. Verifica que todos los archivos están allí:
   - ✓ app.py
   - ✓ requirements.txt
   - ✓ README.md
   - ✓ src/ (carpeta)
   - ✓ data/ (carpeta)
   - ✓ .streamlit/ (carpeta)

---

## 🌐 PASO 5: CONECTAR CON STREAMLIT CLOUD

### 5.1 Crear Cuenta en Streamlit Cloud

1. Ve a https://share.streamlit.io
2. Click en **"Sign in with GitHub"**
3. Autoriza Streamlit para acceder a tu GitHub

### 5.2 Deployar la App

1. En Streamlit Cloud, click en **"New app"**
2. Llena los datos:
   - **Repository**: `github.com/tuusuario/ProyectoUCSG`
   - **Branch**: `main`
   - **Main file path**: `app.py`

3. Click en **"Deploy!"**

**¡Streamlit iniciará el deployment automáticamente!**

---

## 📊 PASO 6: ESPERAR Y COMPARTIR

### Tiempo de Deployment

- ⏱️ Primera vez: 2-5 minutos
- ⏱️ Actualizaciones: 30-60 segundos

### Tu URL será:

```
https://[username]-[appname].streamlit.app/
```

**Ejemplo:** `https://juan-proyectoucsg.streamlit.app/`

### Compartir

- ✅ Copia la URL y comparte
- ✅ Agrega a redes sociales
- ✅ Incluye en tu portafolio

---

## 🔄 PASO 7: ACTUALIZAR LA APP (En el Futuro)

Cada vez que cambies el código:

```bash
# 1. Ver cambios
git status

# 2. Agregar cambios
git add .

# 3. Commit
git commit -m "feat: descripción del cambio"

# 4. Push
git push origin main
```

**Streamlit Cloud detectará los cambios automáticamente y redesplegará en ~1 minuto.**

---

## ⚠️ SOLUCIÓN DE PROBLEMAS

### Problema: "Repository not found"

**Solución:**
- Verifica que la URL es correcta
- Asegúrate de que el repositorio es **público**
- Revisa que hayas dado permisos a Streamlit

### Problema: "ModuleNotFoundError"

**Solución:**
- Verifica que `requirements.txt` tiene todas las dependencias
- Ejecuta localmente: `pip install -r requirements.txt`
- Pushea los cambios

### Problema: "Datos no encontrados"

**Solución:**
- Verifica que `data/Churn_Modelling.csv` está en GitHub
- Comprueba la ruta en `src/config.py`

### Problema: App carga pero está vacía

**Solución:**
- Ve a Streamlit Cloud y mira los **logs**
- Busca errores en la sección "Deploy"
- Revisa que todas las importaciones son correctas

### Ver Logs en Streamlit Cloud

1. Ve a tu app en Streamlit Cloud
2. Click en el menú (⋮) arriba a la derecha
3. Click en **"Logs"**
4. Busca mensajes de error

---

## 🎯 CHECKLIST FINAL

Antes de deployar, verifica:

- [ ] Todos los archivos están en el proyecto
- [ ] `requirements.txt` tiene todas las dependencias
- [ ] `app.py` funciona localmente sin errores
- [ ] Rutas de archivos son relativas (no absolutos)
- [ ] `.gitignore` está configurado
- [ ] Repositorio en GitHub es **público**
- [ ] Permiso de Streamlit está autorizado

---

## 📱 TESTING LOCAL ANTES DE DEPLOYAR

Simula exactamente lo que hará Streamlit Cloud:

```bash
# Instalar desde cero
python -m venv test_env
source test_env/bin/activate  # Windows: test_env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Si funciona localmente, funcionará en Streamlit Cloud ✓

---

## 🔐 VARIABLES SENSIBLES EN STREAMLIT CLOUD

Si tu app necesita secretos (API keys, contraseñas):

1. En tu app Streamlit Cloud, click en **"Settings"**
2. Ve a la sección **"Secrets"**
3. Pega el contenido de `.streamlit/secrets.toml`:

```toml
[database]
host = "localhost"
password = "secret"
```

4. En tu código Python, accede así:

```python
import streamlit as st
db_password = st.secrets["database"]["password"]
```

---

## 📈 MONITOREAR TU APP

En Streamlit Cloud puedes:

- ✅ Ver estadísticas de uso
- ✅ Revisar logs
- ✅ Pausar/Reanudar app
- ✅ Ver consumo de recursos

---

## 🆘 SOPORTE

Si algo falla:

1. **Revisa los logs** en Streamlit Cloud
2. **Prueba localmente** con los mismos pasos
3. **Verifica que el código** funciona sin importar cambios
4. **Contacta a Streamlit**: https://discuss.streamlit.io

---

## ✨ ¡HECHO!

Tu app está online y accesible desde cualquier navegador 🚀

**Próximos pasos:**
- Comparte tu URL
- Agrega información a tu portafolio
- Itera y mejora basado en feedback

---

<div align="center">

**¡Felicidades por hacer tu app profesional disponible en línea!**

Hecho con ❤️ para desarrolladores

</div>
