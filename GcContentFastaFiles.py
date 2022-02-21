# -*- coding: utf-8 -*-
"""
Created on Thu May 20 11:22:19 2021

@author: Administrator

"""

# It retrieves sequence from fasta files,
# puts the sequence in 'seq', the indicators/names of sequence in 'name'
# and calculates the gc content of the sequence.

seq = ""
fasta_file = open('gc1.txt','r')

name_list = []
seq_list = []
for i in range(0,6):
    for line in fasta_file:
        if line[0] != '>':
            seq = seq + line.strip()
           
            else:
                 name = line[1:-1]
                 name_list.append(name)
                if line[0] == '>':
                    break
                seq_list.append(seq)


file_dict = dict()
for i in name_list:
    for j in seq_list:
        file_dict[i] = j


def gcContent(dna):
    g = dna.count("g") + dna.count("G")
    c = dna.count("c") + dna.count("C")
    gc_percent = (g+c)*100/len(dna)
    return gc_percent



print(seq_list)
print(name_list)
print(file_dict)
print(gcContent(seq))
print(seq)

# ----------------------------------------------------------------------------

# for comparing between two ore more set of sequences and print the sequence name with highes

# dict1 = dict()
# lista = [1,2,3,4,5]
# listb = ['A','B', 'C', 'D', 'E']
# for j in listb:
#     for i in lista:
#         dict1[i] = j

# print(dict1)







