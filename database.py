import csv
import mariadb

archivo_csv = 'localidades.csv'

# Funcion para retornar cursor
def obtener_cursor():
    try:
        connection = mariadb.connect(
            host="localhost",
            user="root",
            password="",
            database="localidadesdb"
        )

        cursor = connection.cursor()

        # Eliminar tabla de la base de datos (si existe)
        cursor.execute("DROP TABLE IF EXISTS localidades")

        # Crear la tabla
        cursor.execute("CREATE TABLE localidades (provincia VARCHAR(25), id INT, localidad VARCHAR(25), cp INT, id_prov_mstr INT)")

        # Abrir el archivo CSV en modo lectura
        with open(archivo_csv, mode='r', newline='') as archivo:
            lector_csv = csv.reader(archivo)
            # Saltar la primera fila si contiene encabezados
            next(lector_csv, None)
            # Interar sobre las filas del archivo CSV
            for fila in lector_csv:
                # Consulta de insercion
                cursor.execute("INSERT INTO localidades (provincia, id, localidad, cp, id_prov_mstr) VALUES (%s, %s, %s, %s, %s)", fila)

        # Confirmar los cambios
        connection.commit()

        print("Interacción exitosa con la Base de Datos!!")

        return cursor
    
    except mariadb.Error as error:
        print("Error: ", error)