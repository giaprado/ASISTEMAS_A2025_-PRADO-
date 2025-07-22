
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Informe de Evaluación de Seguridad", layout="wide")

st.title("Informe de Evaluación de Seguridad")
st.markdown("La siguiente evaluación fue generada automáticamente usando el cuestionario en Excel incluido en el repositorio.")

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

# Simular respuesta con valor fijo (ejemplo: 3)
respuestas = [{"Dominio": row["Dominio"], "Pregunta": row["Pregunta"], "Respuesta": 3} for _, row in df.iterrows()]

df_resp = pd.DataFrame(respuestas)
resumen = df_resp.groupby("Dominio")["Respuesta"].mean().reset_index()

st.subheader("Resumen de Puntuaciones por Dominio")
st.dataframe(resumen)

# Radar Chart
fig = px.line_polar(
    resumen, r="Respuesta", theta="Dominio", line_close=True, range_r=[0, 5],
    title="Radar Chart de Promedios por Dominio"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Interpretación de Resultados")
for _, row in resumen.iterrows():
    if row["Respuesta"] < 2.1:
        st.error(f"{row['Dominio']}: **Riesgo Alto** ({row['Respuesta']:.2f})")
    elif row["Respuesta"] < 3.6:
        st.warning(f"{row['Dominio']}: **Riesgo Medio** ({row['Respuesta']:.2f})")
    else:
        st.success(f"{row['Dominio']}: **Cumplimiento Bueno** ({row['Respuesta']:.2f})")
