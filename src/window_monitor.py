import threading
import time


class WindowMonitor:
    def __init__(self, page):
        """
        Inicializa el monitor de la ventana.
        """
        self.page = page
        print(self.page.width)
        self.last_width = 50
        self.observers = []  # Lista de observadores (callbacks)
        self.running = True

        # Iniciar el hilo de monitoreo
        threading.Thread(target=self.monitor_window_size, daemon=True).start()

    def monitor_window_size(self):
        """
        Monitorea continuamente el tamaño de la ventana y notifica a los observadores si cambia.
        """
        while self.running:
            if self.page.width != self.last_width:
                self.last_width = self.page.width
                print(f"New window size detected: {self.page.width} px")

                # Notificar a todos los observadores
                for observer in self.observers:
                    observer(self.page.width)

            time.sleep(0.1)  # Verificar cada 100 ms

    def add_observer(self, callback):
        """
        Agrega un observador (callback) para ser notificado cuando cambie el tamaño de la ventana.
        """
        self.observers.append(callback)

    def stop(self):
        """
        Detiene el monitoreo de la ventana.
        """
        self.running = False
