import pandas as pd
import streamlit as st

import plotly.express as px

# Leer el dataset
df_vehicles = pd.read_csv("vehicles_us.csv")

# Encabezado
st.header("Análisis de anuncios de vehículos en EE.UU.")

# Botón para histograma
if st.button("Construir histograma"):
    st.write("Distribución del odómetro")
    
    fig_hist = px.histogram(
        df_vehicles,
        x="odometer",
        title="Distribución del Odómetro"
    )
    
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para gráfico de dispersión
if st.button("Construir gráfico de dispersión"):
    st.write("Relación entre precio y odómetro")
    
    fig_scatter = px.scatter(
        df_vehicles,
        x="odometer",
        y="price",
        title="Precio vs Odómetro"
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)