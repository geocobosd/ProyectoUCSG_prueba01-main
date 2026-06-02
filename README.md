# 📊 Análisis de Churn Bancario - ProyectoUCSG

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Production](https://img.shields.io/badge/Status-Production-brightgreen.svg)]()

Una aplicación web profesional desarrollada con **Streamlit** para análisis exploratorio y predicción de abandono de clientes en instituciones bancarias.

---

## 🎯 Descripción

Este proyecto proporciona una **interfaz interactiva** para analizar patrones de churn (abandono) en datos bancarios. Permite:

✅ Carga flexible de datasets  
✅ Exploración visual de datos interactiva  
✅ Múltiples análisis comparativos  
✅ Filtros dinámicos personalizables  
✅ Visualizaciones profesionales con Plotly y Matplotlib  
✅ Interfaz responsiva y moderna  

### Caso de Uso
Identifica qué clientes tienen mayor probabilidad de abandonar el banco y qué factores influyen en su decisión, permitiendo tomar acciones preventivas.

---

## 📋 Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Análisis Disponibles](#análisis-disponibles)
- [Deployment](#deployment)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## 🚀 Características

### Análisis Exploratorio
- **Relación Clientes Activos vs Churn**: Analiza cómo la actividad influye en el abandono
- **Antigüedad vs Churn**: Identifica patrones de retención por años de permanencia
- **Productos vs Churn**: Correlaciona la cantidad de productos con abandonos
- **Género vs Churn**: Compara tasas de churn entre géneros
- **Distribución de Churn**: Proporciones de clientes activos/abandonados
- **Análisis de Edades**: Distribución demográfica del churn
- **Análisis Personalizado**: Herramienta flexible con filtros interactivos

### Interfaz Profesional
- 🎨 Tema personalizado (colores corporativos)
- 📱 Diseño responsivo y limpio
- 🎯 Tarjetas de métricas KPI
- 📊 Gráficos interactivos con Plotly
- ⚡ Caché optimizado para rendimiento
- 🔍 Validación automática de datos

---

## 💻 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes Python)
- Git (opcional, para clonar el repositorio)

### Pasos

#### 1. Clonar el Repositorio
```bash
git clone https://github.com/usuario/ProyectoUCSG.git
cd ProyectoUCSG
```

#### 2. Crear Entorno Virtual (Recomendado)
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

---

## 🎮 Uso

### Ejecutar la Aplicación Localmente

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

### Primera Ejecución

1. **La aplicación cargará automáticamente** el dataset `Churn_Modelling.csv`
2. **Visualizarás** un dashboard con métricas principales
3. **Selecciona** un análisis del menú lateral para explorar datos
4. **Aplica filtros** en la sección "Análisis Personalizado" para análisis específicos

### Cargar Dataset Personalizado

1. En la barra lateral, elige "Subir archivo CSV"
2. Selecciona tu archivo
3. El dataset se validará automáticamente

⚠️ **Nota**: El dataset debe contener las columnas: Geography, Gender, Age, Tenure, Balance, CreditScore, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Exited

---

## 📁 Estructura del Proyecto

```
ProyectoUCSG/
│
├── app.py                          # 🎯 Aplicación principal
├── requirements.txt                # 📦 Dependencias
├── README.md                       # 📚 Este archivo
├── .gitignore                      # 🚫 Git ignore
│
├── .streamlit/
│   └── config.toml                 # ⚙️ Configuración de tema
│
├── src/                            # 📂 Código fuente
│   ├── __init__.py
│   ├── config.py                   # 🎨 Colores y constantes
│   ├── data/
│   │   ├── __init__.py
│   │   └── loader.py               # 📥 Carga y validación de datos
│   └── utils/
│       ├── __init__.py
│       └── ui_components.py        # 🎪 Componentes visuales personalizados
│
├── data/
│   └── Churn_Modelling.csv         # 📊 Dataset principal
│
└── assets/
    └── logo.png                    # 🖼️ Logo (opcional)
```

### Descripción de Componentes

| Archivo | Descripción |
|---------|------------|
| `app.py` | Punto de entrada de la aplicación. Contiene toda la lógica de interfaz |
| `src/config.py` | Configuración centralizada: colores, rutas, constantes |
| `src/data/loader.py` | Funciones para cargar, validar y procesar datos |
| `src/utils/ui_components.py` | Componentes visuales reutilizables (tarjetas, encabezados, etc.) |
| `.streamlit/config.toml` | Configuración de tema personalizado de Streamlit |

---

## 📊 Análisis Disponibles

### 1. Clientes Activos vs Abandonados
Compara la tasa de churn entre miembros activos e inactivos.
- **Visualización**: Gráfico de barras
- **Métrica**: Porcentaje de abandono

### 2. Antigüedad vs Churn
Analiza cómo evoluciona el abandono según los años de permanencia.
- **Visualización**: Gráfico de línea con marcadores
- **Rango**: 0-10+ años

### 3. Número de Productos vs Churn
Relación entre cantidad de productos contratados y abandono.
- **Visualización**: Gráfico de barras
- **Categorías**: 1, 2, 3, 4+ productos

### 4. Género vs Churn
Comparación de tasas de churn por género.
- **Visualización**: Gráfico de barras
- **Géneros**: Masculino, Femenino

### 5. Distribución de Churn
Proporción de clientes activos vs abandonados.
- **Visualización**: Gráfico de pastel + tabla de estadísticas
- **Métricas**: Edad promedio, tarjeta de crédito

### 6. Distribución de Edades
Densidad de edades según estado de abandono.
- **Visualización**: Gráfico de densidad KDE
- **Tipo**: Comparativa visual

### 7. Análisis Personalizado
Herramienta flexible para crear análisis personalizados.
- **Filtros**: Geografía, Género
- **Variables**: Selección múltiple de categorías y numéricas

---

## 🌐 Deployment

### Opción 1: Streamlit Cloud (Recomendado)

#### Paso 1: Pushear a GitHub
```bash
git add .
git commit -m "feat: proyecto streamlit profesional"
git push origin main
```

#### Paso 2: Conectar con Streamlit Cloud
1. Ir a [streamlit.io/cloud](https://streamlit.io/cloud)
2. Hacer clic en "Sign in with GitHub"
3. Autorizar Streamlit
4. Hacer clic en "New app"
5. Seleccionar repositorio, rama y archivo (`app.py`)
6. Hacer clic en "Deploy"

**URL de acceso**: `https://[username]-[appname].streamlit.app/`

### Opción 2: Heroku

#### Paso 1: Crear archivos necesarios
```bash
echo "web: streamlit run app.py --logger.level=error" > Procfile
```

#### Paso 2: Deployar
```bash
heroku create tu-app-nombre
git push heroku main
```

### Opción 3: Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501"]
```

```bash
docker build -t churn-app .
docker run -p 8501:8501 churn-app
```

---

## 🔧 Configuración

### Cambiar Tema de Colores
Edita `src/config.py`:

```python
COLORS = {
    "primary": "#1E3A5F",      # Azul marino
    "secondary": "#FF6B35",     # Naranja vibrante
    "accent": "#4ECDC4",        # Turquesa
    # ... más colores
}
```

### Cambiar Ruta de Datos
En `src/config.py`:

```python
DATA_PATH = "tu/ruta/archivo.csv"
```

---

## 📈 Mejoras Futuras

- [ ] Modelo de predicción de churn con ML
- [ ] Integración con base de datos
- [ ] Autenticación de usuarios
- [ ] Reportes automatizados por correo
- [ ] Análisis de cohortes
- [ ] API REST para predicciones
- [ ] Dashboard de real-time
- [ ] Exportación a PDF/Excel

---

## 🐛 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'streamlit'"
**Solución**: Ejecuta `pip install -r requirements.txt`

### Problema: Dataset no encontrado
**Solución**: Verifica que `Churn_Modelling.csv` esté en la carpeta `data/`

### Problema: La app es lenta
**Solución**: El caché está habilitado. Reinicia Streamlit: `streamlit run app.py --logger.level=error`

---

## 👥 Contribuciones

Las contribuciones son bienvenidas! Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

```
MIT License

Copyright (c) 2024 ProyectoUCSG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📞 Contacto

- 📧 Email: tu-email@ejemplo.com
- 🐙 GitHub: [@tuusuario](https://github.com/tuusuario)
- 💼 LinkedIn: [Tu Nombre](https://linkedin.com/in/tunombre)

---

## 🙏 Agradecimientos

- Universidad CASA GRANDE - Maestría en IA y Ciencia de Datos
- Streamlit por el framework
- Plotly y Matplotlib por las visualizaciones
- Comunidad de Python

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub!**

Hecho con ❤️ para análisis de datos

</div>
