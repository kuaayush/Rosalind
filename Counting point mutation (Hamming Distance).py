# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:05:56 2020

@author: Administrator
"""

### The code below counts the total number of point mutations, by comparing two sequences and
### couting the number of mismatches in respective places.
dna1 = input("Enter sequence1 :")
dna2 = input("Enter sequence2 :")

def HammingDistance(sequence1, sequence2):
    if len(sequence1) != len(sequence2):
        print("The provided sequences are of UNEQUAL LENGTH")
    else:
        hamdis = 0
        for i in range(0, len(sequence1)):
            if sequence1[i] != sequence2[i]:
                hamdis = hamdis + 1
                
    return hamdis
print("Number of mismatches in two sequences is:", HammingDistance(dna1, dna2))
