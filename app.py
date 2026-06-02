"""
ProyectoUCSG - Análisis de Churn Bancario
Aplicación profesional de análisis exploratorio de datos 
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from src.config import COLORS, ANALYSIS_OPTIONS, CATEGORICAL_VARS, NUMERIC_VARS, APP_DESCRIPTION
from src.data.loader import load_dataset, get_data_summary, validate_dataframe
from src.utils.ui_components import (
    metric_card, section_header, header_app, custom_divider,
    info_box, highlight_text
)

# ============= CONFIGURACIÓN DE PÁGINA =============
st.set_page_config(
    page_title="Análisis de Churn Bancario",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============= ESTILOS PERSONALIZADOS =============
st.markdown("""
    <style>
    /* Principal container */
    .main {
        padding: 20px;
        background-color: #F8F9FA;
    }
    
    /* Sidebar personalizado */
    .sidebar .sidebar-content {
        background-color: #1E3A5F;
    }
    
    /* Botones personalizados */
    .stButton > button {
        background-color: #FF6B35;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #E55A24;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transform: translateY(-2px);
    }
    
    /* Selectbox personalizado */
    .stSelectbox {
        margin: 10px 0;
    }
    
    /* Tablas */
    .dataframe {
        border-radius: 5px;
        overflow: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# ============= INICIALIZAR SESSION STATE =============
if "data_loaded" not in st.session_state:
    st.session_state.data_loaded = False
if "df" not in st.session_state:
    st.session_state.df = None


# ============= BARRA LATERAL =============
def sidebar_config():
    """Configura la barra lateral"""
    st.sidebar.markdown("""
        <div style="
            background: linear-gradient(135deg, #1E3A5F 0%, #2C3E50 100%);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        ">
            <h2 style="color: white; text-align: center; margin: 0;">
                📊 ANÁLISIS DE CHURN
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    # Logo
    try:
        st.sidebar.image("assets/logo.png", use_column_width=True)
    except:
        pass
    
    st.sidebar.markdown("---")


# ============= FUNCIÓN PRINCIPAL =============
def main():
    """Función principal de la aplicación"""
    
    # Encabezado
    header_app(
        "📊 Análisis de Churn Bancario",
        "Sistema inteligente de predicción de abandono de clientes"
    )
    
    st.markdown(APP_DESCRIPTION)
    custom_divider()
    
    # Configurar sidebar
    sidebar_config()
    
    # ========== CARGA DE DATOS ==========
    st.sidebar.header("1️⃣ Cargar Datos")
    
    upload_option = st.sidebar.radio(
        "Selecciona una opción:",
        ["Usar dataset predeterminado", "Subir archivo CSV"]
    )
    
    df = None
    
    if upload_option == "Usar dataset predeterminado":
        df = load_dataset()
        if df is not None:
            st.session_state.data_loaded = True
            st.session_state.df = df
            st.sidebar.success("✓ Dataset cargado")
    else:
        uploaded_file = st.sidebar.file_uploader("Sube un archivo CSV", type=["csv"])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.session_state.data_loaded = True
            st.session_state.df = df
            st.sidebar.success("✓ Archivo cargado")
    
    if df is None:
        df = st.session_state.df
    
    # Si no hay datos cargados, mostrar mensaje
    if df is None:
        st.error("⚠️ No hay datos cargados. Por favor carga un dataset.")
        return
    
    # Validar datos
    is_valid, message = validate_dataframe(df)
    if not is_valid:
        st.error(f"❌ Error en los datos: {message}")
        return
    
    st.sidebar.success(message)
    
    # ========== PREVISUALIZACIÓN DE DATOS ==========
    section_header("📋 Previsualización del Dataset", "📋")
    
    col1, col2, col3, col4 = st.columns(4)
    
    summary = get_data_summary(df)
    with col1:
        metric_card("Registros", f"{summary['total_rows']:,}", "📦", COLORS["primary"])
    with col2:
        metric_card("Columnas", summary['total_columns'], "📊", COLORS["accent"])
    with col3:
        metric_card("Tasa de Churn", f"{summary['churn_rate']:.1f}%", "📉", COLORS["danger"])
    with col4:
        metric_card("Clientes Activos", f"{summary['active_customers']:,}", "✓", COLORS["success"])
    
    st.write("**Primeros registros del dataset:**")
    st.dataframe(df.head(), use_container_width=True)
    
    custom_divider()
    
    # ========== EXPLORACIÓN DE DATOS ==========
    st.sidebar.header("2️⃣ Exploración de Datos")
    
    section_header("🔍 Análisis Exploratorio", "🔍")
    
    modulo = st.sidebar.selectbox(
        "Selecciona un análisis:",
        list(ANALYSIS_OPTIONS.keys())
    )
    
    # 1. Clientes Activos vs Abandonados
    if modulo == "1. Clientes Activos vs Abandonados":
        st.subheader("Relación de Clientes Activos vs Abandonados")
        
        resultado = (
            df.groupby("IsActiveMember")["Exited"]
            .mean()
            .mul(100)
            .round(2)
            .reset_index()
        )
        resultado["Exited"] = resultado["Exited"].astype(str) + "%"
        resultado.columns = ["Miembro Activo", "Tasa de Abandono (%)"]
        
        st.dataframe(resultado, use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(
                resultado,
                x="Miembro Activo",
                y="Tasa de Abandono (%)",
                color="Miembro Activo",
                color_discrete_map={"0": COLORS["success"], "1": COLORS["primary"]},
                title="Tasa de Abandono por Estado de Actividad"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # 2. Antigüedad vs Churn
    elif modulo == "2. Antigüedad vs Churn":
        st.subheader("Relación de Años de Permanencia vs Abandono")
        
        resultado = (
            df.groupby("Tenure")["Exited"]
            .mean()
            .mul(100)
            .round(2)
            .reset_index()
        )
        
        st.dataframe(resultado, use_container_width=True)
        
        fig = px.line(
            resultado,
            x="Tenure",
            y="Exited",
            markers=True,
            title="Evolución de Tasa de Churn según Antigüedad",
            labels={"Tenure": "Años de Antigüedad", "Exited": "Tasa de Abandono (%)"},
            color_discrete_sequence=[COLORS["secondary"]]
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # 3. Número de Productos vs Churn
    elif modulo == "3. Productos vs Churn":
        st.subheader("Relación de Número de Productos vs Abandono")
        
        resultado = (
            df.groupby("NumOfProducts")["Exited"]
            .mean()
            .mul(100)
            .round(2)
            .reset_index()
        )
        resultado["Exited"] = resultado["Exited"].astype(str) + "%"
        resultado.columns = ["Número de Productos", "Tasa de Abandono (%)"]
        
        st.dataframe(resultado, use_container_width=True)
        
        fig = px.bar(
            resultado,
            x="Número de Productos",
            y="Tasa de Abandono (%)",
            color="Número de Productos",
            color_discrete_sequence=[COLORS["accent"], COLORS["warning"], COLORS["danger"], COLORS["secondary"]],
            title="Tasa de Abandono por Número de Productos"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # 4. Género vs Churn
    elif modulo == "4. Género vs Churn":
        st.subheader("Relación de Género vs Abandono")
        
        resultado = (
            df.groupby("Gender")["Exited"]
            .mean()
            .mul(100)
            .round(2)
            .reset_index()
        )
        resultado["Exited"] = resultado["Exited"].astype(str) + "%"
        resultado.columns = ["Género", "Tasa de Abandono (%)"]
        
        st.dataframe(resultado, use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(
                resultado,
                x="Género",
                y="Tasa de Abandono (%)",
                color="Género",
                color_discrete_map={"M": COLORS["primary"], "F": COLORS["secondary"]},
                title="Tasa de Abandono por Género"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # 5. Distribución de Churn
    elif modulo == "5. Distribución de Churn":
        st.subheader("Distribución de Clientes por Estado")
        
        col1, col2 = st.columns(2)
        
        with col1:
            resultado = df["Exited"].value_counts().reset_index()
            resultado.columns = ["Estado", "Cantidad"]
            resultado["Estado"] = resultado["Estado"].map({0: "Activos", 1: "Abandonados"})
            st.dataframe(resultado, use_container_width=True)
        
        with col2:
            fig = px.pie(
                resultado,
                values="Cantidad",
                names="Estado",
                color_discrete_sequence=[COLORS["success"], COLORS["danger"]],
                title="Proporción de Churn"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        info_box(
            f"Edad promedio de clientes activos: {df[df['Exited']==0]['Age'].mean():.1f} años | "
            f"Edad promedio de clientes que se fueron: {df[df['Exited']==1]['Age'].mean():.1f} años",
            "info"
        )
    
    # 6. Distribución de Edades
    elif modulo == "6. Distribución de Edades":
        st.subheader("Distribución de Edades según Estado de Abandono")
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.kdeplot(
            data=df,
            x="Age",
            hue="Exited",
            fill=True,
            ax=ax,
            palette={0: COLORS["success"], 1: COLORS["danger"]}
        )
        ax.set_title("Distribución de Edades por Estado", fontsize=14, fontweight="bold")
        ax.set_xlabel("Edad (años)")
        ax.set_ylabel("Densidad")
        ax.legend(labels=["Activos", "Abandonados"])
        plt.tight_layout()
        st.pyplot(fig)
    
    # 7. Análisis Personalizado
    elif modulo == "7. Análisis Personalizado":
        st.subheader("Análisis Personalizado")
        
        col1, col2 = st.columns(2)
        
        with col1:
            cat_sel = st.multiselect(
                "Selecciona variables categóricas",
                CATEGORICAL_VARS,
                default=["Geography", "Gender"],
                max_selections=2
            )
        
        with col2:
            num_sel = st.multiselect(
                "Selecciona variables numéricas",
                NUMERIC_VARS,
                default=["CreditScore", "Balance"],
                max_selections=2
            )
        
        st.markdown("---")
        
        # Filtros
        st.subheader("📍 Filtros Interactivos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if "Geography" in df.columns:
                geography_filter = st.multiselect(
                    "Filtrar por Geografía",
                    df["Geography"].unique(),
                    default=df["Geography"].unique()
                )
            else:
                geography_filter = None
        
        with col2:
            if "Gender" in df.columns:
                gender_filter = st.multiselect(
                    "Filtrar por Género",
                    df["Gender"].unique(),
                    default=df["Gender"].unique()
                )
            else:
                gender_filter = None
        
        # Aplicar filtros
        df_filtrado = df.copy()
        
        if geography_filter:
            df_filtrado = df_filtrado[df_filtrado["Geography"].isin(geography_filter)]
        if gender_filter:
            df_filtrado = df_filtrado[df_filtrado["Gender"].isin(gender_filter)]
        
        st.info(f"✓ Se muestran {len(df_filtrado):,} de {len(df):,} registros")
        
        # Gráficos
        for cat in cat_sel:
            if cat in df_filtrado.columns:
                fig = px.histogram(
                    df_filtrado,
                    x=cat,
                    title=f"Distribución de {cat}",
                    color_discrete_sequence=[COLORS["primary"]]
                )
                st.plotly_chart(fig, use_container_width=True)
    
    custom_divider()
    
    # ========== FOOTER ==========
    st.markdown("""
        <div style="
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            border-top: 1px solid #ddd;
            color: #666;
        ">
            <p>🚀 ProyectoUCSG | Análisis de Churn Bancario v1.0</p>
            <p style="font-size: 12px;">Desarrollado con ❤️ usando Streamlit</p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
