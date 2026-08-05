def distance(strand_a, strand_b):

    #raise value error in case strands aren't of equal length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    #compare the strands
    hamming_distance = 0
    for _ in range(len(strand_a)):
        if strand_a[_] == strand_b[_]:
            continue
        hamming_distance += 1
    
    return hamming_distance