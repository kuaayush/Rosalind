# -*- coding: utf-8 -*-
"""
Created on Mon May 24 00:01:29 2021

@author: Administrator
"""

seq = ""
for line in open("E coli 500.txt"):
    if line[0] != ">":
        seq = seq + line.strip()
        

# seq = input("Enter the DNA String:\n")
k = int(input("Enter the length of pattern (k): "))

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

#print(PatternCount(seq, "ATGA"))


def FrequentWords(sequence,kmer):
    frequent_word = set()
    a = len(sequence)-kmer + 1
    counts = [None]*a
    for i in range(0, a, 1):
        Pattern = sequence[i:i+kmer]
        counts[i] = PatternCount(sequence, Pattern)
    maxcount = max(counts)
    print(maxcount)
    for i in range(0, a, 1):
        if counts[i] == maxcount:
            frequent_word.add(sequence[i:i+kmer])
    return frequent_word


print(seq)
print(FrequentWords(seq, k))
print(type(FrequentWords(seq, k)))


