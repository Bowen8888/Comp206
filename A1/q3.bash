#! /bin/bash

names=$(ls *.jpg)
images=$(ls *.dat)
a=1
b=$1
if [ "$b" == "alpha" ]
then 
	touch alphas.txt
	while [ "$a" -lt "9" ]
	do
		echo $names | cut -d' ' -f$a  >> alphas.txt
		a=`expr $a + 1`
	done

	cat alphas.txt | sort > f.txt
	cat f.txt
	
	b=1
	while [ "$b" -lt "9" ]
	do
		c=" `head -1 f.txt `"
		sed -i '1d' f.txt
		if [ "$b" == 1 ] 
		then
			convert -append $c zoo.jpg
		else
			convert -append zoo.jpg $c zoo.jpg
		fi
		
		b=`expr $b + 1`
	done
	eog -n zoo.jpg &
	rm alphas.txt
	
fi

if [ "$b" == "weight" ]
then
	touch weights.txt
	while [ "$a" -lt "9" ]
	do
		animal=" `echo $images | cut -d' ' -f$a`" 
		weight=" `cat $animal | cut -d' ' -f1`"
		name=" `echo $names | cut -d' ' -f$a`"
		echo $weight $name >> weights.txt
		a=`expr $a + 1`
	done
	
	cat weights.txt | sort -n >> f.txt
	cat f.txt | cut -d' ' -f2 > weights.txt
	cat weights.txt
	
	b=1
	while [ "$b" -lt "9" ]
	do
		c=" `head -1 weights.txt `"
		sed -i '1d' weights.txt
		if [ "$b" == 1 ] 
		then
			convert -append $c zoo.jpg
		else
			convert -append zoo.jpg $c zoo.jpg
		fi
		
		b=`expr $b + 1`
	done
	eog -n zoo.jpg &
	rm f.txt
	
	rm weights.txt
fi

if [ "$b" == "length" ]
then 
	touch lengths.txt
	while [ "$a" -lt "9" ]
	do 
		animal=" `echo $images | cut -d' ' -f$a`"
		length=" `cat $animal | cut -d' ' -f2`"
		name=" `echo $names | cut -d' ' -f$a`"
		echo $length $name >> lengths.txt
		a=`expr $a + 1`
	done

	cat lengths.txt | sort -n >> f.txt
	cat f.txt | cut -d' ' -f2 > lengths.txt
	cat lengths.txt

	b=1
	while [ "$b" -lt "9" ]
	do
		c=" `head -1 lengths.txt `"
		sed -i '1d' lengths.txt
		if [ "$b" == 1 ] 
		then
			convert -append $c zoo.jpg
		else
			convert -append zoo.jpg $c zoo.jpg
		fi
		
		b=`expr $b + 1`
	done
	eog -n zoo.jpg &
	rm f.txt
	
	rm lengths.txt
fi
