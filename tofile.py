import os
import datetime
import sys


def tofile_write(data,file_name):

  file_out = open(file_name, 'a')

  if (type(data[0]) != tuple) and (type(data[0]) != list):    
     result=";".join(str(item) for item in data)
     file_out.write(result)
     file_out.write('\n')	    

  else: 
     for row in data:  
         result=";".join(str(item) for item in row)
         file_out.write(result)
         file_out.write('\n')

  file_out.close()
         
