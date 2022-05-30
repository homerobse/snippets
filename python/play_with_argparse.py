#!/home/homero/miniconda3/bin/python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('n_files', type=int, help='number of days to be displayed', nargs='?')
parser.add_argument('name_files', type=str, help='filenames', nargs='?')
parser.add_argument('-w', '--week', help='show week times', action='store_true')
args = parser.parse_args()
print(args)
print(args.n_files)
print(args.week)
#print(args.name_files)

## E.g. $python play_with_argparse.py 3
## Namespace(n_files=3, week=False)
## 3
## False

## E.g. $python play_with_argparse.py -w
##$ python play_with_argparse.py 2 -w
##Namespace(n_files=2, week=True)
##2
##True

##$ python play_with_argparse.py 12 asdf.lkj
##Namespace(n_files=12, name_files='asdf.lkj', week=False)
##12
##False