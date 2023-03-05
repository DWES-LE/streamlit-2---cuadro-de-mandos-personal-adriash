# DOCUMENTACIÓN

## Temática de datos

Los datos tratan sobre diferentes juegos compatibles con el programa geforce now, un programa con la función de optimizar las opciones 
gráficas de diferentes juegos

## Procedencia de los datos

He extraido los datos desde un archivo excel convertido en csv
procedente de un foro de nvidia (https://www.reddit.com/r/GeForceNOW/comments/ez698b/full_list_of_available_games_in_json/).
Este json contiene todo tipo de informacion de cada juego.

##Campos que contiene cada elemento

El primer campo se trata del id del elemento, el cual como su nombre nos indica sirve para identificar el juego, pero no 
es un recurso que se pueda utilizar para la comparación de datos en una gráfica, solo sirve para la representación de elementos
en una lista.

El siguiente campo es el título del juego, tiene los mismos usos que el identificador pero es una manera más clara de diferenciar cada
elemento para el usuario.

Los dos siguientes campos están dedicados a la verificación de la compatibilidad de cada juego con diferentes opciones del programa Geforce,
estos campos son datos que nos dan la capacidad de compararlos y filtrarlos con gráficas y listas.

La URL sería un campo totalmente inutil con la excepción de recopilación externa de datos desde una lista.

Los dos últimos campos nos ayudan a filtrar los elementos por empresa que lo ha desarrollado o el género del mismo.
El campo status no tiene más utilidad que individualizar los juegos ya que al estar todos los juegos correctamente publicados, el valor del 
elemento siempre es 1.
