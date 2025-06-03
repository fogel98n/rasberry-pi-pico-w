import wifi
from firebase import Firebase
from semaforo import Semaforo

FIREBASE_URL_BASE = "https://raspberry-pi-pico-w-5635e-default-rtdb.firebaseio.com/"

def main():
    if wifi.conectar_wifi():
        sem = Semaforo()
        fb = Firebase(FIREBASE_URL_BASE)
        print("Iniciando ciclo del semáforo...")
        while True:
            sem.ciclo(firebase=fb)
    else:
        print("No se pudo conectar a WiFi. Terminando programa.")

if __name__ == "__main__":
    main()
