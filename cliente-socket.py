import socket
import threading
import os
import sys

class Cliente():
    def __init__(self, host="localhost", port=7000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))
        threading.Thread(target=self.msg_recv, daemon=True).start()
        self.run()

    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1028)
                if data:
                    self.handle_data(data)
            except Exception as e:
                print(f"Error en la recepción: {e}")
                break

    def handle_data(self, data):
        data = data.decode('utf-8', errors='ignore')  # Evitar errores de decodificación
        if data.startswith("FILES:"):
            files = data[len("FILES:"):].strip().split("\n")
            for file in files:
                print(file)
        elif data.startswith("FILE:"):
            filename = data[len("FILE:"):].strip()
            print(f"Recibiendo archivo: {filename}")
            self.receive_file(filename)
        elif "COPY IN PROGRESS" in data:
            print("Copiando archivo...")
        elif "END OF FILE" in data:
            print("Transferencia de archivo completada.")
        else:
            print(data)

    def run(self):
        while True:
            msg = input('cliente> ')
            if msg.lower() == 'salir':
                self.sock.close()
                sys.exit()
            else:
                self.send_msg(msg)

    def send_msg(self, msg):
        try:
            self.sock.send(msg.encode('utf-8'))
        except Exception as e:
            print(f"Error al enviar: {e}")

    def receive_file(self, filename):
        os.makedirs('download', exist_ok=True)
        filepath = os.path.join('download', filename)

        with open(filepath, 'wb') as f:
            total_received = 0
            while True:
                data = self.sock.recv(1024)
                if data.startswith(b"END OF FILE"):  # Termina la recepción del archivo
                    print(f"Archivo {filename} guardado en la carpeta 'download'.")
                    break
                elif b"COPY IN PROGRESS" in data:
                    print("Copiando archivo...")
                else:
                    f.write(data)  # Escribir los bloques en el archivo
                    total_received += len(data)
                    print(f"Recibiendo: {total_received} bytes")

cliente = Cliente()
