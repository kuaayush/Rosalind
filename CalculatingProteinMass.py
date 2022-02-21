# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:26:18 2021

@author: Administrator
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:07:21 2021

@author: Administrator
"""

#     A = 71.03711        # ALANINE
#     C = 103.00919       # CYSTEINE
#     D = 115.02694       # ASPARTATE
#     E = 129.04259       # GLUTAMATE
#     F = 147.06841       # PHENYLALANINE
#     G = 57.02146        # GLYCINE
#     H = 137.05891       # HISTIDINE
#     I = 113.08406       # ISOLEUCINE
#     K = 128.09496       # LYSINE
#     L = 113.08406       # LEUCINE
#     M = 131.04049       # METHIONINE
#     N = 114.04293       # ASPARAGINE
#     P = 97.05276        # PROLINE
#     Q = 128.05858       # GLUTAMINE
#     R = 156.10111       # ARGININE
#     S = 87.03203        # SERINE
#     T = 101.04768       # THREONINE
#     V = 99.06841        # VALINE
#     W = 186.07931       # TRYPTOPHAN
#     Y = 163.06333       # TYROSINE

peptide = input("Enter the amino acid sequence:")
pep_list = list(peptide)
pep_wei_list = []

for aa in pep_list:
    weight = aa.replace("A", "71.03711").replace("C", "103.00919").replace("D", "115.02694").replace("E", "129.04259").replace("F", "147.06841").replace("G", "57.02146").replace("H", "137.05891").replace("I", "113.08406").replace("K", "128.09496").replace("L", "113.08406").replace( "M", "131.04049").replace( "N", "114.04293").replace("P", "97.05276").replace( "Q", "128.05858").replace("R", "156.10111").replace("S", "87.03203").replace("T", "101.04768").replace("V", "99.06841").replace("W", "186.07931").replace("Y", "163.06333") 
    pep_wei_list.append(weight) 
    

pep_wei_list2 = []
for i in range(0, len(pep_wei_list)):
    j = float(pep_wei_list[i])
    pep_wei_list2.append(j)


s = 0
for e in range(0,len(pep_wei_list2)):
    s = s + pep_wei_list2[e]

 
# print(pep_wei_list)
# print(pep_wei_list2)
print("\nThe protein mass is:", round(s, 3), "Da")










