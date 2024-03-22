# client.py
import socket
import ssl
# Create an SSL context for server authentication
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
# Load the server certificate for verification
context.load_verify_locations("server.crt")
# Main function for the client to connect to the server
def main():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Wrap the socket with SSL/TLS
    secure_socket = context.wrap_socket(client_socket, server_hostname="localhost")
    try:
        # Connect to the server
        secure_socket.connect(('localhost', 12345))
        # Receive and print the player number from the server
        player_number = secure_socket.recv(1024).decode()
        print("Welcome to RPS game\n")
        print(player_number)
        # Get user input for their choice
        choice = input("Enter your choice (rock/paper/scissors): ")
        # Send the choice to the server
        secure_socket.send(choice.encode())
        # Receive and print the game result from the server
        result = secure_socket.recv(1024).decode()
        print(result)
    except (ConnectionResetError, ConnectionAbortedError, KeyboardInterrupt):
        print("\nClient Shutting Down...")
    finally:
        # Close the secure socket
        secure_socket.close()
# Entry point of the program
if __name__ == "__main__":
    main()
