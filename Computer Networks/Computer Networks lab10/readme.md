#Compilation
Run the command `make all`
This will create 2 runnable files `client.out` and `server.out`
or
for server:
`gcc -o server.out server.c`
for client:
`gcc client.c -lssl -lcrypto -o client.out`

#Server (Run this first)
Run the command :
`./server.out 8080`
Now the server has started listening and will accept two clients
Sample Run:
`./server.out 8080`

#Client
** Please make sure to run this in a black background terminal **
Run the command :
`./client.out <ip> <port> <self_private_key> <other_public_key>`
Now type in the string to send to the other client.
Sample Run:
(client 1):
`./client.out 127.0.0.1 8080 private2.pem public1.pem` 
(client 2):
`./client.out 127.0.0.1 8080 private1.pem public2.pem`


#Expected Output
-After typing a string in a client, the output can be seen in the other client
-The text in yellow color is the encrypted text received.
-The text in cyan color is the decrypted text.
