# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 12:34:41 2021

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


def FrequentWords(sequence,kmer):
    frequent_word = set()
    a = len(sequence)-kmer + 1
    counts = [None]*a
    for i in range(0, a, 1):
        Pattern = sequence[i:i+kmer]
        counts[i] = PatternCount(sequence, Pattern)
    
    maxcount = max(counts)
    
    for i in range(0, a, 1):
        if counts[i] == maxcount:
            frequent_word.add(sequence[i:i+kmer])
    return frequent_word



seq = input("Enter Genome Sequence:\n")
k = int(input("length of k-mer:"))
L = int(input("Length of interval in Genome:"))
t = int(input("Least Number of occurence:"))


print(FrequentWords(seq, k))



for i in range (0, len(seq)-k + 1, 1):
    clump = seq[i:i+L]

print(FrequentWords(clump, k))
    
        
    













