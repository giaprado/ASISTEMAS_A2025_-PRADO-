
# Evaluación de Seguridad – Streamlit App

Esta aplicación web permite evaluar dominios de seguridad mediante un cuestionario dinámico cargado desde un archivo Excel.

## **Características principales**
- Carga un archivo Excel con preguntas y dominios.
- Responde cada pregunta mediante sliders (1 a 5).
- Calcula automáticamente el promedio por dominio.
- Genera un gráfico **Radar Chart** interactivo con los promedios.
- Muestra indicadores tipo semáforo (Riesgo Alto, Medio, Bueno).
- Proporciona interpretación textual de los resultados.

---

## **¿Cómo usar la aplicación?**
1. Accede a la aplicación desde el siguiente enlace:  
   **[Abrir la app en Streamlit](https://sistemascuestionario-grupoe-2025.streamlit.app)**
2. Sube el archivo Excel con las preguntas del cuestionario (por ejemplo, `AUSBAD Tarea 9 Cuestionario Grupo E.xlsx`).
3. Responde todas las preguntas moviendo los sliders.
4. Haz clic en **"Generar Informe"** para ver:
   - Tabla con promedios.
   - Radar Chart interactivo.
   - Indicadores de riesgo (Rojo, Amarillo, Verde).

---

## **Ejecución local (opcional)**
Si deseas ejecutar el proyecto en tu computadora:

### **1. Clonar el repositorio**
```bash
git clone https://github.com/AdrianValencia04/ASISTEMAS_2025_VALENCIA.git
cd ASISTEMAS_2025_VALENCIA
```

### **2. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### **3. Ejecutar la aplicación**
```bash
streamlit run app.py
```

---

## **Archivos del proyecto**
- **app.py** – Código principal de la aplicación.
- **requirements.txt** – Librerías necesarias para ejecutar la app.
- **AUSBAD Tarea 9 Cuestionario Grupo E.xlsx** – Archivo Excel con las preguntas.
- **README.md** – Este archivo de documentación.

---

## **Captura de Pantalla**
![Captura de la App](https://i.imgur.com/ExampleImage.png)

---
