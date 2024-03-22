Hey there, hope you understand how this entire things works :)

Objective: To develop a multiplayer Rock-Paper-Scissors game using socket programming in Python, allowing multiple players to compete against each other over a network.

Overview: The project involves creating a server-client architecture where a central server manages the game state and facilitates communication between multiple clients. 
Players will connect to the server, select their moves (Rock, Paper, or Scissors), and receive feedback on the game outcome.

Language used - Python

Server Side script : 

Creates a socket using socket.socket() with IPv4 and TCP. 
Binds the socket to the server's IP address and port 12345 using bind(). 
Starts listening for incoming connections using listen().
Creates an SSL context with ssl.create_default_context() and loads the server's certificate and private key using load_cert_chain().
Enters a try-except block to handle potential exceptions, including Keyboard Interrupt for graceful termination.
Inside the try block, the script waits for incoming client connections inside the try block, the script waits for incoming client connections using accept() 
within a with statement that wraps the SSL socket.accept() within a with statement that wraps the SSL socket.

Client Side script : 

Creates an SSL context using ssl.create_default_context(). This context will be used to wrap the client socket with SSL encryption.
Receives a message from the server indicating whether the client is Player 1 or Player 2.
Prompts the user to input their choice for the game (rock/paper/scissors) using input().
Sends the user's choice to the server using send().
Receives the game result from the server using recv() and prints it to the console.

SSL Setup : 

The SSL certificate is used to verify the identity of the server to the clients, ensuring they are connecting to the correct server. 
The private key is used to decrypt data encrypted by the public key in the certificate, ensuring secure communication between the clients and the server. 
This encryption ensures that the game data, including player choices and game results, is protected from eavesdropping and tampering.
The server uses the ssl.create_default_context() function to create an SSL context with default settings.The server loads its certificate chain and private 
key using the load_cert_chain() method of the SSL context.
The client also creates an SSL context using ssl.create_default_context(). This creates an SSL context with default settings.The client specifies 
the location of trusted CA certificates using load_verify_locations() to enable verification of the server's certificate during the SSL handshake.
