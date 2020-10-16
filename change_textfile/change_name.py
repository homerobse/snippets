#!/usr/bin/env python3
import fileinput

text_to_search = "rl-book"
replacement_text = "book-club_reading"

with fileinput.FileInput("eg_file", inplace=True, backup='.bakpy') as file:
    for line in file:
        print(line.replace(text_to_search, replacement_text), end='')
