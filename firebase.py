import urequests
import json

class Firebase:
    def __init__(self, url_base):
        self.url_base = url_base.rstrip('/')

    def enviar_estado(self, estado, duracion):
        url = f"{self.url_base}/semaforo.json"
        data = {
            "estado": estado,
            "duracion": duracion
        }
        try:
            headers = {'Content-Type': 'application/json'}
            data_json = json.dumps(data)
            response = urequests.put(url, data=data_json, headers=headers)
            if response.status_code == 200:
                print("Datos enviados con éxito:", data)
            else:
                print(f"Error HTTP {response.status_code} al enviar estado.")
            response.close()
        except Exception as e:
            print("Error al enviar datos a Firebase:", e)
