#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def words_twenty_char():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

##############################################################################
def main():
    words_twenty_char()

if __name__ == '__main__':
    main()
