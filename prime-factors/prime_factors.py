def factors(value):
    
    factor_list = []
    factor = 2
    if value <= 1:
        return factor_list
    while factor <= value: #max possible factor: the reamining value itself
        if value%factor == 0:
            value /= factor
            factor_list.append(factor) #only append factor if the value is divisible by it
        else:
            factor += 1

    return factor_list