# 🖧 Python Client-Server Socket Application

This repository contains a basic implementation of a client-server communication model using Python sockets.

The server listens for incoming connections and the client sends messages. The project demonstrates fundamental concepts of network programming with `socket`.

---

## Project Structure

- `server.py` – Starts a socket server that listens on a configurable IP and port, accepts client connections, and handles communication.
- `client.py` – Connects to the server, sends a message, and receives a response.

---

##  How to Run

### Requirements

This project only requires the Python standard library. Tested with **Python 3.8+**.

### 1. Start the Server
In one terminal window:

```bash
python server.py
```
### 2. Run the Client
In another terminal window:
```bash
python client.py
```
The client will connect to the server and exchange messages.

### Customization
You can change the IP and port in both files:
- In server.py:
```bash
bind_ip = "127.0.0.1"
bind_port = 9999
```
- In client.py:
```bash
target_host = "127.0.0.1"
target_port = 9999
```
Make sure they match on both ends.

