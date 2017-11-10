#include <stdio.h>
#include <stdlib.h>
int file_exists(const char * filename);
int main(int argc, char **argv)
{
	if(argc<=3){
		printf("Usage: ./calendar label_file day_spacing first_day \n");
	}
	else{
	int arg2 = atoi(argv[2]);
	FILE *file;
	file = fopen( argv[1], "r" );
	int arg3 = atoi(argv[3]);
	if ((arg2<2)||(arg3<1)||(arg3>7)||(file_exists(argv[1])==0)){
		printf("argument not valid\n");
	}
	else{
	int x;
	arg3--;
	int count=0;
	for(int q=0;q<(arg2*7);q++){
		printf("*");
	}
	printf("********************\n");
	printf("*");
	

	while  ( ( x = fgetc( file ) ) != EOF)
            {	
		if (count==1){
		if(x!=10){
                printf( "%c", x );
			}
			if((x==' ')||(x==10)){
				printf("\n");
				FILE *file2;
				file2 = fopen( argv[1], "r" );
				int y;
				for(int q=0;q<(arg2*7);q++){
					printf("*");
					}
				printf("********************\n");
				printf("* ");
				int w=0;
				int countletter=0; //new
				while ( ( y = fgetc( file2 ) ) != EOF && (y!=10)){
					if (w<arg2){
					printf( "%c", y );
					countletter++;//new
					w++;
					}
					if(y==' '){
						while(countletter<arg2){//new
							printf(" ");
							countletter++;
						}
						printf(" * ");
						w=0;
						countletter=0;
					}
						
				}
				printf("\n");
				for(int q=0;q<(arg2*7);q++){
					printf("*");
					}
				printf("********************");				
				fclose(file2);
				printf("\n");
				for(int t=0; t<(arg3%7); t++){
						printf("*");
						for(int k=0; k<(arg2+2); k++){
							
								printf(" ");
							}
						}
				for (int i=1; i<31; i++){
					

						printf("* %d ",i);
					
					if(i>9){
						
						for(int k=0; k<(arg2-2); k++){
							
							printf(" ");
						}
					}
					else{
						
						for(int k=0; k<(arg2-1); k++){
							printf(" ");
						}
					
					}
					if(( ( (arg3+i) % 7 ) == 0)&&(i!=30)) {
						printf("\n");
					}
	
				}
				
				arg3=arg3+2;
				int c=arg3;
				while((c%7)!=0){
						printf("*");
						for(int k=0; k<(arg2+2); k++){
							
								printf(" ");
							}
						c++;
						}
				printf("\n");
				for(int q=0;q<(arg2*7);q++){
					printf("*");
					}
				printf("********************");
				printf("\n*");
				
			}
			
		}
		if (x==10){
		count++;
		}
		
            }
	fclose(file);
	}
	}
	return 0;
}

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
