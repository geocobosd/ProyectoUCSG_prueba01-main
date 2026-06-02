"""
Funciones para cargar y procesar datos
"""

import pandas as pd
import streamlit as st
from src.config import DATA_PATH, CATEGORICAL_VARS, NUMERIC_VARS


@st.cache_data
def load_dataset(filepath=DATA_PATH):
    """
    Carga el dataset de Churn Bancario
    
    Args:
        filepath: Ruta al archivo CSV
        
    Returns:
        DataFrame con los datos cargados
    """
    try:
        df = pd.read_csv(filepath, index_col=0)
        return df
    except FileNotFoundError:
        st.error(f"No se encontró el archivo: {filepath}")
        return None
    except Exception as e:
        st.error(f"Error al cargar datos: {str(e)}")
        return None


@st.cache_data
def get_data_summary(df):
    """
    Obtiene resumen estadístico del dataset
    
    Args:
        df: DataFrame
        
    Returns:
        Diccionario con estadísticas clave
    """
    if df is None:
        return {}
    
    return {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "churn_rate": (df['Exited'].sum() / len(df)) * 100,
        "active_customers": (df['Exited'] == 0).sum(),
        "churned_customers": df['Exited'].sum(),
    }


def validate_dataframe(df):
    """
    Valida que el DataFrame cumpla con los requisitos mínimos
    
    Args:
        df: DataFrame a validar
        
    Returns:
        Tupla (is_valid, message)
    """
    required_columns = CATEGORICAL_VARS + NUMERIC_VARS
    
    if df is None:
        return False, "El archivo no fue cargado correctamente"
    
    missing_cols = set(required_columns) - set(df.columns)
    if missing_cols:
        return False, f"Faltan columnas: {', '.join(missing_cols)}"
    
    return True, "✓ Datos validados correctamente"
