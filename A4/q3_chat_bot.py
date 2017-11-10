#!/usr/bin/python
from sys import stdin
import sys
import random
import os.path
letter = ['.','?','!','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
punctuations=['.','!','?']
letter2 =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

allwords=[]
all_file_exist = True
argc = 0
for filename in sys.argv[1:]:
	argc = argc + 1
	if (not os.path.isfile(filename)):
		all_file_exist = False


if (all_file_exist and argc >= 1):
	for filename in sys.argv[1:]:
	
		f = open(filename, "r")
		for line in f:
			for word in line.replace('-',' ').split():
				word=word.lower()
				for i in word:
					if letter.count(i)<1:
						word = word.replace(i,'');
				
				if word != '':
					allwords.append(word)
			
		f.close()
	listwithnopunc=[]
	for i in allwords:
		for punc in i:
			if punc not in letter2:
				i=i.replace(punc,'')
		listwithnopunc.append(i)
	a=len(allwords)-1
	pairlist=[]
	for i in range(0,a):
		first = allwords[i]
		for punc in first:
			if punctuations.count(punc)>=1:
				first = first.replace(punc,'')
		pair = first+' ' +allwords[i+1]
		pairlist.append(pair)
	
	
			

	checkEnd = {}
	for i in pairlist:
		word_length= len(i)-1
		punc = i[word_length]
		if punc in punctuations:
			i= i.replace(punc, '')
			checkEnd[i] = '1';
		if (i not in checkEnd):
			checkEnd[i] = '0';


	keys = []
	for word in pairlist:
		for char in word:
			if char in punctuations:
				word =  word.replace(char,'')
		keys.append(word);
	#print keys

	while 1:
		sys.stdout.write( "Send:     ")
		line = stdin.readline()
		incoming= line.split()
	
	
		word= incoming[len(incoming)-1]
		word=word.lower()
		for i in word:
			if letter2.count(i)<1:
				word = word.replace(i,'');
		if word not in listwithnopunc or word == '':
			word = random.choice(listwithnopunc)
		if word in listwithnopunc:
			index1 = listwithnopunc.index(word)
			pair = ''
			if (index1<(len(listwithnopunc)-1)):
				smt = listwithnopunc[index1+1]
				pair = word + ' ' + smt
			else:
				pair = random.choice(keys)
			if pair not in keys:
				pair = random.choice(keys)
			index= keys.index(pair)
			check=index
			a=index+20
			output =""
			while index<a:
				if (index<len(keys)-1):
					key = keys[index+1].split()[0]
					if index==check:
						key=key.title()
				
					word = keys[index+1]
					if (checkEnd[word]=='1'):
						key = keys[index+1]
						index = a+1
					output = output+key
					index=index+1
					if (index <a):
						output = output + " "
				else:
					index = a+1

			print "Received: "+ output +"."
else:
	print "Usage: python q3_chat_bot.py filename1 filename2 ... files must exist"


















