import csv
import mariadb
from database import obtener_cursor

try:
    # Obtener el cursor
    cursor = obtener_cursor()

    # Consulta SQL para agrupar las localidades por provinecias
    cursor.execute("SELECT provincia, COUNT(*) AS cant_localidades FROM localidades GROUP BY provincia")

    # Obtener los resultados
    resultados = cursor.fetchall()

    # Interar sobre cada provincia
    for provincia, cant_localidades in resultados:
        # Consulta para obtener todas las localidades de cada provincia
        cursor.execute(" SELECT * FROM localidades WHERE provincia = %s", (provincia,))
        localidades = cursor.fetchall()

        # Indicar nombre del archivo CSV para cada provincia
        nombre_archivo = f"{provincia}.csv"

        # Escribir los resultados en el archivo CSV
        with open(nombre_archivo, mode='w', newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            # Escribir el encabezado
            escritor.writerow(['provincia', 'id', 'localidad', 'cp', 'id_prov_mstr'])
            # Escribir las filas de localidades
            for localidad in localidades:
                escritor.writerow(localidad)

        print(f"Archivo CSV para {provincia} creado exitosamente.")

except (Exception, mariadb.Error) as error:
    print("Error al Ejecutar la consulta: ", error)

finally:
    # Cerrar la conexion
    if 'cursor' in locals():
        cursor.close()
        print("Conexion cerrada.")