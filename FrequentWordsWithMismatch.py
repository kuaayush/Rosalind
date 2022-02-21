# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 22:39:12 2022

@author: Administrator
"""


# seq = ""
# for line in open("E coli genome.txt"):
#     if line[0] != ">":
#         seq = seq + line.strip()
        

seq = input("Enter the DNA String:\n")
kmer = int(input("Enter the length of pattern:"))
# pattern = input("Enter the pattern:\n")
d = int(input("Enter the most mismatches allowed: "))

AllPattern = []
for i in range(0, len(seq)- kmer + 1):
    AllPattern.append(seq[i:i+kmer])


# AllPattern_dict = {}
# for i in range(0, len(seq)- kmer + 1):
#     pattern = seq[i:i+kmer]
#     if pattern not in AllPattern_dict:
#         AllPattern_dict[pattern] = 1
#     else:
#         AllPattern_dict[pattern] +=1


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

result = {}
# result.update(AllPattern_dict)

for i in range(0, len(AllPattern)):
    result[AllPattern[i]] = ApproxPatternCount(seq, AllPattern[i], d)

# for i in result.keys():
#     result[i] = ApproxPatternCount(seq, result[i], d)
    

itemMaxValue = max(result.items(), key=lambda x: x[1])

listOfKeys = list()
for key, value in result.items():
    if value == itemMaxValue[1]:
        listOfKeys.append(key)
    

print("\n")
print("The length of entered sequence is:", len(seq))
print("The result for Approximate Pattern Count is: ",result )

# print("\n")
# print(result.keys())

# print("\n")
print("The number of pattern is : ", len(result))

print("\n")
print("The expected DnaA boxes are: ", listOfKeys)

print("\n")
for i in range(0, len(listOfKeys)):
    print(listOfKeys[i], end = " ")

# print("\n")    
# print(AllPattern)
# print(len(AllPattern))

# print("\n") 
# print(AllPattern_dict)
# print(len(AllPattern_dict))




# Keymax = max(zip(result.values(), result.keys()))[1]

# listOfkeys = []
# for key, value in result.items():
#     if value == Keymax:
#         listOfKeys.append(key)