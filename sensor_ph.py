#sensor_ph.py
import random
import urequests

url = 'https://tilapias360.duckdns.org:3000/actualizarPH'

def leer_ph():
    #simula el ph en nodos
    ph round(random.uniform(4.0, 9.0), 2)

    #crear el cuerpo de la solicitud en formato JSON
   data = {'nuevoNumero': ph}

   try:
    response=urequests.post(url,json=data)

    if response.status_code==200:
        print("ph enviado:",ph)
    else:
        print("error al actualizar la temperratura:",response.status_code)
    response.close()        

    except Exception as e:
        print("error al enviar ph:",e)

return ph