import network
import time
import urequests
from machine import Pin
import onewire, ds18x20

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'fogel'
password = '123456789'
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Conectando...")
    time.sleep(1)

print("Detalles de conexión:", wlan.ifconfig())

API_KEY = "F3JXY98XMVNZEU9S"

pin_ds18b20 = Pin(0)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(pin_ds18b20))
roms = ds_sensor.scan()
print("Dispositivos encontrados:", roms)

led = Pin("LED", Pin.OUT)

def enviar_dato(valor):
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={valor}"
    try:
        led.on()
        respuesta = urequests.get(url)
        print("Respuesta:", respuesta.text)
        respuesta.close()
    except Exception as e:
        print("Error al enviar:", e)
    finally:
        led.off()

def leer_temperatura():
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        print(f"Temperatura: {temp} °C")
        return temp

while True:
    temperatura = leer_temperatura()
    enviar_dato(temperatura)
    time.sleep(15)
