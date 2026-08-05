import re
from itertools import groupby

def decode(string):
    
    pattern = r"(\d*)(.)" 
    decoded_string = ""
    for match in re.findall(pattern,string):
        mult, char = match
        if mult:
            decoded_string += char*int(mult)
        else:
            decoded_string += char
    return decoded_string
    # return "".join(char*int(mult) 
        # if mult else char 
        # for mult, char in re.findall(pattern, string))

def encode(string):

    if not string:
        return ""

    encoded_chars = []
    for char, group in groupby(string):
        count = sum(1 for _ in group) # group is iter(['A','A',...])
        count_str = str(count) if count > 1 else ""
        encoded_chars.append(f"{count_str}{char}")

    return "".join(encoded_chars)


decode("K3Fg7D")