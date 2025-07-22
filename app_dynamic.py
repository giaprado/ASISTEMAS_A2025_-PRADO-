
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Evaluación de Seguridad Dinámica", layout="wide")

st.title("Evaluación de Seguridad Dinámica")
st.markdown("Selecciona una puntuación (1-5) para cada pregunta y genera el informe con recomendaciones.")

# Cargar el archivo Excel automáticamente
try:
    df_raw = pd.read_excel("AUSBAD Tarea 9 Cuestionario Grupo E.xlsx")
except FileNotFoundError:
    st.error("No se encontró el archivo 'AUSBAD Tarea 9 Cuestionario Grupo E.xlsx'. Asegúrate de que está en el repositorio.")
    st.stop()

# Limpiar y preparar datos
df = df_raw.iloc[1:, 0:2]
df.columns = ["Dominio", "Pregunta"]
df = df.dropna().reset_index(drop=True)

# Crear sliders para que el usuario seleccione puntuaciones
respuestas = []
st.subheader("Responde las Preguntas")
for idx, row in df.iterrows():
    valor = st.slider(f"{row['Dominio']} - {row['Pregunta']}", min_value=1, max_value=5, value=3, step=1)
    respuestas.append({"Dominio": row["Dominio"], "Pregunta": row["Pregunta"], "Respuesta": valor})

if st.button("Generar Informe"):
    df_resp = pd.DataFrame(respuestas)

    # Mostrar respuestas seleccionadas
    st.subheader("Preguntas y Respuestas")
    st.dataframe(df_resp)

    # Resumen por dominio
    resumen = df_resp.groupby("Dominio")["Respuesta"].mean().reset_index()

    st.subheader("Resumen de Puntuaciones por Dominio")
    st.dataframe(resumen)

    # Radar Chart
    fig = px.line_polar(
        resumen, r="Respuesta", theta="Dominio", line_close=True, range_r=[0, 5],
        title="Radar Chart de Promedios por Dominio"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Interpretación y recomendaciones
    st.subheader("Recomendaciones por Dominio")
    for _, row in resumen.iterrows():
        if row["Respuesta"] < 2.1:
            st.error(f"{row['Dominio']}: **Riesgo Alto** ({row['Respuesta']:.2f}) - Recomendación: Tomar medidas correctivas inmediatas.")
        elif row["Respuesta"] < 3.6:
            st.warning(f"{row['Dominio']}: **Riesgo Medio** ({row['Respuesta']:.2f}) - Recomendación: Implementar mejoras para fortalecer controles.")
        else:
            st.success(f"{row['Dominio']}: **Cumplimiento Bueno** ({row['Respuesta']:.2f}) - Recomendación: Mantener los controles y realizar seguimiento.")
