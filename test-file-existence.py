import os

if os.path.isfile('existent-file'): 
    print('existent-file exists')
if not os.path.isfile('b'): 
    print('b doesn\'t exist')
    
