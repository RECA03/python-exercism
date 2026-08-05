def proverb(*args, qualifier=None):
    words = args

    if len(words) == 0: # return empty list if no words were given
        return []

    proverb_verses = []
    for i in range(len(words)-1): # loop to obtain all verses except for the final one
        verse = f"For want of a {words[i]} the {words[i+1]} was lost."
        proverb_verses.append(verse)
    
    qual_word = " " if qualifier==None else " "+qualifier+" " # add qualifier if given
    final_verse = f"And all for the want of a{qual_word}{words[0]}." # generate final verse
    proverb_verses.append(final_verse)

    return proverb_verses