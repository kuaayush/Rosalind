# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:08:56 2021

@author: Administrator
"""


def PatternFind(string, pattern, d):
    a = len(string) - len(pattern) +1
    count = 0
    b = len(pattern) - d
    for i in range(0,a,1):
        m = 0
        for j in range(0, len(pattern), 1):
            if pattern[j] == string[i]:
                m = m+1
            i = i+1
        if b <= m <= len(pattern):
            count = count +1
        
    return count
    
def FrequentWords(string, kmer,d):
    a = len(string) - kmer +1
    Frequentword = set()
    Counts = [None] * a
    for i in range(0, a, 1):
        Pattern = string[i:i+kmer]
        Counts[i] = PatternFind(string, Pattern, d)
    
    maxCount = max(Counts)
    print(maxCount)
    for i in range(0,a,1):
        if Counts[i] == maxCount:
            adds = ''.join(string[i: i+kmer])
            Frequentword.add(adds)
    return Frequentword
   
    
DNA = input("Please enter the string in all capital")
kmer = int(input("Please enter the kmer"))
string = list(DNA)
d = int(input("Enter the number of mismatches"))

print(FrequentWords(string, kmer, d))