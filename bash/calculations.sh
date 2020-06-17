#!/bin/bash

# https://www.shell-tips.com/2010/06/14/performing-math-calculation-in-bash/
expr 1+1 # doesn't work
expr 1 + 1  # does work

echo $((2*4))  

echo "scale=3; 2/3" | bc

awk "BEGIN {print 100/3}"
