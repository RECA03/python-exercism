alphabet = "abcdefghijklmnopqrstuvwxyz"

#Applies the Atbash cipher key to the characters in the list
def atbasher(char_list):
    for i, char in enumerate(char_list):
        if char.isalpha():
            char = alphabet[-(alphabet.index(char) + 1)]

        char_list[i] = char
    
    return char_list

def encode(plain_text):
    #"Atbash" the characters (only alpha or digits) and save them on a list
    char_list = atbasher([c.lower() for c in plain_text if (c.isalpha() or c.isdigit())])
    
    ciphered_list = [] #here the resulting cipher will be saved in list form
    i = 0

    while i < len(char_list):
        if i + 5 < len(char_list): #adds space every five characters
            ciphered_list.append("".join(char_list[i:i+5]))
            ciphered_list.append(" ")
        else: #only adds the final characters, without an extra space
            ciphered_list.append("".join(char_list[i:]))
        
        i += 5 
    
    return "".join(ciphered_list)

def decode(ciphered_text):
    #remove spaces between characters, and apply atbash cipher key
    char_list = atbasher([char.lower() for char in ciphered_text if char != " "])

    return "".join(char_list)
