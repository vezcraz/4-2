%option noyywrap
	#include<stdio.h>
	#include<string.h>
	int count1 = 0, count2 = 0, count3 = 0;

DUAL (A[1348A])|(B[1-5])
SRNO 0(([0-3][0-9][0-9])|(4(([0-7][0-9])|(8[0-3]))))
%%
200[4-9]{DUAL}A7{SRNO}G {
											/* printf("ID %s\n",yytext); */
											count1++; count3++;
											char s1[14];
											strcpy(s1,yytext);
											s1[4] = '\0'; s1[12] = '\0';
											int x = strcmp(s1,"2009"), y = strcmp(s1+8,"0463");
											if(x<=0 && y<=0) count2++;
											printf(yytext);										if(x<=0 && y<=0) count2++;
										}
201[0-7]{DUAL}A7{SRNO}G {
											/* printf("ID %s\n",yytext); */
											count1++; count3++;
											char s1[14];
											strcpy(s1,yytext);
											s1[4] = '\0'; s1[12] = '\0';
											int x,y;
											x = strcmp(s1,"2019");
											y = strcmp(s1+8,"0463");
											if(x<=0 && y<=0) count2++;
											printf(yytext);										if(x<=0 && y<=0) count2++;
										}
20......[0-9][0-9][0-9][0-9]G { /* Other IDs: */ count3++; }
. { /* Anything else: Ignore */ }
%%

int main(void) {
	yylex();
	printf("%d %d %d\n",count1, count2, count3);
}
