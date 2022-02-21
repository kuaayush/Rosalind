# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:01:02 2021

@author: Administrator
"""

# seq = ""
# for line in open("E coli genome.txt"):
#     if line[0] != ">":
#         seq = seq + line.strip()
        

# seq = input("Enter the DNA String:\n")
# kmer = int(input("Enter the length of pattern:"))
# # pattern = input("Enter the pattern:\n")
# d = int(input("Enter the most mismatched allowed: "))

# AllPattern = []
# for i in range(0, len(seq)- kmer + 1):
#     AllPattern.append(seq[i:i+kmer])

# def HammingDistance(seq1, seq2):
#     hamdist = 0
#     for i in range (0, len(seq1)):
#         if seq1[i] != seq2[i]:
#             hamdist = hamdist + 1
    
#     return hamdist


# def ApproxPatternCount(sequence, Pattern, d):
#     count = 0
#     for i in range(0,len(sequence)-len(Pattern) + 1):
#         Pattern1 = seq[i: i+len(Pattern)]
#         if HammingDistance(Pattern, Pattern1) <= d:
#             count = count+1
#     return count

# result = {}
# # countlist = []
# for i in range(0, len(AllPattern)):
#     result[AllPattern[i]] = ApproxPatternCount(seq, AllPattern[i], d)
    

# itemMaxValue = max(result.items(), key=lambda x: x[1])

# listOfKeys = list()
# for key, value in result.items():
#     if value == itemMaxValue[1]:
#         listOfKeys.append(key)
    


# print("\n")
# print("The length of entered sequence is:", len(seq))
# print("The result for Approximate Pattern Count is: ",result )

# print("\n")
# print(listOfKeys)

# print("\n")
# for i in range(0, len(listOfKeys)):
#     print(listOfKeys[i], end = " ")
    
# print(Pattern)

# Keymax = max(zip(result.values(), result.keys()))[1]

# listOfkeys = []
# for key, value in result.items():
#     if value == Keymax:
#         listOfKeys.append(key)




###########################################################################################################################################

# #TRY NUMBER 1

# def PatternCount(sequence, pattern, d):
#     count = 0
#     b = len(pattern)- d
#     for i in range(0, len(sequence)-len(pattern)+1,1):
#         m = 0
#         for j in range(0, len(pattern), 1):
#             if pattern[j] == sequence[i]:
#                 m = m+1
#             i = i+1
#         if b <= m <= len(pattern):
#             count = count + 1
            
#     return count
# #print(PatternCount(seq, "ATGA"))

# def FrequentWordsWithMismatch(sequence,kmer, d):
#     frequent_word = set()
#     a = len(sequence)-kmer + 1
#     counts = [None]*a
#     for i in range(0, a, 1):
#         Pattern = sequence[i:i+kmer]
#         counts[i] = PatternCount(sequence, Pattern, d)
    
#     maxcount = max(counts)
#     print(maxcount)
#     for i in range(0, a, 1):
#         if counts[i] == maxcount:
#             frequent_word.add(sequence[i:i+kmer])
#     return frequent_word


# seq = input("Enter the DNA String:\n")
# k = int(input("Enter the length of pattern (k): "))
# d = int(input("Enter the number of mismatchs tolerated: "))

# print(seq)
# print(FrequentWordsWithMismatch(seq, k, d))

# print(type(FrequentWords(seq, k, d )))


#==============================================================================


# def HammingDistance(seq1, seq2):
#     print("We are at HAMMING DISTANCE")
#     hamdist = 0
#     for x in range (0, len(seq2)):
#         if seq1[x] != seq2[x]:
#             hamdist = hamdist + 1
#     return hamdist


# def PatternCount(sequence, pattern, kmer, d):
#     print("We are at PATTERN COUNT")
#     count = 0
#     a =len(sequence) -len(pattern) +1
#     for i in range(0, a, 1):
#         m = 0       
#         for j in range(0, len(pattern), 1):
#             if pattern[j] == sequence[i]:
#                 m = m+1
#             i = i + 1
#         if m == len(pattern):
#             count = count + 1
#     patternH = sequence[i: i+kmer]
#     if HammingDistance(pattern, patternH) <= d:
#             count = count +1
        
#     return count
        

# def FrequentWordsWithMismatch(sequence,kmer, d):
#     print("We are at FREQUENT WORDS WITH MISMATCH")
#     frequent_word = set()
#     a = len(sequence)-kmer + 1
#     counts = [None]*a
#     for i in range(0, a, 1):
#         Pattern = sequence[i:i+kmer]
#         counts[i] = PatternCount(sequence, Pattern, kmer, d)
    
#     maxcount = max(counts)
#     print(maxcount)
#     for i in range(0, a, 1):
#         if counts[i] == maxcount:
#             frequent_word.add(sequence[i:i+kmer])
#     return frequent_word


# seq = input("Enter the DNA String:\n")
# k = int(input("Enter the length of pattern (k): "))
# d = int(input("Enter the number of mismatchs tolerated: "))

# print(seq)
# print(FrequentWordsWithMismatch(seq, k, d))









####################################################################################

# def FrequentWordsWithMismatch(sequence,kmer,md):
#     frequent_word = []
#     a = len(sequence)-kmer + 1
#     counts = [None]*a
#     for i in range(0, a, 1):
#         Pattern = sequence[i:i+kmer]
#         m = i
#         hamdist=0
#         for j in range(0, len(Pattern),1):
#             if sequence[m] != Pattern[j]:
#                 hamdist=hamdist+1
#             m = m+1
#         if hamdist <= md:
#             counts[i] = PatternCount(sequence, Pattern)
    
#     maxcount = max(counts)
            
#     for i in range(0, a, 1):
#         if counts[i] == maxcount:
#             frequent_word.append(sequence[i:i+kmer])
#     return frequent_word

####################################################################################
# def PatternFind(string, pattern, d):
#     a = len(string) - len(pattern) +1
#     count = 0
#     b = len(pattern) - d
#     for i in range(0,a,1):
#         m = 0
#         for j in range(0, len(pattern), 1):
#             if pattern[j] == string[i]:
#                 m = m+1
#             i = i+1
#         if b <= m <= len(pattern):
#             count = count +1

#############################################################################3#

def HammingDistance(seq1, seq2):
    hamdist = 0
    for x in range (0, len(seq2)):
        if seq1[x] != seq2[x]:
            hamdist = hamdist + 1
    return hamdist


def PatternCount(sequence, pattern, kmer, d):
    count = 0
    a =len(sequence) -len(pattern) +1
    for i in range(0, a, 1):
        m = 0       
        for j in range(0, len(pattern), 1):
            if pattern[j] == sequence[i]:
                m = m+1
            i = i + 1
        if m == len(pattern):
            count = count + 1
    patternH = sequence[i: i+kmer]
    if HammingDistance(pattern, patternH) <= d:
            count = count +1
        
    return count
        

def FrequentWordsWithMismatch(sequence,kmer, d):
    frequent_word = set()
    a = len(sequence)-kmer + 1
    counts = [None]*a
    for i in range(0, a, 1):
        Pattern = sequence[i:i+kmer]
        counts[i] = PatternCount(sequence, Pattern, kmer, d)
    
    maxcount = max(counts)
    print(maxcount)
    for i in range(0, a, 1):
        if counts[i] == maxcount:
            frequent_word.add(sequence[i:i+kmer])
    return frequent_word


seq = input("Enter the DNA String:\n")
k = int(input("Enter the length of pattern (k): "))
d = int(input("Enter the number of mismatchs tolerated: "))

print(seq)
print(FrequentWordsWithMismatch(seq, k, d))



