alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def rows(letter):

    diamond_letters = alphabet[:alphabet.index(letter)+1]
    diamond_slice = [" " for _ in range(len(diamond_letters)*2-1)]

    diamond_rows = []
    for i,l in enumerate(diamond_letters):
        new_slice = diamond_slice.copy()
        if l == "A":
            new_slice[len(diamond_letters)-1] = l
            diamond_rows.append("".join(new_slice))
            continue
        
        position = i
        blanks = len(diamond_letters)-1-position
        new_slice[blanks], new_slice[-(blanks)-1] = l, l
        diamond_rows.append("".join(new_slice))
    
    half = diamond_rows.copy()
    half.reverse()
    diamond_rows.extend(half[1:])

    return diamond_rows

print(rows("B"))