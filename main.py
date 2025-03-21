# main.py

import time
from internet import conectarW

# mis sensores
from sensor_turbidez import leer_turbidez
from sensor_humedad import leer_temperatura
from sensor_ph import leer_ph
from sensor_oxigeno import leer_oxigeno


# Conexión a la red
conectarW()

while True:
    try:
        # Obtener los valores de los sensores
        turbidez = leer_turbidez()
        temperatura = leer_temperatura()
        ph = leer_ph()
        oxigeno=leer_oxigeno()        
        # Imprimir valores
        print(f"Turbidez: {turbidez}, Temperatura: {temperatura}, pH: {ph}")
    
    except Exception as e:
        print("Error en el bucle principal:", e)
    
    time.sleep(5)

