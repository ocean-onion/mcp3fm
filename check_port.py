import socket

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if __name__ == "__main__":
    port = 5001
    if check_port(port):
        print(f"Port {port} is in use")
    else:
        print(f"Port {port} is free")

