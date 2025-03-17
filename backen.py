# backen.py
import urequests

API_KEY_TURBIDEZ = "0QOPQV2OY7DOWV4Z"
API_KEY_TEMPERATURA = "5XA1LZK32NVUYFJ2"
API_KEY_PH = "VNCPGPEVBNPNPP8Z"

def turbidez(turbidez):
    url_turbidez = f"https://api.thingspeak.com/update?api_key={API_KEY_TURBIDEZ}&field1={turbidez}"
    try:
        respuesta_turbidez = urequests.get(url_turbidez)
        if respuesta_turbidez.status_code == 200:
            print(f"✅ Datos de turbidez enviados correctamente: {respuesta_turbidez.text}")
        else:
            print(f"⚠️ Error al enviar turbidez: HTTP {respuesta_turbidez.status_code}")
        respuesta_turbidez.close()
    except Exception as e:
        print(f"❌ Error al enviar turbidez: {e}")

def temperatura(temperatura):
    url_temperatura = f"https://api.thingspeak.com/update?api_key={API_KEY_TEMPERATURA}&field1={temperatura}"
    try:
        respuesta_temperatura = urequests.get(url_temperatura)
        if respuesta_temperatura.status_code == 200:
            print(f"✅ Datos de temperatura enviados correctamente: {respuesta_temperatura.text}")
        else:
            print(f"⚠️ Error al enviar temperatura: HTTP {respuesta_temperatura.status_code}")
        respuesta_temperatura.close()
    except Exception as e:
        print(f"❌ Error al enviar temperatura: {e}")

def ph(ph):
    url_ph = f"https://api.thingspeak.com/update?api_key={API_KEY_PH}&field1={ph}"
    try:
        respuesta_ph = urequests.get(url_ph)
        if respuesta_ph.status_code == 200:
            print(f"✅ Datos de pH enviados correctamente: {respuesta_ph.text}")
        else:
            print(f"⚠️ Error al enviar pH: HTTP {respuesta_ph.status_code}")
        respuesta_ph.close()
    except Exception as e:
        print(f"❌ Error al enviar pH: {e}")
