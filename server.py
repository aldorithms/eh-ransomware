import socketserver

class ClientHandler(socketserver.BaseRequestHandler):
    
    # Function to decrypt symmetric key and send back to client.
    def handle(self):
        encrypted_key = self.request.recv(1024).strip()
        print("Implement decryption of data " + encrypted_key)
        #
        #
        #
        self.request.sendall("send key back")

if __name__ == "__main__":
    HOST, PORT = "", 8000

    # Create new instance of the TCP Server
    tcpServer = socketserver.TCPServer((HOST, PORT), ClientHandler)
    try:
        # Start TCP Server
        tcpServer.serve_forever()
    except:
        print("There was an error")