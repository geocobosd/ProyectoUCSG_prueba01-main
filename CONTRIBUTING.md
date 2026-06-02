# 🤝 Guía de Contribución - ProyectoUCSG

¡Gracias por tu interés en contribuir a ProyectoUCSG! 🎉

## Código de Conducta

Este proyecto adopta un código de conducta inclusivo. Esperamos que todos los contribuyentes se adhieran a él.

---

## ¿Cómo Contribuir?

### 1. Reportar Bugs

Si encuentras un bug, crea un issue con:
- **Título claro y descriptivo**
- **Descripción detallada del problema**
- **Pasos para reproducirlo**
- **Comportamiento esperado vs actual**
- **Screenshots** (si aplica)

**Ejemplo:**
```
Título: Error al cargar dataset con columnas faltantes

Descripción:
La app se crashea cuando el CSV falta la columna 'Exited'

Pasos:
1. Subir CSV sin columna 'Exited'
2. Hacer clic en "Cargar"
3. Error: KeyError

Esperado: Mostrar mensaje de error claro
```

### 2. Sugerir Mejoras

- Abre un issue con etiqueta `enhancement`
- Describe la mejora propuesta
- Explica por qué sería útil
- Proporciona ejemplos si es posible

### 3. Enviar Pull Requests

#### Proceso:

1. **Fork el repositorio**
   ```bash
   # En GitHub: click en "Fork"
   ```

2. **Clonar tu fork**
   ```bash
   git clone https://github.com/TU_USUARIO/ProyectoUCSG.git
   cd ProyectoUCSG
   ```

3. **Crear rama de feature**
   ```bash
   git checkout -b feature/descripcion-clara
   # Ejemplos:
   # git checkout -b feature/agregar-analisis-rfm
   # git checkout -b bugfix/validar-datos-entrada
   ```

4. **Hacer cambios**
   - Seguir el estilo de código existente
   - Mantener código limpio y legible
   - Agregar comentarios donde sea necesario

5. **Commit con mensajes claros**
   ```bash
   git commit -m "feat: agregar análisis de RFM"
   git commit -m "fix: validación de datos nula"
   git commit -m "docs: actualizar README"
   ```

   **Convención de mensajes:**
   - `feat:` para nuevas características
   - `fix:` para correcciones
   - `docs:` para documentación
   - `style:` para formato de código
   - `refactor:` para refactorización
   - `test:` para pruebas

6. **Push a tu fork**
   ```bash
   git push origin feature/descripcion-clara
   ```

7. **Abrir Pull Request**
   - En GitHub, haz clic en "New Pull Request"
   - Asegúrate de que base sea `main`
   - Llena el template del PR

---

## Estándares de Código

### Python
- Seguir [PEP 8](https://pep8.org/)
- Usar nombres descriptivos
- Agregar docstrings a funciones
- Máximo 100 caracteres por línea

**Ejemplo:**
```python
def load_dataset(filepath: str) -> pd.DataFrame:
    """
    Carga un dataset CSV.
    
    Args:
        filepath: Ruta al archivo CSV
        
    Returns:
        DataFrame con los datos cargados
        
    Raises:
        FileNotFoundError: Si el archivo no existe
    """
    df = pd.read_csv(filepath)
    return df
```

### Streamlit
- Usar caché: `@st.cache_data` para datos
- Organizar código en módulos
- Usar componentes reutilizables
- Validar entrada de usuarios

### Estructura de Commits
```
feat: agregar análisis de RFM

- Agregar módulo de análisis RFM
- Crear visualizaciones de Recency, Frequency, Monetary
- Documentar uso en README

Closes #123
```

---

## Proceso de Review

1. **El mantenedor revisará** el PR
2. **Se pueden solicitar cambios** para mejorar la calidad
3. **Una vez aprobado**, se hará merge a `main`
4. **Tu contribución estará publicada** en la siguiente versión

---

## Área de Enfoque

Buscamos contribuciones en:

- ✨ **Nuevas análisis** de churn
- 📊 **Nuevas visualizaciones** con Plotly
- 🎨 **Mejoras de interfaz** y UX
- 📚 **Documentación** mejorada
- 🐛 **Correcciones de bugs**
- ⚡ **Optimizaciones de rendimiento**
- 🧪 **Tests y validaciones**

---

## Preguntas?

- Abre un issue con la etiqueta `question`
- Contacta a los mantenedores
- Revisa la documentación existente

---

## Agradecimientos

¡Apreciamos tu contribución! Todos los colaboradores serán mencionados en:
- README.md
- Changelog
- Página de contributors

---

<div align="center">

**¡Gracias por ayudar a mejorar ProyectoUCSG!** 🚀

Made with ❤️ by the ProyectoUCSG community

</div>
