
codon_to_amino_acid = {"AUG": "Methionine", "UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine",
                        "UUG": "Leucine", "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
                        "UAU": "Tyrosine", "UAC": "Tyrosine", "UGU": "Cysteine", "UGC": "Cysteine",
                        "UGG": "Tryptophan", "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"}

def proteins(strand):
    
    protein_list = []
    for nuc_num in range(0,len(strand),3): # nuc_num = nucleotide index
        codon = strand[nuc_num:nuc_num+3]
        if codon_to_amino_acid[codon] == "STOP": #stop checking subsequent codons if STOP codon is found
            break
        protein_list.append(codon_to_amino_acid[codon])
    return protein_list
        