#!/usr/bin/python
import pickle
import sys
import ctypes
#Compile with gcc -shared -fPIC fast_filter.c -o libfast_filter.so
clib = ctypes.cdll.LoadLibrary("./libfast_filter.so")

def parseFilterCmdArgs( cmd_args ):

	  filter_width = int( cmd_args[2] )
	  filter_weights = []
	  filter_offsets = []

	  for i in range(0,filter_width*filter_width):
	    filter_weights.append( float(cmd_args[3+i] ))

	  return ( filter_width, filter_weights )

def loadFile():
	filename = sys.argv[2]
	f = open (filename,'rb')
	list_of_images = []
	i = 1
	list_of_images.append(i)
	img_data = ''
	for line in f:
		img_data = img_data +line
	f.close()
	list_of_images.append(img_data)
	fhistory = open('history.pickle', 'wb')

	pickle.dump(list_of_images,fhistory)

	fhistory.close()

def filterImage():
	fhistory = open('history.pickle', 'rb')
	list_of_images = pickle.load(fhistory)
	fhistory.close()
	
	i=int(list_of_images[0])
	img_data = list_of_images[i]

	(filter_width, filter_weights) = parseFilterCmdArgs( sys.argv )
	out_img_data = ' '*len(img_data)
	builtin_float_array2 = filter_weights
	CFloatArrayType = ctypes.c_float*len(builtin_float_array2)
	cfloat_weights = CFloatArrayType( *builtin_float_array2 )
	
	clib.doFiltering(img_data, cfloat_weights, filter_width, out_img_data)

	
	fp = open('result.bmp','wb')
	fp.write(out_img_data)
	fp.close()
	
	new_list_of_images=[]
	
	a=0
	while a<=i:
		new_list_of_images.append(list_of_images[a])
		a=a+1
	
	new_list_of_images.append(out_img_data)
	
	
	new_list_of_images[0] = i+1

	fhistory = open('history.pickle', 'wb')

	pickle.dump(new_list_of_images,fhistory)

	fhistory.close()
	
	

def undoFilter():
	fhistory = open('history.pickle', 'rb')
	list_of_images = pickle.load(fhistory)
	fhistory.close()
	
	i=list_of_images[0]
	
	
	
	if i>1:
		out_img_data = list_of_images[i-1]
		fp = open('result.bmp','wb')
		
		fp.write(out_img_data)
		fp.close()
		i = i-1
	else:
		print "Not possible"
	list_of_images[0] = i
	
	fhistory = open('history.pickle', 'wb')

	pickle.dump(list_of_images,fhistory)

	fhistory.close()

def redoFilter():
	fhistory = open('history.pickle', 'rb')
	list_of_images = pickle.load(fhistory)
	fhistory.close()
	
	i=list_of_images[0]
	
	
	out_img_data=''
	if i<len(list_of_images)-1:
		out_img_data = list_of_images[i+1]
		fp = open('result.bmp','wb')
		fp.write(out_img_data)
		fp.close()
		i = i+1
	else:
		print "Not possible"
	list_of_images[0] = i
	
	fhistory = open('history.pickle', 'wb')

	pickle.dump(list_of_images,fhistory)

	fhistory.close()
argc = 0
for filename in sys.argv[1:]:
	argc = argc + 1
numToFilter=0
k=0
if argc <1:
	k=0

elif sys.argv[1]=='load' and argc == 2:
	loadFile()
	k=1
elif sys.argv[1]=='filter':
	if(argc >=2):
		numToFilter = int(sys.argv[2])*int(sys.argv[2])+2
	if numToFilter==argc:
		k=1
		filterImage()
elif sys.argv[1]=='undo'and argc == 1:
	undoFilter()
	k=1
elif sys.argv[1]=='redo'and argc == 1:
	redoFilter()
	k=1

if k ==0:
	print "not valid input"
