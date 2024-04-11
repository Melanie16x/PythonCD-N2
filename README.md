# Trabajo Practico N° 2 - Python para ciencia de datos

Este sistema tiene como objetivo interactuar con una base de datos para almacenar y manipular información sobre localidades de las provincias de Argentina, y generar archivos CSV separados por provincia.

## Archivos del Sistema

database.py: Este archivo contiene funciones para interactuar con la base de datos. Define la estructura de la tabla localidades, elimina y recrea la tabla en el caso de que la tabla exista, e inserta datos desde un archivo CSV llamado localidades.csv.
main.py: En este archivo se utiliza la función obtener_cursor de database.py para obtener un cursor de la base de datos, se ejecutan consultas SQL para obtener información sobre las localidades agrupadas por provincia, se generan archivos CSV separados para cada provincia, y se cierra la conexión al finalizar.

## Uso del Sistema

Ejecución del Programa: Ejecuta el archivo main.py. Esto iniciará la importación de datos desde el archivo CSV a la base de datos, realizará consultas para agrupar las localidades por provincia y generará archivos CSV separados para cada provincia.

## Requisitos del Sistema

Instalación de la biblioteca mariadb (puedes instalarla mediante 'pip install mariadb')
Instalacion de la biblioteca csv (puedes instalarla mediante 'pip install csv')