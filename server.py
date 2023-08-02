import socket

def start_listener():
    server_ip = 'your_server_ip'
    server_port = your_server_port

    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener_socket.bind((server_ip, server_port))
    listener_socket.listen(1)

    print(f"[*] Đang lắng nghe kết nối từ {server_ip}:{server_port}")

    conn, addr = listener_socket.accept()
    print(f"[+] Đã kết nối với {addr[0]}:{addr[1]}")

    while True:
        command = input(f"{addr[0]}:{addr[1]}$ ")
        if command.strip().lower() == 'exit':
            conn.send(b'exit')
            break
        conn.send(command.encode())

        response = conn.recv(1024).decode(errors='ignore')
        print(response)

    print("[*] Ngắt kết nối.")
    conn.close()
    listener_socket.close()

if __name__ == "__main__":
    start_listener()
