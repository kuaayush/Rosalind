# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:04:27 2021

@author: Administrator
"""


def dnaToRNA(dna):
    RNA = ""
    DNA = dna.upper()
    for i in DNA:
        if i =='A':
            RNA = RNA + 'U'
        elif i == 'T':
            RNA = RNA + 'A'
        elif i == 'G':
            RNA = RNA + 'C'
        elif i == 'C':
            RNA = RNA + 'G'
        else:
            print("\nENTER VALID DNA SEQUENCE!")
            RNA = ""
            break
    return RNA

def rnaToAminoAcid(RNA1):
    GeneticCode = { 
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T', 
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                  
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R', 
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A', 
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G', 
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S', 
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L', 
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_', 
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W', 
    }
    rna = RNA1
    # before translation, we must find the translation initiation site, i.e. AUG codon in mRNA
    for k in range(0,len(rna)-3+1,1):
        codon = rna [k:k+3]
        if codon == 'AUG':
            break
        
    # once AUG is found, translation begins.
    aacid = ""
    for j in range(k, len(rna)-3+1, 3):
        aacodon = rna[j:j+3]
        aa = GeneticCode[aacodon]
        if aa == '_':
            break
        else:
            aacid = aacid + aa
    return(aacid)

dna1 = input("Enter DNA sequence:")
rna1 = dnaToRNA(dna1)
print('\n'+ rna1)

amino_acid = rnaToAminoAcid(rna1)
print('\n'+ amino_acid)