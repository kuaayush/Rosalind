

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

seq = input("Enter the sequence:")
print(PatternToNumber(seq))


        