import socket
import pickle
import threading

def handle_client(client_socket, task_queue):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            task = pickle.loads(data)
            # Process the task and send the result back to the client
            result = process_task(task)
            client_socket.send(pickle.dumps(result))
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()

def process_task(task):
    # Implement task processing logic here
    return f"Task processed: {task}"

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)

    print("Server listening on port 9999")

    task_queue = []

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, task_queue))
        client_handler.start()

if __name__ == "__main__":
    main()
