import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Importamos la el archivo que contiene la lista de juegos

URL = 'Games.csv'
list_original = pd.read_csv(URL)

list_original['Status'] = list_original['Status'].astype(int)
# Título

st.title('Lista de juegos Geforce')

# Filtrar la lista por compañia

bandai_games = st.checkbox('Mostrar todos los juego publicado por la compañia Bandai Namco')
devolver_games = st.checkbox('Mostrar todos los juego publicado por la compañia Devolver Digital')
bethesda = st.checkbox('Mostrar todos los juego publicado por la compañia Bethesda')

#filtramos los juegos con los atributos de compañias

if (bandai_games) & (devolver_games) & (bethesda):
    list = list_original[(list_original['Publisher'] == 'BANDAI NAMCO Studio Inc.') | (list_original['Publisher'] == 'BANDAI NAMCO Entertainment') | (list_original['Publisher'] == 'Devolver Digital') | (list_original['Publisher'] == 'Bethesda Softworks')]
elif (bandai_games) & (devolver_games):
    list = list_original[(list_original['Publisher'] == 'BANDAI NAMCO Studio Inc.') | (list_original['Publisher'] == 'BANDAI NAMCO Entertainment') | (list_original['Publisher'] == 'Devolver Digital')]
elif (devolver_games) & (bethesda):
    list = list_original[(list_original['Publisher'] == 'Devolver Digital') | (list_original['Publisher'] == 'Bethesda Softworks')]
elif (bandai_games) & (bethesda):
    list = list_original[(list_original['Publisher'] == 'BANDAI NAMCO Studio Inc.') | (list_original['Publisher'] == 'BANDAI NAMCO Entertainment') | (list_original['Publisher'] == 'Bethesda Softworks')]
elif bandai_games:
    list = list_original[(list_original['Publisher'] == 'BANDAI NAMCO Studio Inc.') | (list_original['Publisher'] == 'BANDAI NAMCO Entertainment')]
elif devolver_games:
    list = list_original[list_original['Publisher'] == 'Devolver Digital']
elif bethesda:
    list = list_original[list_original['Publisher'] == 'Bethesda Softworks']
else:
    list = list_original

# Mostramos la tabla según los filtros que el usuario seleccione

st.write(list)

# Gráficos según su compatibilidad con grabaciones, optimización 

st.subheader('Gráfico según la compatibilidad con la grabación Geforce')
st.bar_chart(list.groupby('Highlights Supported?')['Status'].sum())

st.subheader('Gráfico según la compatibilidad con la optimización Geforce')
st.bar_chart(list.groupby('Fully Optimized?')['Status'].sum())

# Creamos una gráfica a través de matplotlib

plt.bar(list.groupby('Fully Optimized?')['Status'].sum())