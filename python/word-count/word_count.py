import re

def count_words(sentence):

    pattern = r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)*" 
    regexed_sentence = re.findall(pattern, sentence.lower())
    
    return {word: regexed_sentence.count(word) for word in set(regexed_sentence)}