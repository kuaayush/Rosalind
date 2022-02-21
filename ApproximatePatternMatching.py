# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:17:30 2021

@author: Administrator
"""


# def HammingDistance(seq1, seq2):
#     hamdist = 0
#     for i in range (0, len(seq1)):
#         if seq1[i] != seq2[i]:
#             hamdist = hamdist + 1
    
#     return hamdist

# def ApproxPatternMatching (string, pattern, d):
#     pos = []
#     for i in range(0, len(string)-len(pattern)+1,1):
#         patternH = string[i:i+len(pattern)]
#         if HammingDistance(pattern, patternH) <=d:
#             pos.append(i)
#     return pos

# sequence = input("Enter the DNA Sequence:\n")
# substring = input("Enter the pattern:\n")
# d = int(input("Enter the most mismatched allowed: "))

# positions = ApproxPatternMatching(sequence, substring, d)

# for i in range (0,len(positions)):
#     print(positions[i], end=" ")
# print("\nThe number of repeats is :",len(positions))


# -------------------------------------------------------------------------


def HammingDistance(seq1, seq2):
    hamdist = 0
    for i in range (0, len(seq1)):
        if seq1[i] != seq2[i]:
            hamdist = hamdist + 1
    
    return hamdist

def ApproxPatternMatching (string, pattern, d):
    pos = []
    pat = []
    result = {}
    for i in range(0, len(string)-len(pattern)+1,1):
        patternH = string[i:i+len(pattern)]
        if HammingDistance(pattern, patternH) <= d:
            pos.append(i)
            pat.append(patternH)
    for a in range(0, len(pos)):
        result[pos[a]]= pat[a]
    return result

sequence = input("Enter the DNA Sequence:\n")
substring = input("Enter the pattern:\n")
d = int(input("Enter the most mismatched allowed: "))


print(ApproxPatternMatching(sequence, substring, d))













# def ApproxPatternMatching (string, pattern, md):
#     pos = []
#     for i in range(0, len(string)-len(pattern)+1,1):
#         hamdist = 0
#         m = i
#         for j in range(0,len(pattern), 1):
#             if string[m] != pattern[j]:
#                 hamdist = hamdist+1
#             m = m+1
#         if hamdist <= md:
#             pos.append(i)
#     return pos

# sequence = input("Enter the DNA Sequence:\n")
# substring = input("Enter the pattern:\n")
# d = int(input("Enter the most mismatched allowed: "))

# positions = ApproxPatternMatching(sequence, substring, d)

# for i in range (0,len(positions)):
#     print(positions[i], end=" ")
# print("\nThe number of repeats is :",len(positions))




































