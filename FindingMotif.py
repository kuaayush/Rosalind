# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 09:30:11 2021

@author: Administrator
"""


# string = input("Enter DNA Sequence (s):\n")

file = open('E coli genome.txt', 'r')
string = ""
for line in file:
    if line[0] !='>':
        string= string +line.strip()
        
substring = input("Enter Substring to check (t):\n")

def FindMotif(sequence, pattern):
    a = len(sequence)-len(pattern)+1
    pos = []
    for i in range(0, a, 1):
        if pattern == sequence[i:i+len(pattern)]:
            pos.append(i+1)
    return pos


def PatternCount(sequence, pattern):
    count = 0
    for i in range(0, len(sequence)-len(pattern)+1,1):
        if pattern == sequence[i: i+len(pattern)]:
            count = count + 1
    return count

print('\n' +"The length of given sequence:", len(string))
print("Number of patterns found:", PatternCount(string, substring))
print("Location of pattern:",FindMotif(string, substring), '\n')

