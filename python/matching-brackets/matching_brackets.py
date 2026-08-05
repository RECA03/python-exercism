def is_paired(input_string):

    #classify the opening and closing brackets
    left_e = "[{("
    right_e = "]})"

    #initialize a list to store the opening brackets
    verifier = []

    #filter the input string to only include the opening and closing brackets
    filtered_string = "".join(e for e in input_string if e in "[({])}")

    #if the length of the filtered string is odd, return False
    if len(filtered_string) % 2 != 0:
        return False

    #iterate through the filtered string
    for e in filtered_string:
        #if the current bracket is not an opening bracket and is the first bracket, return False
        if (e not in left_e) and (filtered_string.index(e) == 0):
            return False
        #if the current bracket is an opening bracket, add it to the list
        elif e in left_e:
            verifier.append(e)
        #if the current bracket is a closing bracket, check if it matches the last opening bracket in the list
        else:
            if left_e.index(verifier[-1]) == right_e.index(e):
                verifier.pop()
    
    #verify that all the opening brackets have been closed
    return len(verifier) == 0
        