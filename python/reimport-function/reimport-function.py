#!/usr/bin/python3.6
#https://stackoverflow.com/questions/4385839/reimporting-a-single-function-in-python

import os
from module import f

f()

# changing f
command = "sed -i 's/hello/goodbye/' module.py"  # https://stackoverflow.com/a/53124215/1273751
os.system(command)

# reloading
import sys
import importlib
importlib.reload(sys.modules['module'])
from module import f

# calling the altered f
f()

# changing back to the original
command = "sed -i 's/goodbye/hello/' module.py"
os.system(command)

## if function is not from a module, do the following:

def g(x):
   return x+1

print(g(3))

def new_g(x):
   return x-1
 
g = new_g
print(g(3))

