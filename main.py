#modulos
from internet import conectarW
from backen import enviar_dato

#dependencias
import time
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
