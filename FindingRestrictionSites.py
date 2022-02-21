# -*- coding: utf-8 -*-
"""
Created on Mon May 24 00:01:29 2021

@author: Administrator
"""



sequence = ""
for line in open("genome.txt"):
    if line[0] != '>':
        sequence = sequence +line.strip()

restriction_site = input("Enter the sequence of Restriction Site:")

def restrictionSiteCount(seq, res):
    count = 0
    for i in range(0, len(seq)-len(res)+1, 1):
        site = seq[i:i+len(res)]
        if site == res:
            count = count + 1
    return count


print(sequence)
print(restriction_site)
print(restrictionSiteCount(sequence, restriction_site))





































