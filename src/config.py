"""
Configuración global y constantes de la aplicación
"""

# ============= COLORES Y TEMA =============
COLORS = {
    "primary": "#1E3A5F",      # Azul marino profesional
    "secondary": "#FF6B35",     # Naranja vibrante
    "accent": "#4ECDC4",        # Turquesa
    "success": "#2ECC71",       # Verde
    "warning": "#F39C12",       # Naranja claro
    "danger": "#E74C3C",        # Rojo
    "light": "#F8F9FA",         # Gris muy claro
    "dark": "#2C3E50",          # Gris oscuro
    "white": "#FFFFFF",
}

# ============= CONFIGURACIÓN DE DATOS =============
DATA_PATH = "data/Churn_Modelling.csv"
LOGO_PATH = "assets/logo.png"

# ============= VARIABLES CATEGÓRICAS Y NUMÉRICAS =============
CATEGORICAL_VARS = [
    "Geography",
    "Gender",
    "HasCrCard",
    "IsActiveMember",
    "Exited"
]

NUMERIC_VARS = [
    "CreditScore",
    "Balance",
    "EstimatedSalary",
    "Age",
    "Tenure",
    "NumOfProducts"
]

# ============= CONFIGURACIÓN DE ANÁLISIS =============
ANALYSIS_OPTIONS = {
    "1. Clientes Activos vs Abandonados": "active_vs_churn",
    "2. Antigüedad vs Churn": "tenure_vs_churn",
    "3. Productos vs Churn": "products_vs_churn",
    "4. Género vs Churn": "gender_vs_churn",
    "5. Distribución de Churn": "churn_distribution",
    "6. Distribución de Edades": "age_distribution",
    "7. Análisis Personalizado": "custom_analysis"
}

# ============= TAMAÑOS Y ESPACIOS =============
CHART_HEIGHT = 500
CHART_WIDTH = 800
PADDING = 20

# ============= MENSAJES Y TEXTOS =============
APP_TITLE = "Análisis de Churn Bancario"
APP_SUBTITLE = "Sistema inteligente de predicción de abandono de clientes"
APP_DESCRIPTION = """
Esta aplicación analiza patrones de abandono de clientes en instituciones bancarias.
Utiliza análisis exploratorio de datos para identificar factores clave que influyen en la retención.
"""
