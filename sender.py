from CaeserCipher import CaeserCipher
import socket

class Sender:
    def __init__(self):
        self.sender_socket()

    def sender_socket(self):
        host = "127.0.0.1"
        port = 8002

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            enc_msg = self.user_message()
            to_send = bytes(enc_msg, 'utf-8')
            print("Encrypted Message: " +  enc_msg)
            s.sendall(to_send)
            

    def user_message(self):
        msg_string = input("Write the message to send: ")
        my_cipher = CaeserCipher(2)
        encrypted_string = my_cipher.encrypt(msg_string)
        return encrypted_string


Sender()