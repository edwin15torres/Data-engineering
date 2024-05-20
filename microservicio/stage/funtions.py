import pandas as pd

def csv_to_dict(file_path: str) -> dict:
    try:
        # Importar el archivo CSV como DataFrame
        df = pd.read_csv(file_path, sep= ';')
        
        # Convertir el DataFrame a un diccionario
        data_dict = df.to_dict(orient='records')
        
        return data_dict
    except Exception as e:
        print("Error al convertir el archivo CSV a un diccionario:", e)
        return None