

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

seq = input("Enter the sequence: ")
k = int(input("Enter the value of k: "))

positions = ComputingFrequencies(seq, k)
for i in range(0, len(positions)):
    print(positions[i], end = " ")


