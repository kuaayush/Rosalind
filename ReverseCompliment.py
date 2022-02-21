# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:17:12 2021

@author: Administrator
"""


def reverseComplement(dna):
    DNA = dna.upper()
    
    comp =""
    for i in DNA:
        if i =='A':
            comp = comp+'T'
        elif i =='G':
            comp = comp +'C'
        elif i =='T':
            comp = comp+ 'A'
        elif i =='C':
            comp = comp +'G'
        else:
            print("Provide a valid DNA sequence")
            comp = ""
            break
    rev_comp = comp[::-1] # it gives the reverse of the string (here 'comp')
    return(rev_comp)
dna1 = input("Enter DNA Sequence:\n")
print('\n' + reverseComplement(dna1))