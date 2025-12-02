from socket import *
import time

server_name = "localhost"
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)  # timeout 1 detik

print("Mengirim 10 ping messages...\n")

for i in range(1, 11):
    send_time = time.time()
    message = f"Ping {i} {send_time}"

    try:
        # kirim paket
        client_socket.sendto(message.encode(), (server_name, server_port))

        # tunggu respon
        data, addr = client_socket.recvfrom(1024)
        recv_time = time.time()

        rtt = (recv_time - send_time) * 1000  # ms
        print(f"{data.decode()}  RTT = {rtt:.2f} ms")

    except timeout:
        print(f"Ping {i}   Request timed out")

client_socket.close()
