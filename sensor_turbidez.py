#sensor_turbidez.py
import random
import urequests

url = 'https://tilapias360.duckdns.org:3000/actualizarTurbidez'
def leer_turbidez():
    turbidez=round(random.uniform(0, 100), 2)

    data= {'nuevoNumero':turbidez}
    try:
        # Realizar la solicitud POST al servidor
        response = urequests.post(url, json=data)

        # Verificar si la respuesta fue exitosa
        if response.status_code == 200:
            print('Turbidez enviada:', turbidez)
        else:
            print('Error al actualizar la turbidez:', response.status_code)
        
        response.close()

    except Exception as e:
        print("Error al enviar la turbidez:", e)

    return turbidez  # Retornar el valor generado para que `main.py` lo use
