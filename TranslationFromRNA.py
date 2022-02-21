# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:11:42 2020

@author: Administrator
"""

  # r = input("Enter RNA sequence: ")
  # def prot(rna):
  #   for i in range(3, (5*len(rna))//4+1, 4):
  #     rna=rna[:i]+','+rna[i:]
  #   rnaList=rna.split(',')
  #   bases=['U','C','A','G']
  #   codons = [a+b+c for a in bases for b in bases for c in bases]
  #   amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
  #   codon_table = dict(zip(codons, amino_acids))
  #   peptide=[]
  #   for i in range (len (rnaList)):
  #     if codon_table[rnaList[i]]=='*':
  #       break
  #     peptide+=[codon_table[rnaList[i]]]
  #   output=''
  #   for i in peptide:
  #     output+=str(i)
  #   return output
  # print ("The translation of provided RNA sequence gives following protein: \n", prot(r))



def fastaRnaToAminoAcid(RNA1):
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
    # before translation, we must find the translation initiation site, 
    # i.e. AUG codon in mRNA
    for k in range(0,len(rna)-3+1,1):
        codon = rna [k:k+3]
        if codon == 'AUG':
            break
        
    # once AUG is found, translation begins.
    aacid = ""
    for j in range(k, len(rna)-3+1, 3):
        aacodon = rna[j:j+3]
        aa = GeneticCode[aacodon]
        aacid = aacid + aa
    return(aacid)

# seq = ""
# for line in open('rosalind_prot.txt'):
#     if line[0] != '>':
#         seq = seq +line.strip()

seq = input("Enter the sequence:")


amino_acid = fastaRnaToAminoAcid(seq)
print('\nThe translated protein of provided DNA sequence is:\n'+'\n'+ amino_acid)
