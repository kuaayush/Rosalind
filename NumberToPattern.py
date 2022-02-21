

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


index = int(input("Enter the index: "))
k  = int(input("Enter the value of k: "))
print(NumberToPattern(index,k))


