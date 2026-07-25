import pandas as pd
import streamlit as st
import plotly.graph_objects as go

car_data = pd.read_csv("vehicles_us.csv")
st.header("Análisis de Datos de Vehículos")
hist_button = st.button("Mostrar Histograma")
if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches"
    )

    fig = go.Figure(data=[go.Histogram(x=car_data["odometer"])])
    fig.update_layout(title_text="Distribución del Odómetro")

    st.plotly_chart(fig, use_container_width=True)


dispersion_button = st.button("Mostrar Gráfico de Dispersión")
if dispersion_button:
    st.write(
        "Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches"
    )

    fig = go.Figure(
        data=[go.Scatter(x=car_data["odometer"], y=car_data["price"], mode="markers")]
    )
    fig.update_layout(title_text="Relación entre Odómetro y Precio")

    st.plotly_chart(fig, use_container_width=True)
