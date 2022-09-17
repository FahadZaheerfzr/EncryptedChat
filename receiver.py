from CaeserCipher import CaeserCipher
import socket

class Receiver:

    def __init__(self):
        self.receiver_socket()

    def receiver_socket(self):
        host = "127.0.0.1"
        port = 8002

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host,port))
            s.listen()
            print("Listening for connections")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    my_cipher = CaeserCipher(2)
                    new_data = data.decode("utf-8") 
                    print("Message Received: " + new_data)
                    new_data = my_cipher.decrypt(new_data)
                    print("Decrypted Message: " +new_data)


Receiver()