import socket
import sounddevice as sd

def sender(ip, port):
    CHUNK = 1024
    FORMAT = "int16"
    CHANNELS = 1
    RATE = 44100

    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender_socket.connect((ip, port))
    print("Connected to receiver.")

    def callback(indata, frames, time, status):
        sender_socket.sendall(indata)

    with sd.InputStream(channels=CHANNELS, samplerate=RATE, callback=callback):
        sd.sleep(int(10 * RATE))

if __name__ == "__main__":
    receiver_ip = "172.16.129.14"  # Replace with receiver's IP address
    receiver_port = 12345  # Choose a suitable port
    sender(receiver_ip, receiver_port)
