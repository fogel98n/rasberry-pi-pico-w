# sensor_humedad.py
import random
import urequests

url = 'http://45.56.113.215:3000/actualizarTemperatura'

def leer_temperatura():
    # Simula temperatura en °C
    temperatura = round(random.uniform(15, 35), 2)

    # Crear el cuerpo de la solicitud en formato JSON
    data = {'nuevoNumero': temperatura}

    try:
        # Realizar la solicitud POST al servidor
        response = urequests.post(url, json=data)

        # Verificar si la respuesta fue exitosa
        if response.status_code == 200:
            print('Temperatura enviada:', temperatura)
        else:
            print('Error al actualizar la temperatura:', response.status_code)
        
        response.close()

    except Exception as e:
        print("Error al enviar la temperatura:", e)

    return temperatura  # Retornar el valor generado para que `main.py` lo use