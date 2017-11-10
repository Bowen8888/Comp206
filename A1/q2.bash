#! /bin/bash
images=$(ls *.jpg)
touch check.txt

touch eog_opened.txt

a=$1

while [ 1 ]

do 
	ps > check.txt
	cat check.txt | grep eog > eog_opened.txt
	numOfEogs=" `wc -l eog_opened.txt | cut -d' ' -f1`"

	if [ "$numOfEogs" -lt "$a" ]

	then
		this_image=`echo $images | cut -d' ' -f1`
		images="`echo $images | cut -d' ' -f2-` ${this_image}"
		eog -n $this_image &
	fi

done


