# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:03:13 2021

@author: Administrator
"""

"""     Calculating expected offspring with dominant phenotype      """

# The number of couples possessing each genotype pairing is given below:

c1 = int(input("Enter Number of AA-AA pairing couples:"))      # AA-AA
c2 = int(input("Enter Number of AA-Aa pairing couples:"))      # AA-Aa
c3 = int(input("Enter Number of AA-aa pairing couples:"))      # AA-aa
c4 = int(input("Enter Number of Aa-Aa pairing couples:"))      # Aa-Aa
c5 = int(input("Enter Number of Aa-aa pairing couples:"))      # Aa-aa
c6 = int(input("Enter Number of aa-aa pairing couples:"))      # aa-aa

n = int(input("Enter Number of offspring assumption:"))

E1 = (n * 1) * c1 # probability of dominant phenotype in child for AA_AA pairing is 1
E2 = (n * 1) * c2 # probability of dominant phenotype in child for AA_Aa pairing is 1
E3 = (n * 1) * c3 # probability of dominant phenotype in child for AA_aa pairing is 1
E4 = (n * 0.75) * c4 # probability of dominant phenotype in child for Aa_Aa pairing is 0.75
E5 = (n * 0.5) * c5 # probability of dominant phenotype in child for Aa_aa pairing is 0.5
E6 = (n * 0) * c6 # probability of dominant phenotype in child for aa_aa pairing is 0

Expec_dom = E1 + E2 + E3 + E4 + E5 + E6

print(Expec_dom)