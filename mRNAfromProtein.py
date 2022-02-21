
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
    rna0 = RNA1
    rna1 = RNA1 - RNA1[0]
    rna2 = RNA1 - RNA1[0] - RNA1[1]
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
    

    # for k in range(1,len(rna)-3+1,1):
    #     codon = rna [k:k+3]
    #     if codon == 'AUG':
    #         break
        
    # # once AUG is found, translation begins.
    # aacid = ""
    # for j in range(k, len(rna)-3+1, 3):
    #     aacodon = rna[j:j+3]
    #     aa = GeneticCode[aacodon]
    #     if aa == '_':
    #         break
    #     else:
    #         aacid = aacid + aa
   

dna1 = input("Enter DNA sequence:")
rna1 = dnaToRNA(dna1)
print('\n'+ rna1)

amino_acid = rnaToAminoAcid(rna1)
print('\n', amino_acid)


# aacid = []
#     # before translation, we must find the translation initiation site, i.e. AUG codon in mRNA
#     for k0 in range(0,len(rna)-3+1,1):
#         codon0 = rna [k0:k0+3]
#         if codon0 == 'AUG':
#             break
        
#     # once AUG is found, translation begins.
#     aacid0 = ""
#     for j0 in range(k0, len(rna)-3+1, 3):
#         aacodon0 = rna[j0:j0+3]
#         aa0 = GeneticCode[aacodon0]
#         if aa0 == '_':
#             break
#         else:
#             aacid0 = aacid0 + aa0
#     aacid.append(aacid0)
# # ---------------------------------------------------------------------------------------------------------------------------
#     for k1 in range(1,len(rna)-3+1-1,1):
#             codon1 = rna [k1:k1+3]
#             if codon1 == 'AUG':
#                 break
            
#         # once AUG is found, translation begins.
#     aacid1 = ""
#     for j1 in range(k1, len(rna)-3+1-1, 3):
#         aacodon1 = rna[j1:j1+3]
#         aa1 = GeneticCode[aacodon1]
#         if aa1 == '_':
#             break
#         else:
#             aacid1 = aacid1 + aa1
#     aacid.append(aacid1)
#  # --------------------------------------------------------------------------------------------------------------------------- 
 
#     for k2 in range(2,len(rna)-3+1-2,1):
#             codon2 = rna [k2:k2+3]
#             if codon2 == 'AUG':
#                 break
            
#         # once AUG is found, translation begins.
#     aacid2 = ""
#     for j2 in range(k2, len(rna)-3+1-1, 3):
#         aacodon2 = rna[j2:j2+3]
#         aa2 = GeneticCode[aacodon2]
#         if aa2 == '_':
#             break
#         else:
#             aacid2 = aacid2 + aa2
#     aacid.append(aacid2)
# #  -------------------------------------------------------------------------------------------------------------------------------