def translate(text):
    
    if len(text.split()) == 1:
        
        text_bool = [letter in "aeiou" for letter in text]

        rule_1 = (text[0] in "aeiou") or (text[:2] == "xr") or (text[:2] == "yt") #Tambien se podria haber usado metodo startswith

        if rule_1:
            text += "ay"

        #For rule 3
        elif ("qu" in text) and (sum(text_bool[0:text.index("qu")]) == 0):
            if text_bool.index(True) >= 0:
                text += text[0:(text.index("qu")+2)]
                text += "ay"
                text = text[(text.index("u")+1):]

        #For rule 2
        elif True in text_bool and text_bool.index(True) > 0:
            text += text[:text_bool.index(True)] #Esto funciona porque index() busca el primero de los elementos repetidos en la lista
            text += "ay"
            text = text[text_bool.index(True):]
        
        #For rule 4 
        elif "y" in text:
            if (sum([cons for cons in text_bool[0:text.index("y")]]) == 0):
                text += text[:text.index("y")]
                text += "ay"
                text = text[text.index("y"):]
    
    else:
        text = text.split()

        for i in text:

            word = text[text.index(i)]
            word_bool = [letter in "aeiou" for letter in word]

            rule_1 = (word[0] in "aeiou") or (word[:2] == "xr") or (word[:2] == "yt") #Tambien se podria haber usado metodo startswith

            if rule_1:
                word += "ay"

            #For rule 3
            elif ("qu" in word) and (sum(word_bool[0:word.index("qu")]) == 0):
                if word_bool.index(True) >= 0:
                    word += word[0:(word.index("qu")+2)]
                    word += "ay"
                    word = word[(word.index("u")+1):]

            #For rule 2
            elif True in word_bool and word_bool.index(True) > 0:
                word += word[:word_bool.index(True)] #Esto funciona porque index() busca el primero de los elementos repetidos en la lista
                word += "ay"
                word = word[word_bool.index(True):]
            
            #For rule 4 
            elif "y" in word:
                if (sum([cons for cons in text_bool[0:word.index("y")]]) == 0):
                    word += word[:word.index("y")]
                    word += "ay"
                    word = word[word.index("y"):]
            
            text[text.index(i)] = word
        
        text = " ".join(text)

    return text