#!/usr/bin/python
import ctypes
#Compile with gcc -shared -fPIC fast_filter.c -o libfast_filter.so
clib = ctypes.cdll.LoadLibrary("./libfast_filter.so")
import sys

filename = sys.argv[1]
f = open (filename,'rb')
img_data = ''
for line in f:
	img_data = img_data +line
f.close()
def parseFilterCmdArgs( cmd_args ):

  filter_width = int( cmd_args[3] )
  filter_weights = []
  filter_offsets = []

  for i in range(0,filter_width*filter_width):
    filter_weights.append( float(cmd_args[4+i] ))

  return ( filter_width, filter_weights )

(filter_width, filter_weights) = parseFilterCmdArgs( sys.argv )
out_img_data = ' '*len(img_data)
builtin_float_array2 = filter_weights
CFloatArrayType = ctypes.c_float*len(builtin_float_array2)
cfloat_weights = CFloatArrayType( *builtin_float_array2 )
clib.doFiltering(img_data, cfloat_weights, filter_width, out_img_data)

filename2=sys.argv[2]
fp = open(filename2,'wb')
fp.write(out_img_data)
fp.close()
