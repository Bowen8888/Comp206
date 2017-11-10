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
	if(argc!=2||file_exists(argv[1])==0){printf("Usage: ./program filename\n");}
	else{
	FILE *file = fopen (argv[1],"r");
	long fileSize;
	char *str;
	
	
	fseek( file , 0L , SEEK_END);
	fileSize= ftell( file );
	rewind( file );
	
	str =  calloc (1, fileSize+1);

	fread( str , fileSize, 1 , file);
	int length = strlen(str);
	char str2[length]; 
	int k=0;
	int stop =0;
	while (k<256){
	for (int i=length-1;i>=0; i--){
		char a = str[i]-k;
			str2[(length-1)-i]=str[i]-k;

	}
	for (int i=0 ; i< length;i++){
		if (!((str2[i]>96 && str2[i]<123)||(str2[i]>64 && str2[i]<91)||(str2[i]==' ')||(str2[i]=='\0'))){
			break;
		}
		if(i==(length-1))
		if((strchr(str2,'a')&&strchr(str2,'z'))||(strchr(str2,'a')&&strchr(str2,'Z'))||(strchr(str2,'A')&&strchr(str2,'z'))||(strchr(str2,'A')&&strchr(str2,'Z')))
		stop=1;
	}
	if (stop!=0)
		break;
	k++;
	}
	printf("%d\n",k);
	for (int i=0 ; i< length;i++){
		printf("%c",str2[i]);
	}
	printf("\n");
	fclose(file);
	free(str);
	}
}


