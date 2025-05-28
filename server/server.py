#host= localhost 
#port= 6000

import socket
import sys
from threading import Thread

def suffix_array(s): 
    return [i for (_, i) in sorted((s[i:], i) for i in range(len(s)))]

def bwt_transform(seq):
    seq = seq + '$'
    return ''.join(seq[i-1] for i in suffix_array(seq))

def rank_bwt(bwt):
    counts = {}
    ranks = []
    for char in bwt:
        if char not in counts:
            counts[char] = 0
        ranks.append(counts[char])
        counts[char] += 1
    return ranks, counts

def first_column(counts):
    first = {}
    total = 0
    for char, count in sorted(counts.items()):
        first[char] = (total, total + count)
        total += count
    return first

def reverse_bwt(bwt):
    ranks, counts = rank_bwt(bwt)
    first = first_column(counts)
    index = bwt.index('$')
    original = []
    while True:
        char = bwt[index]
        if char == '$' and len(original) > 0:  
            break
        original.append(char)
        index = first[char][0] + ranks[index]
    return ''.join(reversed(original))

def start_server(host, port):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host, port)) 
    server.listen(5) 
    print(f"[*] Listening on {host}:{port}")
    while True:
        client_socket, addr = server.accept()  
        print(f"[*]Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = Thread(target=handle_client_connection, args=(client_socket,))     
        client_handler.start()

def handle_client_connection(client_socket):
    request = client_socket.recv(100000).decode() 
    print(f"[*] Received: {request}")
    if request.startswith("BWT:"):
        sequence = request[4:]
        response = bwt_transform(sequence)
    elif request.startswith("REV:"):
        bwt_sequence = request[4:]
        response = reverse_bwt(bwt_sequence)
    else:
        response = "Invalid request"
    print(f"[*] Sending response: {response}")
    client_socket.sendall(response.encode()) 
    client_socket.close() 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python server.py <host> <port>")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    start_server(host, port)
    