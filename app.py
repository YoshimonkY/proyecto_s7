import pandas as pd
import plotly.express as px
import streamlit as st
import datetime as dt

st.title('Coches de Estados Unidos desde 1908 al 2019')
st.header('Descubre las caracteristicas de los vehiculos!')


df = pd.read_csv('vehicles_us.csv')  # leer los datos
st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
hist_button = st.button('Generar')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Aquí puedes observar el numero de modelos distintos en cada año')

    # crear un histograma
    fig = px.histogram(df, x="model_year")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(df, x='price')
    st.plotly_chart(fig, use_container_width=True)


# Streamlit App
st.text("Filtro de precios")

# Slider to select range
min_price, max_price = st.slider(
    "Selecciona un rango de precios",
    min_value=int(df["price"].min()),
    max_value=int(df["price"].max()),
    value=(int(df["price"].min()), int(df["price"].max()))
)

# Filter data based on selected range
filtered_df = df[(df["price"] >= min_price) & (df["price"] <= max_price)]

# Create Plotly Chart
fig = px.bar(filtered_df, x="model_year", y="price", title="Filtered Data")

# Display chart in Streamlit
st.plotly_chart(fig)


# ---------------------------------------------------------------------
bar_button = st.button('Create a Bar Plot')

# Clicking the button
if bar_button:

    gb = df.groupby(['model_year', 'fuel'])['odometer'].mean().reset_index()
    fig3 = px.bar(gb, x="model_year", y="odometer", color="fuel",
                  barmode="stack", title="Miles per Year model and Fuel type")
    st.plotly_chart(fig3, use_container_width=True)     # Show a Bar plot

st.write(dt.datetime.now(), 'Proyecto Sprint 7')
