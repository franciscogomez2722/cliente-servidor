import socket  # Importar la librería para manejar conexiones de red

# ==================== Configuración del servidor ====================

HOST = "0.0.0.0"  # Escucha en todas las interfaces de red disponibles
PORT = 60000      # Puerto en el que el servidor estará escuchando conexiones

# ==================== Creación del socket ====================

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear socket TCP/IP
server_socket.bind((HOST, PORT))  # Asociar el socket al host y puerto
server_socket.listen(5)  # Habilitar el servidor para aceptar conexiones (hasta 5 en espera)

print(f"Servidor escuchando en {HOST}:{PORT}...")

# ==================== Manejo de conexiones entrantes ====================

while True:
    # Aceptar conexión de un cliente
    client_socket, client_address = server_socket.accept()
    print(f"Cliente conectado desde {client_address}")

    # ==================== Recepción de datos ====================
    mensaje = client_socket.recv(1024).decode()  # Recibir mensaje del cliente (máximo 1024 bytes)
    print(f"Cliente dice: {mensaje}")

    # ==================== Envío de respuesta ====================
    client_socket.sendall("¡Mensaje recibido!".encode())  # Responder al cliente

    # ==================== Cierre de conexión ====================
    client_socket.close()  # Cerrar la conexión con el cliente
