# internet.py
import network
import time

def conectarW():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)  # Activa la interfaz Wi-Fi

    ssid = 'fogel'  # Reemplaza con el nombre de tu red Wi-Fi
    password = '123456789'  # Reemplaza con la contraseña
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        print("Conectando...")
        time.sleep(1)

    print("Detalles de conexión:", wlan.ifconfig())
