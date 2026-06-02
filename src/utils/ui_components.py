"""
Componentes visuales personalizados para la interfaz
"""

import streamlit as st
from src.config import COLORS


def metric_card(title, value, icon="📊", color=None):
    """
    Crea una tarjeta de métrica personalizada
    
    Args:
        title: Título de la métrica
        value: Valor a mostrar
        icon: Emoji o ícono
        color: Color del borde (hex)
    """
    color = color or COLORS["primary"]
    
    st.markdown(f"""
        <div style="
            background-color: white;
            border-left: 5px solid {color};
            border-radius: 8px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        ">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <p style="margin: 0; color: #666; font-size: 14px; font-weight: 500;">
                        {title}
                    </p>
                    <p style="margin: 8px 0 0 0; color: {color}; font-size: 32px; font-weight: bold;">
                        {value}
                    </p>
                </div>
                <div style="font-size: 40px;">
                    {icon}
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def section_header(title, icon="📈"):
    """
    Crea un encabezado de sección personalizado
    
    Args:
        title: Título de la sección
        icon: Emoji o ícono
    """
    st.markdown(f"""
        <div style="
            margin-top: 30px;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 3px solid {COLORS['secondary']};
        ">
            <h2 style="margin: 0; color: {COLORS['primary']};">
                {icon} {title}
            </h2>
        </div>
    """, unsafe_allow_html=True)


def info_box(text, box_type="info"):
    """
    Crea una caja de información personalizada
    
    Args:
        text: Texto a mostrar
        box_type: 'info', 'success', 'warning', 'error'
    """
    color_map = {
        "info": COLORS["primary"],
        "success": COLORS["success"],
        "warning": COLORS["warning"],
        "error": COLORS["danger"]
    }
    color = color_map.get(box_type, COLORS["primary"])
    
    st.markdown(f"""
        <div style="
            background-color: rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.1);
            border-left: 4px solid {color};
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
        ">
            <p style="margin: 0; color: {color}; font-size: 14px;">
                {text}
            </p>
        </div>
    """, unsafe_allow_html=True)


def header_app(title, subtitle="", show_divider=True):
    """
    Crea un encabezado principal personalizado para la app
    
    Args:
        title: Título principal
        subtitle: Subtítulo opcional
        show_divider: Mostrar línea divisoria
    """
    st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['dark']} 100%);
            padding: 40px 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        ">
            <h1 style="color: white; margin: 0 0 10px 0;">
                {title}
            </h1>
            {f'<p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 16px;">{subtitle}</p>' if subtitle else ''}
        </div>
    """, unsafe_allow_html=True)


def custom_divider():
    """Crea un divisor personalizado"""
    st.markdown(f"""
        <div style="
            height: 2px;
            background: linear-gradient(90deg, transparent, {COLORS['secondary']}, transparent);
            margin: 30px 0;
        "></div>
    """, unsafe_allow_html=True)


def highlight_text(text, color=None):
    """
    Resalta texto con color personalizado
    
    Args:
        text: Texto a resaltar
        color: Color (hex)
    """
    color = color or COLORS["secondary"]
    st.markdown(f"<span style='color: {color}; font-weight: bold;'>{text}</span>", 
                unsafe_allow_html=True)
