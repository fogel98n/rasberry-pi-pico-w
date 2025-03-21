#sensor_temperatura.py
import random
import urequests

url = 'https://tilapias360.duckdns.org:3000/actualizarHumedad'
def leer_humedad():
    humedad=round(random.uniform(0, 100), 2)

    data= {'nuevoNumero':humedad}
    try:
        # Realizar la solicitud POST al servidor
        response = urequests.post(url, json=data)

        # Verificar si la respuesta fue exitosa
        if response.status_code == 200:
            print('humedad enviada:', humedad)
        else:
            print('Error al actualizar la humedad:', response.status_code)
        
        response.close()

    except Exception as e:
        print("Error al enviar la humedad:", e)

    return humedad  # Retornar el valor generado para que `main.py` lo use
