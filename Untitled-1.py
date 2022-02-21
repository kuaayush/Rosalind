# AllPattern_dict = {'GTCTAAC': 25, 'TCTAACG': 25, 'CTAACGA': 5}
# x=[]
# y = []
# for key, value in AllPattern_dict.items():
#     value = value+1
#     x.append(key)
#     y.append(value)
#     for i in range(len(y)):
#         AllPattern_dict.update({key : y[i]})

# print(AllPattern_dict)
# print(x)
# print(y)
# print(x[1])



def PatternFind(string, pattern, d):
    a = len(string) - len(pattern) +1
    count = 0
    b = len(pattern) - d
    for i in range(0,a,1):
        m = 0
        for j in range(0, len(pattern), 1):
            if pattern[j] == string[i]:
                m = m+1
            i = i+1
        if b <= m <= len(pattern):
            count = count +1
        
    return count
    
def FrequentWords(string, kmer,d):
    a = len(string) - kmer +1
    Frequentword = set()
    Counts = [None] * a
    for i in range(0, a, 1):
        Pattern = string[i:i+kmer]
        Counts[i] = PatternFind(string, Pattern,d)
    
    maxCount = max(Counts)
    print(maxCount)
    for i in range(0,a,1):
        if Counts[i] == maxCount:
            adds = ''.join(string[i: i+kmer])
            Frequentword.add(adds)
    return Frequentword
   
    
DNA = input("Please enter the string in all capital")
kmer = int(input("Please enter the kmer"))
string = list(DNA)
d = int(input("Enter the number of mismatches"))

print(FrequentWords(string, kmer, d))


















# seq = input("Enter the DNA String:\n")
# kmer = int(input("Enter the length of pattern:"))
# # pattern = input("Enter the pattern:\n")
# d = int(input("Enter the most mismatches allowed: "))

# def HammingDistance(seq1, seq2):
#     hamdist = 0
#     for i in range (0, len(seq1)):
#         if seq1[i] != seq2[i]:
#             hamdist = hamdist + 1
    
#     return hamdist

# def ApproxPatternCount(sequence, Pattern, d):
#     count = 0
#     for i in range(0,len(sequence)-len(Pattern) + 1):
#         Pattern1 = seq[i: i+len(Pattern)]
#         if HammingDistance(Pattern, Pattern1) <= d:
#             count = count+1
#     return count

# result = {}
# result.update(AllPattern_dict)
# for i in range(0, len(x)):
#     result[x[i]] = ApproxPatternCount(seq, x[i], d)



# itemMaxValue = max(result.items(), key=lambda x: x[1])
# listOfKeys = list()
# for key, value in result.items():
#     if value == itemMaxValue[1]:
#         listOfKeys.append(key)

# print("\n")
# print("The length of entered sequence is:", len(seq))
# print("The result for Approximate Pattern Count is: ",result )