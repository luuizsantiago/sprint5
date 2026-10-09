import pandas as pd
import plotly.express as px
import streamlit as st

# ler os dados (o app roda a partir da raiz do projeto)
car_data = pd.read_csv('vehicles.csv')

# cabeçalho
st.header('Painel de anúncios de carros')

# botão do histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma da quilometragem (odometer)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

# botão do gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão: quilometragem x preço')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig)
