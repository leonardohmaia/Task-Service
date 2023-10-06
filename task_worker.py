import socket
import pickle

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))

    while True:
        task = input("Enter a task: ")
        client.send(pickle.dumps(task))
        result = client.recv(1024)
        print(pickle.loads(result))

if __name__ == "__main__":
    main()
