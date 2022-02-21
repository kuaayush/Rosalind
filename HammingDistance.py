# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:10:08 2021

@author: Administrator
"""


def HammingDistance(seq1, seq2):
    if len(seq1) != len(seq2):
        print("Re-enter the sequences of equal length")
    else:
        hamdist = 0
        for i in range (0, len(seq1)):
            if seq1[i] != seq2[i]:
                hamdist = hamdist + 1
    return hamdist

sequence1 = input("Enter Sequence 1: ")
sequence2 = input("Enter Sequence 2: ")

print(HammingDistance(sequence1, sequence2))
