# Azure4Everyone-Databricks-Intro


Para convertir el código que usa pandas y requests para obtener datos JSON desde una API a un código que use Apache Spark, puedes seguir estos pasos. Utilizaremos PySpark, que es la API de Python para Spark. Primero, necesitaremos usar el módulo requests para obtener los datos JSON y luego cargar estos datos en un DataFrame de Spark.

Aquí está el código actualizado:

Configuración de Spark
Asegúrate de tener PySpark instalado. Puedes instalarlo usando pip install pyspark.

Código para obtener datos JSON y cargarlos en Spark
python
Copiar código
import requests
from pyspark.sql import SparkSession
import json

# Inicializar una sesión de Spark
spark = SparkSession.builder \
    .appName("API to Spark DataFrame") \
    .getOrCreate()

# URL que contiene los datos JSON
url = 'https://api.football-data.org/v2/competitions/2000/teams'
token = '9947b1e60e2a4d37b26ceb23fa3179e3'
headers = {
    'X-Auth-Token': token
}

try:
    # Realizar la solicitud GET a la URL con el token de autenticación
    response = requests.get(url, headers=headers)
    
    # Verificar si la solicitud fue exitosa y tiene contenido
    if response.status_code == 200 and response.text:
        data = response.json()
        
        # Imprime los datos obtenidos de la API
        print(data)
        
        # Convertir los datos JSON a un DataFrame de Spark
        # Para esto, primero convertimos el JSON a un string
        json_data = json.dumps(data['teams'])  # Asumiendo que 'teams' es la clave que contiene los datos relevantes
        
        # Crear un DataFrame de Spark a partir del string JSON
        df = spark.read.json(spark.sparkContext.parallelize([json_data]))
        
        # Mostrar el esquema del DataFrame
        df.printSchema()
        
        # Mostrar algunas filas del DataFrame
        df.show()
        
        # Continuar con el procesamiento de los datos...
        
    else:
        print("La solicitud a la API no fue exitosa o la respuesta está vacía.")
        print("Código de estado de la respuesta:", response.status_code)
        print("Contenido de la respuesta:", response.text)

except Exception as e:
    print("Ocurrió un error:", e)
Explicación
Inicializar SparkSession: Esto es necesario para trabajar con Spark.
Solicitud GET a la API: Se utiliza la biblioteca requests para realizar la solicitud a la API con el token de autenticación.
Verificar respuesta: Se verifica si la solicitud fue exitosa y tiene contenido.
Convertir JSON a String: Los datos JSON se convierten a una cadena de texto.
Crear un DataFrame de Spark: Usamos spark.read.json y sparkContext.parallelize para convertir la cadena JSON a un DataFrame de Spark.
Mostrar esquema y datos: Se imprimen el esquema y algunas filas del DataFrame para verificar que los datos se hayan cargado correctamente.