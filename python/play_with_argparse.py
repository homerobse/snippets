#!/home/homero/miniconda3/bin/python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('n_files', type=int, help='number of days to be displayed', nargs='?')
parser.add_argument('-w', '--week', help='show week times', action='store_true')
args = parser.parse_args()
print(args)
print(args.n_files)
print(args.week)

