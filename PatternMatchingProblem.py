# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:06:31 2021

@author: Administrator
"""


string = input("Enter DNA Sequence (s):\n")
substring = input("Enter Substring to check (t):\n")

def PatternMatching(sequence, pattern):
    a = len(sequence)-len(pattern)+1
    pos = []
    for i in range(0, a, 1):
        if pattern == sequence[i:i+len(pattern)]:
            pos.append(i)
    return pos

positions = PatternMatching(string, substring)

print('\n' +"The length of given sequence:", len(string))
print("Motif",substring, "is found at following positions:")
for i in range(0, len(positions)):
    print(positions[i], end = " ")
