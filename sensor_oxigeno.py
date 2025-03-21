import urequests
from machine import ADC, Pin
import time

# Configurar el pin ADC donde está conectado el potenciómetro (por ejemplo, GPIO26 en ESP32)
potenciometro = ADC(Pin(26))  # Pin 26 en el ESP32

# Configurar el ADC para leer en el rango de 10 bits (0-1023)
potenciometro.width(ADC.WIDTH_10BIT)  # Esto asegura que el rango es de 0-1023
potenciometro.atten(ADC.ATTN_0DB)     # Esto establece la atenuación para un rango de 0-3.3V

# URL del servidor
url = 'https://tilapias360.duckdns.org:3000/actualizarOxigeno'

def leer_oxigeno():
    # Leer el valor del potenciómetro (0-1023)
    valor_adc = potenciometro.read()

    # Mapear el valor ADC a un rango de 0 a 100 (simulando porcentaje de oxígeno)
    oxigeno = round((valor_adc / 1023.0) * 100, 2)

    # Crear los datos en formato JSON
    data = {'nuevoNumero': oxigeno}
    
    try:
        # Realizar la solicitud POST al servidor
        response = urequests.post(url, json=data)

        # Verificar si la respuesta fue exitosa
        if response.status_code == 200:
            print('Oxígeno enviado:', oxigeno)
        else:
            print('Error al actualizar el oxígeno:', response.status_code)

        # Cerrar la respuesta para liberar recursos
        response.close()

    except Exception as e:
        print("Error al enviar el oxígeno:", e)

    return oxigeno  # Devolver el valor de oxígeno

# Llamar a la función para leer y enviar una vez
leer_oxigeno()

