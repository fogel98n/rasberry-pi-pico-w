#sensor_oxigeno.py
import random
import urequests

url = 'https://tilapias360.duckdns.org:3000/actualizarOxigeno'

def leer_oxigeno():
    oxigeno=round(random.uniform(0, 100), 2)

    data= {'nuevoNumero':oxigeno}
    try:
        # Realizar la solicitud POST al servidor
        response = urequests.post(url, json=data)

        # Verificar si la respuesta fue exitosa
        if response.status_code == 200:
            print('oxigeno enviado:', oxigeno)
        else:
            print('Error al actualizar el oxigeno:', response.status_code)
        
        response.close()

    except Exception as e:
        print("Error al enviar el oxigeno:", e)

    return oxigeno  # Retornar el valor generado para que `main.py` lo use
