# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 22:12:16 2022

@author: Administrator
"""


seq = ""
for line in open("E coli genome.txt"):
    if line[0] != ">":
        seq = seq + line.strip()
        

# seq = input("Enter the DNA String:\n")
pattern = input("Enter the pattern:\n")
d = int(input("Enter the most mismatched allowed: "))

def HammingDistance(seq1, seq2):
    hamdist = 0
    for i in range (0, len(seq1)):
        if seq1[i] != seq2[i]:
            hamdist = hamdist + 1
    
    return hamdist

def ApproxPatternCount(sequence, Pattern, d):
    count = 0
    for i in range(0,len(sequence)-len(Pattern) + 1):
        Pattern1 = seq[i: i+len(Pattern)]
        if HammingDistance(Pattern, Pattern1) <= d:
            count = count+1
    return count
print("\n")
print("The length of entered sequence is:", len(seq))
print("The result for Approximate Pattern Count is: ", ApproxPatternCount(seq, pattern, d))