#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int file_exists(const char * filename)
{
	FILE *file;
    if ( file = fopen(filename, "r"))
    {
        fclose(file);
        return 1;
    }
    return 0;
}
void main(int argc, char *argv[]){
	if (argc!=3||file_exists(argv[2])==0){printf("Usage: ./program number filename\n");}
	else{
	FILE *file = fopen (argv[2],"r");
	long fileSize;
	char *str;
	int arg1 = (atoi(argv[1])%256);

	fseek( file , 0L , SEEK_END);
	fileSize= ftell( file );
	rewind( file );
	str =  calloc (1, fileSize+1);
	fread( str , fileSize, 1 , file);
	
	int length = strlen(str);
	char str2[length]; 
	for (int i=length-1;i>=0; i--){
			str2[(length-1)-i]=str[i]-arg1;
	}
	for (int i=0 ; i< length;i++){
		printf("%c",str2[i]);
	}
	printf("\n");
	}
}
