#!/home/homero/miniconda3/bin/python
# https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARNING)

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything

logging.basicConfig(level=logging.DEBUG)  # THIS DOES NOT WORK. IT CAN ONLY BE SET ONCE.

logging.warning('Watch out! 2')  # will print a message to the console
logging.info('I told you so 2')  # will NOT print either

x = 100
logging.warning('Run %d times!', x)  # will print a message to the console

a= 'two'
b= 'variables'
logging.warning(f'you can also log {a} {b}')
