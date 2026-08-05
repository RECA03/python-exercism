def rotate(text, key):

    # dos alfabetos: uno para minúsculas y otro para mayúsculas
    alphabet_low = "abcdefghijklmnopqrstuvwxyz"
    alphabet_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #obtenemos lista de palabras
    word_list = text.split()

    for word in word_list:

        #obtenemos lista de caracteres
        char = list(word)
        index_char = enumerate(char)

        #recorremos lista de caracteres
        for i, ch in index_char:
            #verificamos si el caracter es una letra
            if ch.isalpha():
                #si el caracter es una letra minúscula
                if ch.islower():
                    #revisamos si la rotación supera la longitud del alfabeto
                    if alphabet_low.index(ch) + key >= len(alphabet_low):
                        char[i] = alphabet_low[alphabet_low.index(ch) + key -26]
                    else:
                        char[i] = alphabet_low[alphabet_low.index(ch) + key]
                else:
                    #realizamos lo mismo, pero para mayúsculas
                    if alphabet_up.index(ch) + key >= len(alphabet_up):
                        char[i] = alphabet_up[alphabet_up.index(ch) + key -26]
                    else:
                        char[i] = alphabet_up[alphabet_up.index(ch) + key]
        #unimos la lista de caracteres en una palabra
        word_list[word_list.index(word)]= "".join(char)
    
    #unimos la lista de palabras en una frase
    return " ".join(word_list)
        

