#!/bin/bash
echo "# 1 ---"
for n in 0 1 3 10; do echo "number $n"; echo "another line"; done
echo "# 2 ---"
for n in $(seq 0 2 4); do echo "number $n"; echo "another line"; done
echo "# 3 ---"
for n in $(seq 0 2 4); do 
	echo "number $n"
	echo "another line"
done