import re

def abbreviate(words):
    
    cleaned_text = re.sub(r"[^a-zA-Z\s-]","",words) # instead of \w\s, since _ is part of -w
    spaces_only_text = cleaned_text.replace("-"," ") #hyphens replaced with " " to keep associated words separate
    print(spaces_only_text)

    return "".join([word[0].upper() for word in spaces_only_text.split()])

abbreviate("The Road _Not_ Taken")