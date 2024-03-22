# server.py
import socket
import ssl

# Function to play a round of the game between two clients
def play_game(client1, client2):
    # Define the choices for the game
    choices = ['rock', 'paper', 'scissors']
    # Receive and decode choices from both clients
    c1_choice = client1.recv(1024).decode()
    c2_choice = client2.recv(1024).decode()

    # Determine the result of the game
    result = ""
    if c1_choice == c2_choice:
        result = "It's a tie!"
    elif (c1_choice == 'rock' and c2_choice == 'scissors') or \
         (c1_choice == 'scissors' and c2_choice == 'paper') or \
         (c1_choice == 'paper' and c2_choice == 'rock'):
        result = "Player 1 wins!"
    else:
        result = "Player 2 wins!"

    # Send the result to both clients
    client1.send(result.encode())
    client2.send(result.encode())

# Main function to run the game server
def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the address and port
    server_socket.bind(('localhost', 12345))
    # Listen for incoming connections
    server_socket.listen(2)
    print("Waiting for connections...")

    # Create an SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # Load the server certificate and key
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    try:
        # Wrap the socket with SSL/TLS
        with context.wrap_socket(server_socket, server_side=True) as ssl_socket:
            while True:
                # Accept the first client connection
                client1, addr1 = ssl_socket.accept()
                print(f"Player 1 connected from {addr1}")
                # Send a message to the first client indicating their player number
                client1.send("You are Player 1".encode())

                # Accept the second client connection
                client2, addr2 = ssl_socket.accept()
                print(f"Player 2 connected from {addr2}")
                # Send a message to the second client indicating their player number
                client2.send("You are Player 2".encode())

                # Play a round of the game between the two clients
                play_game(client1, client2)
                # Close the connections to both clients
                client1.close()
                client2.close()

    except KeyboardInterrupt:
        print("\nServer Shutting Down...")
    finally:
        # Close the server socket
        server_socket.close()

# Entry point of the program
if __name__ == "__main__":
    main()
