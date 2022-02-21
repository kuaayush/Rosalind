
#k is the pattern to match in sequence seq
def FrequentWordsBySorting(seq, k):
    FrequentPatterns = set()
    index = []
    a = len(seq)-k+1
    count = [1]*a
    print(count)
    for i in range(0, a):
        pattern = seq[i:i+k]
        index.append(PatternToNumber(pattern))
    index.sort()
    for i in range(1, a):
        if index[i] == index[i-1]:
            count[i] = count[i-1] +1
        maxCount = max(count)
    for i in range(0, a):
        if count[i] == maxCount:
            pattern = NumberToPattern(index[i], k)
            FrequentPatterns.add(pattern)
    return FrequentPatterns


def PatternToNumber(Pattern):
    if len(Pattern) == 0:
        return 0
    symbol = Pattern[-1]
    prefix = Pattern[:-1]
    return 4*PatternToNumber(prefix) + int(SymbolToNumber(symbol))
    
def SymbolToNumber(symbol):
    if symbol == 'A':
        return 0
    if symbol == 'C':
        return 1
    if symbol == 'G':
        return 2
    if symbol == 'T':
        return 3
    else:
        return "NONE"


def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = index // 4 #quotient
    rem = index % 4 #remainder
    symbol = NumberToSymbol(rem)
    PrefixPattern = NumberToPattern(prefixIndex, k-1)
    return PrefixPattern + symbol
    
def NumberToSymbol(index):
    if index == 0:
        return 'A'
    if index == 1:
        return 'C'
    if index == 2:
        return 'G'
    if index == 3:
        return 'T'
    else:
        return "NONE"


sequence = input("Enter the sequence: ")
kmer = int(input("Enter the k-mer value: "))
print(FrequentWordsBySorting(sequence, kmer))

