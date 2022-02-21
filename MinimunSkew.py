# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 16:42:44 2021

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt


seq = ""
for line in open("E coli 500.txt"):
    if line[0] != ">":
        seq = seq + line.strip()

# seq = input("Enter A DNA string:\n")

def MinSkew(Genome):
    arrayskew = np.zeros(len(Genome))
    arraypos = np.zeros(len(Genome))
    skew = 0

    for i in range(0, len(Genome)):         
        if Genome[i] == "G":
            skew = skew + 1        
        elif Genome[i] == "C":
            skew = skew - 1
        arrayskew[i] = skew
        arraypos[i] = i

    minskew = arrayskew.min()
    minpos1 = np.where(arrayskew == minskew)
    minpos = minpos1 + np.ones(len(minpos1))
    
    fig1 = plt.figure()
    plt.plot(arraypos, arrayskew)
    plt.xlabel("Nucleotide Position")
    plt.ylabel("Skewness")
    plt.title("Position Vs Skewness")
    plt.show()
    
    return minpos

print("\n")
print("The minimum skew is present at following positions:\n")
print(MinSkew(seq))


