from internet import conectarW
from backen import enviar_dato
import time
import urequests  # Asegúrate de que esté instalado en tu entorno
import random

# Conectar a internet
conectarW()

while True:
    try:
        valor = random.randint(10, 100)  
        print(f"Enviando: {valor}")
        enviar_dato(valor)
    except Exception as e:
        print("Error en el bucle principal:", e)
    
    time.sleep(15)  # Espera 15 segundos
