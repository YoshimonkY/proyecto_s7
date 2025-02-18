import datetime as dt
import pandas as pd
import plotly.express as px
import streamlit as st


st.title('Coches de Estados Unidos desde 1908 al 2019')        # Titulo
st.header('Descubre las caracteristicas de los vehiculos!')     # encabezado


df = pd.read_csv('vehicles_us.csv')  # cargar dataset

# -------------------------------------------------------------------------------
st.write('Crea un histograma de modelos')
histograma = st.checkbox('Generar')  # crear un botón

if histograma:  # al hacer clic en el botón

    # mensaje
    st.write('Selecciona un rango en el cuadro para amplificar datos')

    fig = px.histogram(df, x="model_year")  # crear un histograma

    st.plotly_chart(fig, use_container_width=True)  # mostrar gráfico
# --------------------------------------------------------------------------------
# crea un boton para un grafico de dispersion
g_dispersion = st.button('Mostrar gráfico de dispersión')

# Al hacer click:
if g_dispersion:

    # Write the message
    st.write(
        'Generaste un grafico de dispersión para el odómetro y el precio. Selecciona un rango para ampliar')
    fig2 = px.scatter(df, x='odometer', y='price')    # Create scatter plot
    st.plotly_chart(fig2, use_container_width=True)     # Show a Scatter plot

# ---------------------------------------------------------------------------------
# Encabezado precios
st.header("Filtro de precios")

# Deslizador de precios
min_price, max_price = st.slider(
    "Selecciona un rango de precios",
    min_value=int(df["price"].min()),
    max_value=int(df["price"].max()),
    value=(int(df["price"].min()), int(df["price"].max()))
)

# Filtrar datos basados en precios
filtered_df = df[(df["price"] >= min_price) & (df["price"] <= max_price)]

# Cuadro hecho con Plotly
fig = px.bar(filtered_df, x="model_year", y="price", title="Filtered Data")

# se muestra el cuadro
st.plotly_chart(fig)


# -------------------------------------------------------------------------------
bar_button = st.button('Genera un ploteo de Barras')

# Al hacer click en boton
if bar_button:

    gb = df.groupby(['model_year', 'type'])['cylinders'].mean().reset_index()
    fig3 = px.bar(gb, x="model_year", y="cylinders", color="type",
                  barmode="stack", title="Cilindros y tipo dependiendo el año")
    st.plotly_chart(fig3, use_container_width=False)     # Mostrar Bar plot

st.write(dt.datetime.now(), 'Proyecto Sprint 7')
