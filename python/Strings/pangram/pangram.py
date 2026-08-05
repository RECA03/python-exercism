def is_pangram(sentence):
    
    i = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_counter = 0
    sentence = sentence.lower()

    while i < 26:
        if alphabet[i] in sentence:
            letter_counter += 1
        i += 1
    
    if letter_counter < 26:
        return False
    else:
        return True
