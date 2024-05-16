import pandas as pd
import json

# Leer el archivo JSON
with open('source/data.json', 'r') as file:
    data = json.load(file)

# Crear un DataFrame a partir del JSON
df = pd.DataFrame(data)

# Imprimir el tamaño del DataFrame
print(df.shape)
