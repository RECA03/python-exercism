def to_rna(dna_strand):
    if len(dna_strand) == 0:
        return ""
    
    nucleotides = list(dna_strand.upper())
    
    for i, n in enumerate(nucleotides):
        if n == "G":
            n = "C"
        elif n == "C":
            n = "G"
        elif n == "T":
            n = "A"
        elif n == "A":
            n = "U"
        nucleotides[i] = n
    
    return "".join(nucleotides)
