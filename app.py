import pandas as pd
import requests
from sqlalchemy import create_engine

# URL que contiene los datos JSON
url = 'https://www.datos.gov.co/resource/tukn-wveu.json'

# Realizar la solicitud GET a la URL
response = requests.get(url)
data = response.json()

# Crear un DataFrame a partir del JSON
df = pd.DataFrame(data)

# Datos de conexión a SQL Server
server = 'DESKTOP-US0NNJK'
database = 'temporal'
# username = 'tu_usuario'
# password = 'tu_contraseña'
driver = 'ODBC Driver 17 for SQL Server'

# Crear la cadena de conexión
connection_string = f'mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes'
# connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'

# Crear el engine de SQLAlchemy
engine = create_engine(connection_string)

# Exportar los datos del DataFrame a la tabla 'datos' en la base de datos SQL Server
df.to_sql('tabla', engine, if_exists='replace', index=False)

# Cerrar la conexión al engine
engine.dispose()

# Imprimir el tamaño del DataFrame
print(df)
