#!/usr/bin/python
import sys
import os.path
def fn():
	letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	list1={}	
	filename = sys.argv[1]
	f = open (filename,'r')
	for line in f:
		for word in line.replace('-',' ').split():
			word=word.lower()
			for i in word:
				if letter.count(i)<1:
					word = word.replace(i,'');
			if word in list1:
				a=int(list1[word])+1
				list1[word] = str(a)
			else:
				list1[word]='1'
	f.close()
	
	list2=[]
	
	list2=list1.values()
	maximum=int(max(list2))
	for number in list2:
		if int(number) > maximum:
			maximum=int(number)
	

	
	while maximum>0:
		
		for key in list1: 
			a=int(list1[key])
			if a==maximum:
				print key + ':'+ list1[key]
		maximum=maximum-1
	

argc = 0
for filename in sys.argv[1:]:
	argc = argc + 1
	
if argc==1 and os.path.isfile(filename):
	fn()
else:
	print "Usage: python q1_word_count.py filename "
	print "file must exist"
