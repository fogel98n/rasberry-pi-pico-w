import random
import urequests
from machine import ADC, Pin
import time

# Configurar el pin ADC donde está conectado el potenciómetro (por ejemplo, GPIO28 en ESP32)
potenciometro = ADC(Pin(28))

# Configurar la atenuación del ADC para que sea adecuada al rango de voltaje (0-3.3V, 0-1V, etc.)
potenciometro.atten(ADC.ATTN_0DB)  # Puedes ajustarlo según el rango de tu sensor

url = 'https://tilapias360.duckdns.org:3000/turbidez'

def leer_turbidez():
    # Leer el valor del potenciómetro
    lectura = potenciometro.read_u16()  # Método alternativo para leer en un rango de 0 a 65535

    # Calcular un valor de turbidez simulado (puedes reemplazarlo con una lectura real)
    turbidez = round(random.uniform(0, 100), 2)

    # Crear el cuerpo de la solicitud en formato JSON
    data = {'nuevoNumero': turbidez}

    try:
        # Realizar la solicitud POST al servidor
        response = urequests.post(url, json=data)

        # Verificar si la respuesta fue exitosa
        if response.status_code == 200:
            print('Turbidez enviada:', turbidez)
        else:
            print('Error al actualizar la turbidez:', response.status_code)

        # Cerrar la respuesta para liberar recursos
        response.close()

    except Exception as e:
        print("Error al enviar la turbidez:", e)

    return turbidez  # Retornar el valor generado para que lo use otro componente del sistema

# Llamada a la función para leer y enviar una vez
leer_turbidez()


