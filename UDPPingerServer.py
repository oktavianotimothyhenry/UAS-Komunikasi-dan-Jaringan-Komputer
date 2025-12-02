from socket import *
import random
import time

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', 12000))

print("UDP Pinger Server berjalan...")

while True:
    # menerima pesan
    message, client_address = server_socket.recvfrom(1024)
    message = message.decode()

    # Simulasi packet loss 30%
    if random.randint(0, 10) < 3:
        print("Simulasi paket hilang, tidak merespon.")
        continue

    # Jika paket tidak hilang, kirim balik pesan (pong)
    server_socket.sendto(message.encode(), client_address)
    print(f"Menerima & mengirim kembali: {message}")
