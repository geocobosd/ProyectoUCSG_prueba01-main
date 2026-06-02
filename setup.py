"""
Script de setup y validación del proyecto
Ejecutar: python setup.py
"""

import os
import sys
import subprocess
from pathlib import Path


def print_header(text):
    """Imprime un encabezado formateado"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")


def check_python_version():
    """Verifica la versión de Python"""
    print_header("Verificando Python")
    
    version = sys.version_info
    required_version = (3, 8)
    
    if version >= required_version:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"✗ Se requiere Python 3.8 o superior. Instalado: {version.major}.{version.minor}")
        return False


def check_required_files():
    """Verifica que existan los archivos requeridos"""
    print_header("Verificando Archivos")
    
    required_files = [
        "app.py",
        "requirements.txt",
        "README.md",
        "data/Churn_Modelling.csv",
        ".streamlit/config.toml",
        "src/config.py",
        "src/data/loader.py",
        "src/utils/ui_components.py"
    ]
    
    all_exist = True
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} - NO ENCONTRADO")
            all_exist = False
    
    return all_exist


def install_dependencies():
    """Instala las dependencias"""
    print_header("Instalando Dependencias")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install",
            "-r", "requirements.txt", "-q"
        ])
        print("✓ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError:
        print("✗ Error al instalar dependencias")
        return False


def validate_dataset():
    """Valida que el dataset tenga las columnas requeridas"""
    print_header("Validando Dataset")
    
    try:
        import pandas as pd
        
        df = pd.read_csv("data/Churn_Modelling.csv", index_col=0)
        
        required_columns = [
            "Geography", "Gender", "Age", "Tenure", "Balance",
            "CreditScore", "NumOfProducts", "HasCrCard",
            "IsActiveMember", "EstimatedSalary", "Exited"
        ]
        
        missing_cols = [col for col in required_columns if col not in df.columns]
        
        if missing_cols:
            print(f"✗ Faltan columnas: {', '.join(missing_cols)}")
            return False
        
        print(f"✓ Dataset válido ({len(df):,} registros, {len(df.columns)} columnas)")
        return True
        
    except FileNotFoundError:
        print("✗ Archivo data/Churn_Modelling.csv no encontrado")
        return False
    except Exception as e:
        print(f"✗ Error al validar dataset: {str(e)}")
        return False


def main():
    """Función principal"""
    print("\n" + "🚀 "*30)
    print("ProyectoUCSG - Script de Setup")
    print("🚀 "*30)
    
    checks = [
        ("Python", check_python_version()),
        ("Archivos", check_required_files()),
        ("Dependencias", install_dependencies()),
        ("Dataset", validate_dataset())
    ]
    
    print_header("Resumen de Validación")
    
    for name, result in checks:
        status = "✓ OK" if result else "✗ ERROR"
        print(f"{name:20} {status}")
    
    all_ok = all(result for _, result in checks)
    
    if all_ok:
        print_header("✓ Todo está listo!")
        print("\nPara ejecutar la app, usa:\n  streamlit run app.py\n")
        return 0
    else:
        print_header("✗ Hay problemas que corregir")
        print("\nPor favor, revisa los errores anteriores.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
