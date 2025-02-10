import socket  # Importar la librería para manejar conexiones de red

# ==================== Configuración del cliente ====================

SERVER_HOST = "localhost"  # Dirección IP del servidor (localhost para pruebas locales)
SERVER_PORT = 60000        # Puerto en el que el servidor está escuchando

# ==================== Creación del socket ====================

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear socket TCP/IP

# ==================== Conexión al servidor ====================

client_socket.connect((SERVER_HOST, SERVER_PORT))  # Intentar conectar con el servidor

# ==================== Envío de mensaje ====================

mensaje = "¡Hola, servidor!"  # Mensaje a enviar
client_socket.sendall(mensaje.encode())  # Enviar el mensaje al servidor codificado en bytes

# ==================== Recepción de respuesta ====================

respuesta = client_socket.recv(1024).decode()  # Recibir la respuesta del servidor (hasta 1024 bytes)
print(f"Servidor responde: {respuesta}")  # Imprimir la respuesta recibida

# ==================== Cierre de conexión ====================

client_socket.close()  # Cerrar la conexión con el servidor
