dna1 = "atgctggggact"

def gc(dna):
    g = dna.count("g") + dna.count("G")
    c = dna.count("c") + dna.count("C")
    gc_percent = (g+c)*100/len(dna)
    return gc_percent

print(dna1.upper())

print(gc(dna1))