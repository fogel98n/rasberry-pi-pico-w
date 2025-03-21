import random
import urequests
from machine import ADC, Pin
import time

# Configurar el pin ADC donde está conectado el potenciómetro (por ejemplo, GPIO27 en ESP32)
potenciometro = ADC(Pin(27))
potenciometro.width(ADC.WIDTH_10BIT)  # Esto asegura que el rango es de 0-1023
potenciometro.atten(ADC.ATTN_0DB)  # Rango de 0-1V

url = 'https://tilapias360.duckdns.org:3000/actualizarPH'

def leer_ph():
    # Simula el pH en nodos, generando un valor aleatorio entre 4.0 y 9.0
    ph = round(random.uniform(4.0, 9.0), 2)

    # Crear el cuerpo de la solicitud en formato JSON
    data = {'nuevoNumero': ph}

    try:
        # Realizar la solicitud POST al servidor
        response = urequests.post(url, json=data)

        # Verificar si la respuesta fue exitosa
        if response.status_code == 200:
            print("pH enviado:", ph)
        else:
            print("Error al actualizar el pH:", response.status_code)

        # Cerrar la respuesta para liberar recursos
        response.close()

    except Exception as e:
        print("Error al enviar el pH:", e)

    return ph  # Retornar el valor de pH

# Llamar a la función para leer y enviar una vez
leer_ph()
