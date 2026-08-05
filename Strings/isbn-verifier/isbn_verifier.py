def is_valid(isbn):

    if "-" in isbn:
        digits = list("".join(isbn.split("-")))
    else:
        digits = list(isbn)
    
    if len(digits) != 10 or (digits[-1] != "X" and  not digits[-1].isdigit()) or sum([d.isdigit() for d in digits[0:9]]) < 9:
        return False
    elif digits[-1] == "X":
        digits[-1] = 10

    return (sum([int(d)*(10-i) for i, d in enumerate(digits)]) % 11) == 0 #enumerate gives you a list of tuples (index, element)
        
    

