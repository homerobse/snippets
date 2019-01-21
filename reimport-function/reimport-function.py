#!/usr/bin/python3.6
#https://stackoverflow.com/questions/4385839/reimporting-a-single-function-in-python

import os
from module import f

f()

command = "sed -i 's/hello/goodbye/' module.py"  # https://stackoverflow.com/a/53124215/1273751
os.system(command)

import sys
import importlib
importlib.reload(sys.modules['module'])
from module import f

f()

command = "sed -i 's/goodbye/hello/' module.py"
os.system(command)
