from machine import Pin
import time

class Semaforo:
    def __init__(self):
        self.led_rojo = Pin(8, Pin.OUT)
        self.led_amarillo = Pin(10, Pin.OUT)
        self.led_verde = Pin(9, Pin.OUT)

    def apagar_todos(self):
        self.led_rojo.value(0)
        self.led_amarillo.value(0)
        self.led_verde.value(0)

    def ciclo(self, firebase=None):
        # Rojo
        self.apagar_todos()
        self.led_rojo.value(1)
        if firebase:
            firebase.enviar_estado("rojo", 2)
        time.sleep(2)

        # Verde
        self.apagar_todos()
        self.led_verde.value(1)
        if firebase:
            firebase.enviar_estado("amarillo", 2)
        time.sleep(2)

        # Amarillo
        self.apagar_todos()
        self.led_amarillo.value(1)
        if firebase:
            firebase.enviar_estado("verde", 2)
        time.sleep(2)
