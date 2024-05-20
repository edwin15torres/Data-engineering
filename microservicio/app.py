import requests
import json
import pandas as pd
import time
from stage.stage import transform
from stage.funtions import csv_to_dict
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)

file_path = 'persistencia/table_movilidad.csv'  #   # 
table_movilidad = csv_to_dict(file_path)
# table_movilidad = csv_to_dict('persistencia/table_movilidad.csv')

def persistir():
    global table_movilidad  # Declarar table_movilidad como global

    with open('url.json', 'r') as file:
        setup_url = json.load(file)
    
    url = setup_url.get('url')
    token = setup_url.get('token')    

    while True:
        try:
            response = requests.get(url, headers={'X-API-Key': token})
            
            if response.status_code == 200 and response.text:
                data = response.json()
                df = pd.DataFrame(data['result'])
                df = transform(df)
        
            else:
                print("La solicitud a la API no fue exitosa o la respuesta está vacía.")
                print("Código de estado de la respuesta:", response.status_code)
                print("Contenido de la respuesta:", response.text)

        except Exception as e:
            print("Ocurrió un error:", e)

        time.sleep(10)
        table_movilidad = csv_to_dict(file_path)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(table_movilidad)

if __name__ == "__main__":
    
    thread = Thread(target=persistir)
    thread.daemon = True
    thread.start()

    app.run(host='0.0.0.0', port=5001)
