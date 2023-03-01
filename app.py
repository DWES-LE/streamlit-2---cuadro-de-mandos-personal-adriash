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

# Filtrar la lista por juegos compatibles o no con radio button

compatibilidad_opti = st.radio('Mostrar todos los juego publicado por la compañia Bandai Namco',
                    ('Todos','Optimizados', 'No optimizados'))

# Filtrar la lista por compañia utilizando selección múltiple

publisher_select = st.multiselect('Filtro por compañía', list_original.Publisher.unique())

# Filtramos por la compatibilidad con la optimización de la app geforce

if compatibilidad_opti == 'Optimizados':
    list_original = list_original[list_original['Fully Optimized?'] =='Y']
elif compatibilidad_opti == 'No optimizados':
    list_original = list_original[list_original['Fully Optimized?'] == 'N']

# Filtramos los juegos por compañia según la selección múltiple o dejamos la lista igual en caso de que no haya valores en la selección

if publisher_select :
    list = list_original[list_original['Publisher'].isin(publisher_select)]
else:
    list = list_original

# Mostramos la tabla según los filtros que el usuario seleccione

st.write(list)

# Gráficos según su compatibilidad con grabaciones, optimización 

st.subheader('Gráfico según la compatibilidad con la grabación Geforce')
st.bar_chart(list.groupby('Highlights Supported?')['Status'].sum())

st.subheader('Gráfico según la compatibilidad con la optimización Geforce')
st.bar_chart(list.groupby('Fully Optimized?')['Status'].sum())
