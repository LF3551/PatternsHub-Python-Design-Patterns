import socket
import threading

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []  # List to store peers' addresses
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        threading.Thread(target=self.listen_for_incoming_connections).start()

    def listen_for_incoming_connections(self):
        self.sock.listen(5)
        while True:
            client, addr = self.sock.accept()
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        while True:
            try:
                data = client.recv(1024)
                if not data:
                    break
                print(f"Received message: {data.decode('utf-8')}")
            except:
                client.close()
                return

    def connect_to_peer(self, host, port):
        peer = (host, port)
        if peer not in self.peers:
            self.peers.append(peer)
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_sock.connect(peer)
            print(f"Connected to {host}:{port}")
            return client_sock

    def send_message(self, message, host, port):
        client_sock = self.connect_to_peer(host, port)
        if client_sock:
            client_sock.sendall(message.encode('utf-8'))
            client_sock.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python peer.py [HOST] [PORT]")
        sys.exit(1)
    peer = Peer(sys.argv[1], int(sys.argv[2]))
