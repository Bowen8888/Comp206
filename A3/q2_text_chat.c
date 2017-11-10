#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void main(int argc, char *argv[]){
	if(argc!=4){printf("Usage: ./program incomingfile outgoingfile User\n");}
	else{
	FILE *file1;
	FILE *fp;
	char * str1;
	char * strcp1;
	long fileSize1;
	
	char msg[1000];
	
	file1 = fopen(argv[1],"r");
	if (!file1){
		
		file1 = fopen(argv[1],"w");
		fclose(file1);
	}
	file1 = fopen(argv[1],"r");
	fseek( file1 , 0L , SEEK_END);
	fileSize1= ftell( file1 );
	rewind(file1);
	strcp1 = calloc (1, fileSize1+1);
	fread( strcp1 , fileSize1, 1 , file1);
	fclose(file1);
	
	if(strcmp("",strcp1)==0){
		printf("Nothing received yet\n");
	}
	else{
		printf("Received: ");
		printf("%s",strcp1);
	}
	int p=1;
	while (1){
		
		file1 = fopen(argv[1],"r");
		fseek( file1 , 0L , SEEK_END);
		fileSize1 = ftell( file1 );
		rewind(file1);
		str1 = calloc (1, fileSize1+1);
		fread( str1 , fileSize1, 1 , file1);
		fclose(file1);	
		
		if((strcmp(str1,strcp1)!=0&&strcmp(str1,"")!=0)||p==1){
			if(p!=1){
				printf("Received: ");
				for(int t=0; t<strlen(str1); t++){
					printf("%c",str1[t]);
				}
			}


			
			strcp1 = calloc (1, fileSize1+1);
			
			strcp1=str1;
			printf("Send:     ");
			fgets(msg,1000,stdin);
	
			fp=fopen(argv[2],"w");
			fprintf(fp, "[%s] ",argv[3]);
			fprintf(fp, "%s",msg);
			//fflush(fp);
			fclose(fp);
			p=0;
		}
	}
	}
}	
