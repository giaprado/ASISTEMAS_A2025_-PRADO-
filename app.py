
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Cuestionario de Seguridad", layout="wide")

st.title("Evaluación de Seguridad")
st.markdown("Sube el archivo Excel con las preguntas del cuestionario.")

# Subir archivo Excel
uploaded_file = st.file_uploader("Sube tu archivo de preguntas (Excel)", type=["xlsx"])

if uploaded_file:
    # Leer Excel y limpiar
    df_raw = pd.read_excel(uploaded_file)
    df = df_raw.iloc[1:, 0:2]  # Tomar desde la fila 2, columnas Dominio y Pregunta
    df.columns = ["Dominio", "Pregunta"]
    df = df.dropna().reset_index(drop=True)

    st.write("Cuestionario cargado:")
    st.dataframe(df)

    st.markdown("---")
    st.header("Responde las preguntas")
    respuestas = []

    # Crear sliders para cada pregunta
    for idx, row in df.iterrows():
        valor = st.slider(
            f"{row['Dominio']} - {row['Pregunta']}",
            min_value=1, max_value=5, value=3, step=1,
            key=f"pregunta_{idx}"
        )
        respuestas.append({
            "Dominio": row["Dominio"],
            "Pregunta": row["Pregunta"],
            "Respuesta": valor
        })

    if st.button("Generar Informe"):
        df_resp = pd.DataFrame(respuestas)
        resumen = df_resp.groupby("Dominio")["Respuesta"].mean().reset_index()

        st.subheader("Resumen de Puntuaciones")
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
