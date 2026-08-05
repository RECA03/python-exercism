def is_isogram(string):
    
    letters = [ch for ch in string.lower() if ch.isalpha()]

    return len(letters) == len(set(letters)) #set removes duplicates from an iterable

