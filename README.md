# Servidor y Cliente de Socket

Este programa implementa un servidor y un cliente de socket en Python que permite a los clientes ejecutar comandos para listar archivos y descargar archivos desde un directorio específico en el servidor. El servidor responde a los comandos del cliente y maneja la transferencia de archivos en bloques, proporcionando mensajes de progreso durante la transferencia.

## Funcionalidades

- **Listar Archivos**: Los clientes pueden enviar el comando `lsFiles` para obtener un listado de los archivos disponibles en el directorio `Files` del servidor.
- **Descargar Archivos**: Los clientes pueden solicitar la descarga de archivos mediante el comando `get archivo.txt`. El servidor enviará el archivo en bloques y notificará sobre el progreso de la copia.
- **Notificaciones de Progreso**: El cliente y el servidor muestran mensajes para indicar que se están copiando archivos y notificar la finalización de la transferencia.

## Requisitos

- Python 3.x
- Bibliotecas estándar de Python (no se requieren instalaciones adicionales)

## Instrucciones para Ejecutar

### Paso 1: Configurar el Directorio de Archivos

1. Crea un directorio llamado `Files` en la misma ubicación donde se encuentran los scripts `server-socket.py` y `client-socket.py`.
2. Coloca algunos archivos en el directorio `Files` para probar la funcionalidad.

### Paso 2: Iniciar el Servidor

Abre una terminal y ejecuta el servidor con el siguiente comando:

```bash
python3 server-socket.py

### Paso 3: Iniciar el Cliente

Abre otra terminal y ejecuta el cliente con el siguiente comando:

```bash
python3 client-socket.py

### Paso 4: Usar el Cliente
En la terminal del cliente, puedes ingresar los siguientes comandos:

lsFiles: Listar los archivos disponibles en el servidor.
get archivo.txt: Descargar un archivo específico (reemplaza archivo.txt con el nombre del archivo que deseas descargar).
salir: Cerrar el cliente.

## Autor
Este programa fue desarrollado por Andrés Manuel Hernández Talamantes