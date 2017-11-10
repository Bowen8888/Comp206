#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Q3.h"

void encrypt(char* str,int key){
	int length = strlen(str);
	char str2[length];
	for(int i=0; i<length;i++){
		str2[i]=str[i]+key;
	}
	for(int i=0; i<length;i++){
		str[i]=str2[length-i-1];
	}
	
	
}

void decrypt(char* str,int key){
	
	
	int length = strlen(str);
	char str2[length];
	for(int i=0; i<length;i++){
		str2[(length-1)-i]=str[i]-key;
	}
	for(int i=0; i<length;i++){
		str[i]=str2[i];
	}
	
}
