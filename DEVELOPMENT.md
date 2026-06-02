# ProyectoUCSG - Guía Rápida de Desarrollo

## Iniciar el proyecto rápidamente

### 1. Instalación Inicial

```bash
# Clonar repositorio
git clone https://github.com/tuusuario/ProyectoUCSG.git
cd ProyectoUCSG

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Ejecutar setup
python setup.py

# O instalar dependencias manualmente
pip install -r requirements.txt
```

### 2. Ejecutar la App

```bash
streamlit run app.py
```

La app estará en: `http://localhost:8501`

---

## Estructura de Módulos

### `app.py`
Archivo principal que contiene:
- Configuración de página
- Estilos personalizados
- Lógica de interfaz
- Integración de componentes

### `src/config.py`
Variables globales:
- Colores corporativos
- Rutas de archivos
- Opciones de análisis
- Listas de variables

**Cambiar colores:**
```python
COLORS = {
    "primary": "#TU_COLOR",
    ...
}
```

### `src/data/loader.py`
Funciones de datos:
- `load_dataset()` - Carga CSV con caché
- `get_data_summary()` - Estadísticas principales
- `validate_dataframe()` - Valida columnas

**Usar:**
```python
from src.data.loader import load_dataset
df = load_dataset("ruta/archivo.csv")
```

### `src/utils/ui_components.py`
Componentes visuales reutilizables:
- `metric_card()` - Tarjetas de métricas
- `section_header()` - Encabezados de sección
- `header_app()` - Encabezado principal
- `info_box()` - Cajas de información

**Usar:**
```python
from src.utils.ui_components import metric_card
metric_card("Título", "100", "📊", "#1E3A5F")
```

---

## Agregar Nuevos Análisis

### Paso 1: Agregar opción en `src/config.py`
```python
ANALYSIS_OPTIONS = {
    ...
    "8. Mi nuevo análisis": "mi_analisis",
}
```

### Paso 2: Agregar lógica en `app.py`
```python
elif modulo == "8. Mi nuevo análisis":
    st.subheader("Mi Nuevo Análisis")
    
    # Tu código aquí
    resultado = df.groupby("columna").agg(...)
    st.dataframe(resultado)
    
    fig = px.bar(resultado, ...)
    st.plotly_chart(fig, use_container_width=True)
```

---

## Personalizar Tema

### Cambiar colores principales

Editar `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#TU_COLOR_PRIMARIO"
secondaryBackgroundColor = "#TU_COLOR_FONDO"
textColor = "#TU_COLOR_TEXTO"
```

### Cambiar estilos CSS

En `app.py`, modificar la sección de estilos:
```python
st.markdown("""
    <style>
    /* Tus estilos aquí */
    .stButton > button {
        background-color: #TU_COLOR;
    }
    </style>
""", unsafe_allow_html=True)
```

---

## Caché y Rendimiento

### Cachear datos
```python
@st.cache_data
def mi_funcion():
    return pd.read_csv("archivo.csv")
```

### Cachear visualizaciones
```python
@st.cache_resource
def crear_figura():
    return plt.figure()
```

### Limpiar caché
```bash
streamlit cache clear
```

---

## Debugging

### Ver logs
```bash
streamlit run app.py --logger.level=debug
```

### Usar st.write() para debugging
```python
st.write("Valor de debug:", variable)
```

### Session state
```python
st.session_state.mi_variable = valor
```

---

## Deployment en Streamlit Cloud

### 1. Pushear a GitHub
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### 2. Conectar en Streamlit Cloud
- Ir a https://share.streamlit.io
- Conectar GitHub
- Seleccionar repo y branch
- Seleccionar `app.py`
- Deploy automático ✓

### 3. Compartir
Tu app estará en: `https://[username]-[appname].streamlit.app/`

---

## Buenas Prácticas

✅ **Siempre:**
- Usar `@st.cache_data` para datos
- Validar entrada de usuarios
- Usar nombres descriptivos
- Documentar funciones

❌ **Nunca:**
- Guardar credenciales en el código
- Usar variables globales mutables
- Queries sin validar en BD
- Hacer requests sin timeout

---

## Tips Útiles

### Medir rendimiento
```python
import time
start = time.time()
# tu código
st.write(f"Tiempo: {time.time() - start:.2f}s")
```

### Mostrar progreso
```python
with st.spinner('Cargando...'):
    time.sleep(3)
st.success('¡Listo!')
```

### Columnas responsivas
```python
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Contenido 1")
```

---

Para más información: Ver `README.md`

Happy coding! 🚀
