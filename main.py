import time
from internet import conectarW
from backen import turbidez, temperatura, ph
from turbidez import leer_turbidez
from datos_humedad import leer_temperatura
from ph import leer_ph

# Conexión a la red
conectarW()

while True:
    try:
        # Obtener los valores de los sensores
        valor_turbidez = leer_turbidez()
        valor_temperatura = leer_temperatura()
        valor_ph = leer_ph()
        
        # Verificar que los valores son válidos
        if None in (valor_turbidez, valor_temperatura, valor_ph):
            print("❌ Error: uno o más valores del sensor no son válidos")
        else:
            print(f"Turbidez: {valor_turbidez} NTU | Temperatura: {valor_temperatura}°C | pH: {valor_ph}")
            
            # Enviar los datos a ThingSpeak
            turbidez(valor_turbidez)
            temperatura(valor_temperatura)
            ph(valor_ph)
    
    except Exception as e:
        print("Error en el bucle principal:", e)
    
    time.sleep(5)
