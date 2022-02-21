# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:33:42 2020

@author: Administrator
"""

# d = 'GTCGTGGACGAGAAGCACGACAGAAGACGCTAACTGCATGGAATCCGACAGCTTGCGTTAAGTGATTCGGAGGGCCTGCGCGCGGGTGATCCACCTTCAATCAAACGACATGAAAGGTCCAAAGCCAAAGGGATGTCACCATCCTGTCAGCGCCTTTCGCTATTCACACGCGGCAGCGGGCTCACAACACTGGCGAGAGACATGCGTTCGTCACTCGAAAGAAGCATATCACGACCAAATAAACTTCTTTTATGGATCTTTCTCGAATAGTTCTTGTTGACCTAGAATCTCGTCGCGATGCTGGGGGCAAAGGCCCTGAGACTGGACGAGTTTACTTTACGCACCATCACTTTCTGATCGGAGCTCGCCATAGCACCCGGATTTGCAGAGTGCTCGCTGAACGGTGAATCCTATTCTTACGCTAGCATATAAGTCGCAAACGTCCGCTGCCAATCTCAAGTGCGGTTGTACAGTGTCCCGATGCCCTCTCTTTGGGGGGAGACAAACCGTTAAGAGTCTGCCGGCTACAATGGCCCAGCAGACCTTCTAGATTTCGCATCCCGGGGTTGGGTACGGAACAACGGACTTACGTCCCCGTCACCTGCCTTTCGTAAAACCAGCCGTCATCGGAAACTTATGAGGGGGGTTAACTGTACGTGGTTACGGGCCGGGATCACATCTTGTCCGTTAATCGGGCTCTTTGGTTCTTCGCGGTATTAGCGCTGTTACTGTCAAATAGAACTGGTCGAGTCTGCTTCAACCGTATATGGAAACGTCCTTAATTATATGAGCGATATGCGACTATAA'

# print (len(d))
# a = d.count("A")
# t = d.count("T")
# g = d.count("G")
# c = d.count("C")
# print (a, c, g, t)

# # Counted A, T, G, C in 1000bp sequence sucessfully.

# ########################################################################################

# d = "ACACTCAAGAGAAACCGTCGCCCGTTGCGCCTCAGGTACCTAGGCCACATCAAAAAAGTCTCTGTTTAAGTGCTTCGAGAACGTCTTATGTTACGGTGGCAAACAAAGCAATCTTTAAATTGGGATTGGGATTAGGGTGGACTATTTCGCCTTCCGGACCTGTTGCGACATGAGGGATGGGAGATAGAAAGCGCGTAGATATACTGCATCATGGTAGTGAGTTAGGAACGTTAGACAATTGCCAATTGTTTGTATCCGAGCCGTGGTTGAGTTTGCATTTCCCTTAATCGTGAGCGGCGGGTTACAACTGGTGACCGTCGCAGTTGTACGGGGTGAAGAGAGTAGATCTTTGGAGCTATGCGGCTTTCGGTGTCAAATGTGAATCCCAGATCTTCTTCTGCATTTACAGTTCGTCAACTTAGAATTACGGCAGTTGGGCATCGTCGCTGATTCTTCCTTAGATGAACAGGGCTATCATGGAAGTCAGGCCGACACAACTTGTTAAATGCATACTCGTAAGCAGCCCAGGGGAGAAGTGACAGTCTACAAACTTAGTCCTTGATTTGATCTTACCTGTGCAGAGCCTCGGATAAATACAGAGCGAAATTCCCGATAACTGGGATCCCATACCGTATACTAATTCTTATCCTTAGCCCGCCGACTGGAAAAGTGCTCCTATCTGACGACGGAATCTTGTGGTAGGAGACTACGGGTTCACGCGACCTGGTTGCATTCGTGATGCGGCTTATGGTTATGTCGGCTTAAGCGGTATACTCAGTGGTAGAAAAGGCTCAATCTCTTTTTGGGGGAAGTTTAAAAGGTCGCCGCAGTAGGTTGTTCTATTACTCGTATTGGACTTCTGGGTTTGCTGGACCGGCCACACCGCGGCTTCCGCTGGTCCTGTTTGTAGTAGGACCAGGGCAATTGTCGCCACCGGGATGAT"
# t= d.count("T")

# r = d.replace("T", "U")
# u = r.count("U")

# print(d, t)
# print(r, u)

# # Replaced Ts by Us to create DNA from RNA; transcribed DNA sucessfully

# ###########################################################################


# s = "AAAACCCGGT"
# print(s)

# na = s.count("A")
# nt = s.count("T")
# nc = s.count("C")
# ng = s.count("G")

# cs1 = s.replace("A", "T", na)
# print(cs1)

# s2 = s
# cs2 = s2.replace("T", "A", nt)
# print(cs2)

# cs3 = s
# cs3.replace("C", "G", nc)
# print(cs3)

# cs4 = s
# cs4.replace("G", "C", ng)
# print(cs4)


# #Here, All I want to do is create a complementary strand. I have completed the 
# #replacings of A by T, G by C and vice versa. But the problem is that, when
# #I add all the replaces at once the code gets repeated, and when I replace the 
# #seperately, only the final replacement value is stored in 'cs'.
# #My guess is this problem can be solved by using certain attribute of 
# #srting datatype.

# =============================================================================
# =============================================================================

# trans = str.maketrans('ATGC', 'TACG')
# s = "AAAACCCGGT"
# print(s)
# cs = s.translate(trans)
# print(cs)

# =============================================================================
# =============================================================================

# cs = s.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
# print(cs.upper())
# This is just another trick to comolement the DNA. First, I replace A by small letter 
# 't', then in next step I make it capital using .upper() method.

# =============================================================================
# =============================================================================

# s = "AGGTCAAGAAGTCAATGCCTACCCCCCAGAGTATAGTCAGGCTCTACGCAGCGAGCGGTGTGGTATACTACGTTACTACAACTGACTATCTTGGCAAATTGTAACTTTGCCAAAGCTTGATAGGACTATTATGCTTAATAAAGAGCTATGTTTTTTCTGTCAAAGGAAAGTTGTCCGCAGTGTGAAGAGAAGAAAGGATGAGGCACCGCAGCTAATCAAGACGTACCATCGACTTATAGAGAAAAGCTGAGCGTCAGGTCAACCTACTGTTCATCCATGGCCTGGCTCCGAGGATGGTCCGCAGAGAGTAAAGCAAGCGGTTGTTGGCCGAAAATACAGTGTCCTCCGCTACGGGGCTGAGACGTCCTGTACCACAAGCACTCGTGTTACAATCGCAAAATTCGAGATGTTTGCCTACGCTAAACTTATTACTGTGATTTCGGAATGTCAAGAGTTCGCTGTTTGTTAGCATGTCAGATTTGTGACTCCCGGACTAACGGGACCGTTCCGGTTCTTTCCAGCGCTAGGTATAAGCAAACAGGGTAGTGCCGAATCGGATGCCTATGCGGTTATATACCGAGTTCCCTCGTACGAGCTCAAAGCGAAGAACTGCAGCGTTATCTTTTTGAGGTCCACGCTTTGGACTACCCTGGGGCTAGTACACGTACTGCCCGGCCGGGACGAGAGACATGCAGGGCCTATGCTGCATCCAACAGTGAATCAGCAGCTAAGTCACAGGTGCGGGCACTTCCATGCTACCAGAGCGGCAGGGAGCAGGAGCGACAATTTTAGCATTTAATCACCCCAACTAGCTACGC"

# def reverse_complement(s):
#     c = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
#     return ''.join([c[base] for base in s[::-1]])
# print (reverse_complement(s))

### This gives the solution, but I copied this code from Internet and not aware about
### the use of .join 

# =============================================================================
# =============================================================================

## The reverse complement of any DNA string has the same GC-content.
d = input()"CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

tot = len(d)
a = d.count("A")
t = d.count("T")
g = d.count("G")
c = d.count("C")

gc = g + c

gc_content = (gc/tot) * 100

print("The GC-content of the given sequence is :", gc_content, "%")
tm = (4*(g+c)) + (2*(a+t))
print("The melting temperature of given sequence is:", tm, "degree Celcius")

# =============================================================================
# =============================================================================


# seq = "ATGC"

# def gc_content (seq):
#     return round((seq.count("C") + seq.count("G"))/len (seq) * 100)

# print (gc_content(seq))
# print(len(seq))
# def gc_content_subsec(seq, k=5):
#     res = []
#     for i in range (0, len(seq) - k+1, k):
#         subseq = seq[i: i + k]
#         res.append(gc_content(subseq))
#         return res

# print (gc_content_subsec(seq, k=5))

# This code is not finished and not understood properly.


# Our for loop makes sure we scan the whole sequence and make k (5 by default) jumps, 
# to replicate the example above. We use string slicing to grab only the part of the 
# string we need, which, again, is of size k (our window). And we accumulator 
# results in a list res



