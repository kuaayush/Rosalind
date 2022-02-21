

def FasterFrequentWords(sequence, k):
    FrequentPatterns = set()
    FrequencyArray = ComputingFrequencies(sequence, k)
    maxCount = max(FrequencyArray)
    for i in range(0, (4**k)):
        if FrequencyArray[i] == maxCount:
            pattern = NumberToPattern(i,k)
            FrequentPatterns.add(pattern)
    
    return FrequentPatterns

def ComputingFrequencies(sequence, k):
    FrequencyArray = []
    for i in range(0, (4**k)):
        FrequencyArray.append(0)
    for i in range(0, len(sequence) - k +1):
        pattern = sequence[i: i+k]
        j = PatternToNumber(pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1
    
    return FrequencyArray


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



seq = input("Enter the sequence: ")
k = int(input("Enter the value of k: "))

print(FasterFrequentWords(seq, k))

# positions = ComputingFrequencies(seq, k)
# for i in range(0, len(positions)):
#     print(positions[i], end = " ")


