""" 
🌐 Lesson 05: Networking Fundamentals (Server & Client)
Expected Behavior: 
This script will launch a background Server thread and a foreground Client.
- The Server will start listening on localhost:5555.
- The Client will attempt to connect.
- Upon successful connection, the Server will send a "Welcome" message.
- The Client will print the received message and then both will close.
"""

import socket
import threading
import time
import sys

# Constants
SERVER_HOST = '127.0.0.1' # Localhost
SERVER_PORT = 5555
BUFFER_SIZE = 1024

def run_dedicated_server():
    """ 
    A simple server that listens for one connection, sends a welcome message, and closes.
    In a real game, this would loop and handle multiple players in individual threads.
    """
    # 1. Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Bind the socket to the address and port
    try:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
    except socket.error as e:
        print(f"[SERVER] Bind failed: {e}")
        return

    # 3. Listen for incoming connections
    server_socket.listen(1)
    print(f"[SERVER] Listening on {SERVER_HOST}:{SERVER_PORT}...")
    
    # 4. Accept a connection
    client_conn, client_addr = server_socket.accept()
    print(f"[SERVER] Accepted connection from {client_addr}")
    
    # 5. Send data
    welcome_msg = "Hello from the Pygame Masterclass Server! 🚀"
    client_conn.send(welcome_msg.encode('utf-8'))
    
    # 6. Clean up
    client_conn.close()
    server_socket.close()
    print("[SERVER] Transaction complete. Server shutting down.")

def run_test_client():
    """
    A simple client that connects to the server, receives a message, and prints it.
    """
    print("[CLIENT] Attempting to connect to server...")
    
    # 1. Create the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Connect to the server
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        
        # 3. Receive data
        received_data = client_socket.recv(BUFFER_SIZE)
        message = received_data.decode('utf-8')
        print(f"[CLIENT] Message received: {message}")
        
    except ConnectionRefusedError:
        print("[CLIENT] Error: Connection refused. Is the server running?")
    except Exception as e:
        print(f"[CLIENT] Unexpected error: {e}")
    finally:
        # 4. Close
        client_socket.close()
        print("[CLIENT] Connection closed.")

if __name__ == "__main__":
    print("--- Advanced Networking Demonstration ---")
    
    # We run the server in a separate thread so it doesn't block the client from running.
    server_thread = threading.Thread(target=run_dedicated_server, daemon=True)
    server_thread.start()
    
    # Give the server a moment to start up
    time.sleep(1)
    
    # Run the client in the main process
    run_test_client()
    
    print("--- End of Demonstration ---")
    sys.exit()
