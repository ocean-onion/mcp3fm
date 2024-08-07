import socket

def check_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex(('localhost', port))
        if result == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    port = 5000
    if check_port_in_use(port):
        print(f"Port {port} is in use.")
    else:
        print(f"Port {port} is available.")
