import pandas as pd
import pytz

def transform(df):

    # Fecha y Hora
    df['time_stamp_event'] = pd.to_datetime(df['time_stamp_event']).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    df['time_stamp_event'] = pd.to_datetime(df['time_stamp_event'], format='%Y-%m-%dT%H:%M:%SZ', utc=True)
    colombia_tz = pytz.timezone('America/Bogota')
    df['time_stamp_event_colombia'] = df['time_stamp_event'].dt.tz_convert(colombia_tz)
    df['fecha'] = df['time_stamp_event_colombia'].dt.strftime('%Y-%m-%d')
    df['hora'] = df['time_stamp_event_colombia'].dt.strftime('%H:%M:%S')
    df = df.drop(columns=['time_stamp_event','time_stamp_event', 'location'])
    
    # latitude  & longitude
    df['latitude'] = df['latitude'].astype(str).str.replace('.', ',', regex=False)
    df['longitude'] = df['longitude'].astype(str).str.replace('.', ',', regex=False)

        # Consultar al servidor
    df0 = pd.read_csv('persistencia/table_movilidad.csv', sep=';', na_values=['NULL', 'NA'], keep_default_na=False, on_bad_lines='skip')
    
    # id
    if df0.empty or 'Id' not in df0.columns:
        last_id = 0
    else:
        last_id = max(df0['Id'], default=0)  # Obtener el máximo ID existente

    # Generar nuevos registros
    df_concat = pd.concat([df0, df], ignore_index=True)
    df_concat.drop_duplicates(subset=['plate', 'fecha', 'hora', 'latitude', 'longitude','angle', 'speed', 'odometer'], inplace=True)

    # Generar nuevos IDs
    new_ids = range(last_id + 1, last_id + 1 + len(df_concat))
    df_concat['Id'] = new_ids
    
     # Select
    df_concat = df_concat.loc[:, ['Id', 'plate', 'fecha','hora', 'latitude', 'longitude', 'angle', 'speed', 'odometer']]

    # Guardar en el archivo CSV
    df_concat.to_csv('persistencia/table_movilidad.csv', index=False, sep=';', header=False, mode='a')

    print(df_concat.shape[0])

