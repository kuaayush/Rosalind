
from collections import defaultdict
import numpy as np

f = open('rosalind_cons.txt','r')
lists = defaultdict(str)
name = ''
for line in f:
    #if your line starts with a > then it is the name of the following sequence
    if line.startswith('>'):
        name = line[1:-1]
        continue #this means skips to the next line
    #This code is only executed if it is a sequence of bases and not a name.
    lists[name] += line.strip()

motifs = list(lists.values())


# print(lists,'\n')
# print(sequences)


A, T, G, C = [], [], [], []
Profile = {}
consensus = ""
 
for i in range(0, len(motifs[0])):
    countA, countG, countT, countC = 0,0,0,0
    for motif in motifs:
        if motif[i] == "A":
            countA += 1
        elif motif[i] == "G":
            countG += 1
        elif motif[i] == "T":
            countT += 1
        elif motif[i] == "C":
            countC += 1
                
    if countA >= max(countC, countG, countT):
        consensus += 'A'
    elif countG >= max(countC, countA, countT):
        consensus += 'G'
    elif countT >= max(countA, countG, countC):
        consensus += 'T'
    elif countC >= max(countA, countG, countT):
        consensus += 'C'
            
        # Profile['A'] = A.append(countA)
        # Profile['G'] = G.append(countG)
        # Profile['T'] = T.append(countT)
        # Profile['C'] = C.append(countC)
        
    A.append(countA)
    G.append(countG)
    T.append(countT)
    C.append(countC)
        
Profile['A'] = A
Profile['C'] = C
Profile['G'] = G
Profile['T'] = T
    
    
print(consensus)
print('A: ', end ='')
for a in range(0,len(A)):
      print(A[a], end = " ")

print('C: ', end ='')
for c in range(0,len(C)):
      print(C[c], end = " ")

print('G: ', end ='')
for g in range(0,len(G)):
      print(G[g], end = " ")
      
print('T: ', end ='')
for t in range(0,len(T)):
      print(T[t], end = " ")


#------------------------------------------------------------------------------------------

# from collections import defaultdict
# f = open('rosalind_cons_practice.txt','r')
# lists=defaultdict(str)
# name = ''
# for line in f:
#     #if your line starts with a > then it is the name of the following sequence
#     if line.startswith('>'):
#         name = line[1:-1]
#         continue #this means skips to the next line
#     #This code is only executed if it is a sequence of bases and not a name.
#     lists[name]+=line.strip()

# sequences = list(lists.values())

# # print(lists,'\n')
# # print(sequences)

# def ConsensusProfile(motifs):
#     A, T, G, C = [], [], [], []
#     Profile = {}
#     consensus = ""
    
#     for i in range(0, len(motifs[0])):
#         countA, countG, countT, countC = 0,0,0,0
#         for motif in motifs:
#             if motif[i] == "A":
#                 countA += 1
#             elif motif[i] == "G":
#                 countG += 1
#             elif motif[i] == "T":
#                 countT += 1
#             elif motif[i] == "C":
#                 countC += 1
                
#         if countA >= max(countC, countG, countT):
#             consensus += 'A'
#         elif countG >= max(countC, countA, countT):
#             consensus += 'G'
#         elif countT >= max(countA, countG, countC):
#             consensus += 'T'
#         elif countC >= max(countA, countG, countT):
#             consensus += 'C'
            
#         # Profile['A'] = A.append(countA)
#         # Profile['G'] = G.append(countG)
#         # Profile['T'] = T.append(countT)
#         # Profile['C'] = C.append(countC)
        
#         A.append(countA)
#         G.append(countG)
#         T.append(countT)
#         C.append(countC)
        
#     Profile['A'] = A
#     Profile['C'] = C
#     Profile['G'] = G
#     Profile['T'] = T
     
#     # return (consensus, Profile)
#     return Profile, len(Profile)

# print(ConsensusProfile(sequences))


# #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # n = len(sequences[1])
# # a = len(sequences)
# # M = np.array([[None]*n]*a)
# # for i in range(0,a):
# #     for j in range(0,n):
# #         M[i][j] = sequences[i][j]

# # print(M)
# #n = int(input("Enter the number of sequence:"))