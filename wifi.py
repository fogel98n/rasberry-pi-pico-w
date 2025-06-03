import network
import time

_redes_wifi = {
    'fogel': '123456789',
}

def agregar_red(ssid, password):
    """
    Agrega una red WiFi al diccionario interno.
    """
    _redes_wifi[ssid] = password
    print(f"Red '{ssid}' agregada.")

def conectar_wifi(intentos=15):
    """
    Intenta conectar a las redes almacenadas en _redes_wifi.
    Retorna True si se conecta, False si falla.
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not _redes_wifi:
        print("No hay redes WiFi para conectar. Usa agregar_red(ssid, password).")
        return False

    for ssid, password in _redes_wifi.items():
        print(f"Intentando conectar a '{ssid}'...")
        wlan.connect(ssid, password)

        for _ in range(intentos):
            if wlan.isconnected():
                print(f"Conectado a {ssid}")
                print("IP:", wlan.ifconfig()[0])
                return True
            time.sleep(1)

        print(f"No se pudo conectar a {ssid}")

    print("No se pudo conectar a ninguna red.")
    return False
