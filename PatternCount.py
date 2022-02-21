# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 14:08:43 2021

@author: Administrator
"""


def PatternCount(sequence, pattern):
    count = 0
    for i in range(0, len(sequence)-len(pattern),1):
        m = 0
        for j in range(0,len(pattern),1):
            if pattern[j] == sequence[i]:
                m = m+1
                i = i+1
        if m == len(pattern):
            count = count + 1
    return count

Sequence = input("Enter Genome Sequence:\n")
Pattern = input("Enter Pattern:")
print(PatternCount(Sequence, Pattern))