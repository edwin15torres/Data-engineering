import pandas as pd
import json
import sqlite3

# Leer el archivo JSON
with open('source/data.json', 'r') as file:
    data = json.load(file)

# Crear un DataFrame a partir del JSON
df = pd.DataFrame(data)

# Conectar a la base de datos SQLite (o crearla si no existe)
conn = sqlite3.connect('database.db')

# Exportar los datos del DataFrame a la tabla 'datos' en la base de datos SQLite
df.to_sql('datos', conn, if_exists='replace', index=False)

# Cerrar la conexión a la base de datos
conn.close()

# Imprimir el tamaño del DataFrame
print(df.shape)
