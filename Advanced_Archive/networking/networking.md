# 🌐 Advanced Topics: Networking

Building a multiplayer game is one of the hardest challenges in software engineering. In this guide, we'll look at how to connect two players using **Sockets**.

## 1. The Server/Client Architecture

- **Server**: The central brain. It maintains the "Truth" of where everyone is.
- **Client**: The player's game. It sends input to the server and receives updates about other players.

## 2. Python Sockets

We use the built-in `socket` library.

### Basic Server Setup

```python
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()
print("Server is listening...")
```

### Basic Client Connection

```python
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))
```

## 3. The Threading Problem

In a multiplayer game, you can't wait for one player to send data before you update the screen. You need to handle multiple players at once using **Threading**.

```python
import threading

def handle_client(conn):
    while True:
        data = conn.recv(2048)
        # Process and broadcast data
        
# Start a new thread for every new connection
threading.Thread(target=handle_client, args=(conn,)).start()
```

---

## 🛠️ Action: Mini-Exercise

**Goal**: Implement a basic Peer-to-Peer "Ping".

1. Open [advanced_examples.py](file:///c:/Users/m287110/Desktop/Git/Personal_projects/Learning_python/intro_to_pygame/05_Advanced_Topics/advanced_examples.py).
2. Modify the `run_test_client` function. After receiving the welcome message, make the client send a response: `client_socket.send("Ping received! 📥".encode('utf-8'))`.
3. Modify the `run_dedicated_server` function. After sending the welcome message, make the server wait for a response: `data = client_conn.recv(BUFFER_SIZE)`.
4. Print the response on the server side: `print(f"[SERVER] Client says: {data.decode('utf-8')}")`.

**Check your progress**: Run the script. If the server prints "Client says: Ping received!", you've successfully implemented two-way communication!

## 🚀 Further Exploration

Networking is a deep rabbit hole. To go beyond this demo:

- Serialization: Learn how to use `pickle` or `json` to send complex objects (like Player positions) over the wire.
- Latency Compensation: Research "Client-Side Prediction" to make multiplayer games feel smooth even on laggy connections.
- Game Engines: If you're serious about multiplayer, look into professional engines like **Godot** or **Unity**, which have built-in networking stacks.
