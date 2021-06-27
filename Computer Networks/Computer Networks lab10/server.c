#include <stdio.h> 
#include <netdb.h> 
#include <sys/socket.h> 
#include <string.h> 
#include <netinet/in.h> 
#include <sys/types.h> 
#include <stdlib.h> 
#define LEN 1000 
#define SA struct sockaddr 

// Function designed for chat between client and server. 

void func(int sckt1,int sckt2) 
{ 
	int par = getpid();
	int kid2=-1;
	int kid1 = fork();
	if(kid1!=0)
		kid2 = fork();
	if(kid1==0)
	{
		while(1)
		{
			char str[LEN];
			int end=read(sckt1, str, sizeof(str));
			str[end]='\0';
			write(sckt2, str, sizeof(str));
			if(strcmp(str, "exit")==0)
				exit(0);
		}

	}
	else if(kid2==0)
	{
		while(1)
		{
			char str[LEN];
			int end=read(sckt2, str, sizeof(str));
			str[end]='\0';
			write(sckt1, str, sizeof(str));
			if(strcmp(str,"exit")==0 || strcmp(str, "exit\n")==0)
				exit(0);

		}

	}
	while(wait(NULL)!=-1);
	
} 

// Driver function 
int main(int argc, char **args) 
{ 
	int sckt, dpt1,dpt2, len; 
	struct sockaddr_in addr_server, cli; 
	int PORT = atoi(args[1]);
	// socket create and verification 
	sckt = socket(AF_INET, SOCK_STREAM, 0); 
	if (sckt == -1) { 
		printf("Creation of Socket Failed..\n"); 
		exit(0); 
	} 
	else
		printf("Socket Created successfully..\n"); 
	bzero(&addr_server, sizeof(addr_server)); 

	// assign IP, PORT 
	addr_server.sin_family = AF_INET; 
	addr_server.sin_addr.s_addr = htonl(INADDR_ANY); 
	addr_server.sin_port = htons(PORT); 

	// Binding newly created socket to given IP and verification 
	if((bind(sckt, (SA*)&addr_server, sizeof(addr_server))) != 0) { 
		printf("Bind Failure...\n"); 
		// sleep(1);
		exit(0); 
	} 
	else
		printf("Bind successfully done..\n"); 

	if ((listen(sckt, 5)) != 0) { 
		printf("Listen failed...\n"); 
		exit(0); 
	} 
	else
		printf("Server listening..\n"); 
	len = sizeof(cli); 

	while(1)
	{
		dpt1 = accept(sckt, (SA*)&cli, &len); 
		dpt2 = accept(sckt, (SA*)&cli, &len);
		if (dpt1 < 0 || dpt2<0) printf("Failed to accept\n");
		else printf("Accepted the Clients\n"); 
		func(dpt1,dpt2);
		printf("Clients exitted. Now waiting.....\n");
	}

} 
