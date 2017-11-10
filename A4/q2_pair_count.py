#!/usr/bin/python
import sys
import os.path
def fn():
	letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	filewords=[]
	
	filename = sys.argv[1]
	f = open (filename,'r')
	for line in f:
		for word in line.replace('-',' ').split():
			word=word.lower()
			for i in word:
				if letter.count(i)<1:
					word = word.replace(i,'');
			filewords.append(word)
	f.close()
	
	
	pairlist=[]
	
	a=len(filewords)-1
	for i in range(0,a):
		pair= filewords[i]+'-' +filewords[i+1]
		pairlist.append(pair)
	
	
	pairdict={}
	for key in pairlist:
		if key in pairdict:
			a=int(pairdict[key])+1
			pairdict[key] = str(a)
		else:
			pairdict[key]='1'
	
	list2=[]
	list2=pairdict.values()
	maximum=int(max(list2))
	for number in list2:
		if int(number) > maximum:
			maximum=int(number)

	
	while maximum>0:
		
		for k in pairdict: 
			a=int(pairdict[k])
			if a==maximum:
				print k + ':'+ pairdict[k]
		maximum=maximum-1
argc = 0
for filename in sys.argv[1:]:
	argc = argc + 1
	
if argc==1 and os.path.isfile(filename):
	fn()
else:
	print "Usage: python q2_pair_count.py filename "
	print "file must exist"
