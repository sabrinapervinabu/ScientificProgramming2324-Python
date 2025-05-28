#host= localhost 
#port= 6000

import socket
import sys

def send_request(host, port, message):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host, port))
    client.sendall (message.encode())
    response = client.recv(100000).decode()
    client.close()
    return response

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python client.py <host> <port> <mode> <sequence>")
        print("Mode: 'BWT' to compute BWT, 'REV' to reverse BWT.")
        print("Sequence: insert it using single quotes '' around it, when mode==REV.")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    mode = sys.argv[3]
    sequence = sys.argv[4]
    if mode not in ["BWT", "REV"]:
        print("Invalid mode. Use 'BWT' to compute BWT or 'REV' to reverse BWT.")
        sys.exit(1)
    if mode == "REV" and '$' not in sequence and not(sequence.startswith("'") and sequence.endswith("'")):
        print("Invalid sequence: BWT sequence must have single quotes '' around it, and it must contain the '$' end-of-string marker")
        sys.exit(1)
    message = f"{mode}:{sequence}"
    response = send_request(host, port, message)  
    print(f"Response: {response}")
    