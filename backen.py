import urequests  # Si usas Python normal, cambia a `import requests`

def enviar_dato(valor):
    API_KEY = "F3JXY98XMVNZEU9S" 
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={valor}"
    
    try:
        respuesta = urequests.get(url)  
        if respuesta.status_code == 200:
            print("Datos enviados correctamente:", respuesta.text)
        else:
            print(f"Error HTTP {respuesta.status_code}: {respuesta.text}")
        respuesta.close()
    except Exception as e:
        print("Error al enviar datos:", e)
