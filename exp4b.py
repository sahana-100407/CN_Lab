import socket
def echo_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    try:
        while True:
            message = input("Enter a message: ")
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Echoed from server: {data.decode()}")
            if message.lower() == 'exit':
                break
    finally:
        client_socket.close()
if __name__ == '__main__':
    echo_client()