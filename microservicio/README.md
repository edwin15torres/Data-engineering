# Importando datos de un API con token


## Tiempo Universal Coordinado - UTC

La hora UTC es 5 horas por delante de la hora en Colombia. Dado que la hora proporcionada es 2024-05-18T04:38:16Z, para convertir esto a la hora de Colombia (COT - Colombia Time) que está en UTC-5, restamos 5 horas.

Ejemplo:
- 04:38 UTC - 5 horas = 23:38 (11:38 PM) del 17 de mayo de 2024 en Colombia.

## Docker

1. Construir la imagen:
    $ docker build -t micro_mob . $
2. Construr el contenedor: 
    $ docker run --name micro_mob-app -it -p 5001:5001 -d micro_mob  $
     py application.py --host 0.0.0.0 --port 5000
