#include <stdlib.h> 
#include <netdb.h> 
#include <string.h> 
#include <stdio.h> 
#include <sys/socket.h> 
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include<signal.h>
#include <string.h>
#include <openssl/rsa.h>
#include <stdio.h>
#include <openssl/pem.h>
#include <stdlib.h>
#define LEN 100 
#define LEN_WRITE 256

void encrypt(char *str, char* crypt_text, char* public_file_name)
{
    FILE *key = fopen(public_file_name, "r");
    RSA *rsa_key = PEM_read_RSA_PUBKEY(key, NULL, NULL, NULL);
    int result = RSA_public_encrypt(strlen(str),str,crypt_text,rsa_key,RSA_PKCS1_PADDING);
}
int decrypt(char crypt_text[], char str[], char* private_file_name)
{
	FILE* key = fopen(private_file_name, "r");
	RSA *rsa_key = PEM_read_RSAPrivateKey(key, NULL, NULL, NULL);
	int  result = RSA_private_decrypt(256,crypt_text,str,rsa_key, RSA_PKCS1_PADDING);
	return result;
}
void printCypher(char* code)
{
	printf("\n");
	fflush(stdout);
	printf("\033[0;33m" );
	fflush(stdout);
	for(int i=0; i<256 ;i++){
		printf("%c",code[i] );
		fflush(stdout);
	}
	printf("\n");
}
void func(int sckt, char* public_file_name, char* private_file_name) 
{ 

	int par = getpid();
	int kid = fork();

	if(kid==0)
	{
		while(1)
		{
			char str[LEN];
			char crypt_text[LEN_WRITE];
			memset(crypt_text, sizeof(crypt_text), 0);
			memset(str, sizeof(str), 0);
			gets(str);
			fflush(stdin);
			encrypt(str, crypt_text, public_file_name);
			fflush(stdout);
			write(sckt, crypt_text, sizeof(crypt_text));
			if(strcmp(str, "exit")==0)
			{
				printf("Exitting....\n");
				kill(par, SIGKILL );
				exit(0);
			}
		}

	}
	else
	{
		while(1)
		{
			char crypt_text[1000], str[100];
			memset(crypt_text, sizeof(crypt_text), 0);
			memset(str, sizeof(str), 0);
			if(read(sckt, crypt_text, sizeof(crypt_text))!= -1)
			{
				int x=decrypt(crypt_text, str, private_file_name);
				str[x]='\0';
				if(strcmp(str,"exit")==0)
				{
					printf("Exitting....\n");
					kill(kid,SIGKILL);
					exit(0);
				}
				printf("\033[0;35m -------------------------------------------------------\033[0m\n");
				fflush(stdout);
				printf("Encrypted Text received is: \n" );
				fflush(stdout);
				printCypher(crypt_text);
				printf("\033[0m" );
				printf("Decoded Text is: ");
				fflush(stdout);
				printf("\033[0;36m" );
				printf("%s\n", str);
				printf("\033[0m" );
				printf("\033[0;35m ---------------------------------------------------------\033[0m\n");
				printf("\033[0m" );
				fflush(stdout);
			}

		}

	}
	exit(0);
}

int main(int argc, char **args) 
{ 
	int sckt, connfd; 
	char ip[20];
	strcpy(ip,args[1]);
	int PORT = atoi(args[2]);
	struct sockaddr_in addr_server, cli;
	char* private_file_name = args[3]; 
	char* public_file_name = args[4];
	sckt = socket(AF_INET, SOCK_STREAM, 0); 
	if (sckt == -1) { 
		printf("Failed to create Socket..\n"); 
		exit(0); 
	} 
	else printf("Socket Created..\n"); 
	bzero(&addr_server, sizeof(addr_server)); 
	addr_server.sin_family = AF_INET; 
	addr_server.sin_addr.s_addr = inet_addr(ip); 
	addr_server.sin_port = htons(PORT); 
	if (connect(sckt, (struct sockaddr*)&addr_server, sizeof(addr_server)) != 0) { 
		printf("Server Unreachable...\n"); 
		exit(0); 
	}
	else printf("Server Connected..\n"); 
	func(sckt, public_file_name, private_file_name); 
	close(sckt); 
} 
