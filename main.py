# main.py
from internet import conectarW
import time
import urequests
import random

# Conectar a internet
conectarW()

API_KEY = "F3JXY98XMVNZEU9S"  # Reemplaza con tu clave de API de ThingSpeak

def enviar_dato(valor):
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={valor}"
    try:
        respuesta = urequests.get(url)
        print("Respuesta:", respuesta.text)
        respuesta.close()
    except Exception as e:
        print("Error al enviar:", e)

# Enviar datos aleatorios cada 15 segundos
while True:
    valor = random.randint(10, 100)  # Genera un número aleatorio entre 10 y 100
    print(f"Enviando: {valor}")
    enviar_dato(valor)
    time.sleep(15)  # Espera 15 segundos
