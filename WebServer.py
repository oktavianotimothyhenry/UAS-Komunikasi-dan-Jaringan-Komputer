from socket import *

# Membuat server socket
server_socket = socket(AF_INET, SOCK_STREAM)

# Bind server ke port (gunakan port berbeda jika 80 dipakai)
server_port = 8080
server_socket.bind(('', server_port))

# Mendengarkan koneksi
server_socket.listen(1)
print(f"Web server berjalan di port {server_port} ...")

while True:
    print("Menunggu request...")
    connection_socket, addr = server_socket.accept()
    print(f"Koneksi dari: {addr}")

    try:
        # Menerima HTTP request
        message = connection_socket.recv(1024).decode()
        print("Request diterima:")
        print(message)

        # Parsing nama file yang diminta
        filename = message.split()[1][1:]  # hapus '/'
        print(f"File diminta: {filename}")

        # Membaca file
        with open(filename, 'rb') as f:
            output_data = f.read()

        # Mengirim HTTP Header
        header = "HTTP/1.1 200 OK\r\n\r\n"
        connection_socket.send(header.encode())

        # Mengirim isi file
        connection_socket.send(output_data)
        print("File berhasil dikirim.")

    except FileNotFoundError:
        # Response 404
        header = "HTTP/1.1 404 Not Found\r\n\r\n"
        body = "<html><body><h1>404 File Not Found</h1></body></html>"
        connection_socket.send(header.encode())
        connection_socket.send(body.encode())
        print("File tidak ditemukan, mengirim 404.")

    connection_socket.close()
    print("Koneksi ditutup.\n")
    break  # hanya memproses satu request
