#include <stdio.h>
#include <string.h>
int file_exists(const char * filename);
int main (int argc, char **argv)
{
	if ((argc!=2)||(file_exists(argv[1]))==0){
		printf("input is not valid\n");
	}
	else{
	int x;
	FILE *file = fopen( argv[1], "r" );
	const char *a[7];
	a[0] = "Sun";
	a[1] = "Mon";
	a[2] = "Tue";
	a[3] = "Wed";
	a[4] = "Thu";
	a[5] = "Fri";
	a[6] = "Sat";

	char str[60];
	fgets(str,4,stdin);
	
	int d=100 ;
	for (int i=0;i<7; i++){
		if (strcmp(str, a[i])==0){
			d=i;
			break;
		}
	}
	const char *months[12];
	months[0] = " Jan";
	months[1] = " Feb";
	months[2] = " Mar";
	months[3] = " Apr";
	months[4] = " May";
	months[5] = " Jun";
	months[6] = " Jul";
	months[7] = " Aug";
	months[8] = " Sep";
	months[9] = " Oct";
	months[10] = " Nov";
	months[11] = " Dec";
	char str2[60];
	fgets(str2,5,stdin);

	int newd=100 ;
	for (int i=0;i<12; i++){
		if (strcmp(str2, months[i])==0){
			newd=i;
			break;
		}
	}
	if ((d==100)||(newd==100)){
		printf("Error\n");
	}
	else{
	int count2=-6;
	
	int count=0;
	while  ( (( x = fgetc( file ) ) != EOF))
            {
		
		if ((count==d)&&(count2!=newd)){
			if(x!=10){
                	printf( "%c", x );
			}
			else{
			printf(" ");
			count=-100;
			}
		}
		if (count2==newd){
			if(x!=10){
                	printf( "%c", x );
			}		
			else{
			printf(" ");	
			}
		}
		if (x==' '){
			count++;
			count2++;
		}
            }
	fclose(file);
	int c;
	fgets(str2,2,stdin);
	while((c = getchar())!=EOF){
		
		putchar(c);
	}
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
