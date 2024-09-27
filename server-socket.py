import socket
import threading
import os
import sys

class Servidor():
    def __init__(self, host="localhost", port=7000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        print(f"Servidor escuchando en {host}:{port}")

        while True:
            conn, addr = self.sock.accept()
            print(f"Conexión aceptada de {addr}")
            threading.Thread(target=self.procesar_conexion, args=(conn,)).start()

    def procesar_conexion(self, conn):
        while True:
            try:
                data = conn.recv(1024).decode('utf-8')
                if data:
                    print(f"Comando recibido: {data}")
                    if data == 'lsFiles':
                        self.lsFiles(conn)
                    elif data.startswith('get '):
                        filename = data.split(' ')[1]
                        self.send_file(conn, filename)
                    else:
                        conn.sendall(b"Comando no reconocido.")
            except Exception as e:
                print(f"Error: {e}")
                break
        conn.close()

    def lsFiles(self, conn):
        try:
            files = os.listdir('./Files')
            response = "\n".join(files)
            response = f"FILES:\n{response}\nEND"
            conn.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"Error al listar archivos: {e}")
            conn.sendall(f"Error al listar archivos: {e}".encode('utf-8'))

    def send_file(self, conn, filename):
        try:
            filepath = os.path.join('./Files', filename)
            if os.path.exists(filepath):
                conn.sendall(f"FILE:{filename}\n".encode('utf-8')) 
                conn.sendall(b"COPY IN PROGRESS\n")

                with open(filepath, 'rb') as f:
                    while True:
                        block = f.read(1024)
                        if not block:
                            break
                        conn.sendall(block)
                
                conn.sendall(b"END OF FILE\n")  
            else:
                conn.sendall(b"Archivo no encontrado.")
        except Exception as e:
            conn.sendall(f"Error al enviar archivo: {e}".encode('utf-8'))

server = Servidor()
