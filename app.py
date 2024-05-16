import pandas as pd
import requests
import sqlite3

# URL que contiene los datos JSON
url = 'https://www.datos.gov.co/resource/tukn-wveu.json'

# Realizar la solicitud GET a la URL
response = requests.get(url)
data = response.json()

# Crear un DataFrame a partir del JSON
df = pd.DataFrame(data)

# Conectar a la base de datos SQLite (o crearla si no existe)
conn = sqlite3.connect('database.db')

# Exportar los datos del DataFrame a la tabla 'datos' en la base de datos SQLite
df.to_sql('datos', conn, if_exists='replace', index=False)

# Cerrar la conexión a la base de datos
conn.close()

# Imprimir el tamaño del DataFrame
print(df)
