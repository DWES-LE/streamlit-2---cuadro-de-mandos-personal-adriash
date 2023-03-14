import pandas as pd
import streamlit as st
import altair as alt

# Importamos la el archivo que contiene la lista de juegos

URL = 'Games.csv'
list_original = pd.read_csv(URL)


# Título

st.title('Lista de juegos')
st.markdown(' Lista de juegos capaces de enlazarse con la aplicación (geforce) dedicada a las tarjetas gráficas Nvidia')
st.markdown('---')
st.markdown('## Filtros para la lista')

# Filtrar la lista por juegos compatibles o no con radio button

st.subheader('Filtro por compatibilidad respecto a la optimización')

compatibilidad_opti = st.radio('Mostrar todos los juegos filtrados según su compatibilidad con la herramienta de optimización del programa geforce.',
                    ('Todos','Optimizados', 'No optimizados'))

# Filtrar la lista por compañia utilizando selección múltiple

st.subheader('Filtro por empresa desarrolladora')

publisher_select = st.multiselect('Filtro por compañía', list_original.Publisher.unique())
st.markdown('---')
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

st.subheader('Tabla de juegos')

st.write(list)

# Filtrar juegos por título

st.markdown('---')

st.subheader('Búsqueda por título')


title_select = st.text_input('Escribe el título del juego que deseas buscar', 'Absolver')
list_busqueda = list_original[list_original['Title'] == title_select]

st.dataframe(list_busqueda, 1000, 100)

# Gráficas según su compatibilidad con grabaciones, optimización 

st.markdown('---')

st.markdown('## Gráficas')

st.subheader('Gráfico según la compatibilidad con la grabación Geforce')
st.markdown('Este gráfico divide en 2 la lista, separa los juegos compatibles con la tecnología de grabación del programa geforce')
st.markdown('Y = compatible con la tecnología   N = no compatible con la tecnología')
st.bar_chart(list.groupby('Highlights Supported?')['Status'].sum())
st.markdown('(Esta gráfica es afectada por los filtros de la zona superior de la página)')

st.subheader('Gráfico según la compatibilidad con la optimización Geforce')
st.markdown('Este gráfico divide en 2 la lista, separa los juegos compatibles con la tecnología de optimización del programa geforce')
st.markdown('Y = compatible con la tecnología   N = no compatible con la tecnología')
st.bar_chart(list.groupby('Fully Optimized?')['Status'].sum())
st.markdown('(Esta gráfica es afectada por los filtros de la zona superior de la página)')

#Gráfica respecto a géneros

st.subheader('Gráfico según empresa o grupo de géneros')
selector_grafica = st.selectbox('Escoge si quieres ver la gráfica en base al grupo de géneros o a la empresa que publicó el juego', ('Publisher', 'Genre'))

side_chart = (
    alt.Chart(list_original)
    .mark_bar()
    .encode(
        x=alt.X(selector_grafica, type='nominal'),
        y=alt.Y('count()', title="Cantidad de juegos", type='quantitative'),
        color=alt.Color(selector_grafica, type='nominal')
    )
    .properties(
        width=600,
    )
)

st.altair_chart(side_chart, use_container_width=True)