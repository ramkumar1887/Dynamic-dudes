import socket
import sounddevice as sd
import numpy as np

def receiver(port):
    CHUNK = 1024
    FORMAT = "int16"
    CHANNELS = 1
    RATE = 44100

    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver_socket.bind(("", port))
    receiver_socket.listen(1)
    print("Waiting for sender to connect...")
    sender_socket, sender_address = receiver_socket.accept()
    print(f"Connected with sender: {sender_address}")

    def callback(outdata, frames, time, status):
        data = sender_socket.recv(CHUNK)
        outdata[:] = np.frombuffer(data, dtype=np.int16)

    with sd.OutputStream(channels=CHANNELS, samplerate=RATE, callback=callback):
        sd.sleep(int(10 * RATE))

if __name__ == "__main__":
    receiver_port = 12345  # Choose the same port as in sender
    receiver(receiver_port)
