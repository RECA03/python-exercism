global_song_passages = ("Ten", "Nine", "Eight", "Seven", "Six", "Five", 
"Four", "Three", "Two", "One")

def recite(start, take=1):
    bsp =  global_song_passages[-(start):]
    passages = start

    bottle_song = list()
    song = list()

    for i in range(take):
        if passages > 2:
            song = [f"{bsp[i]} green bottles hanging on the wall,",
                    f"{bsp[i]} green bottles hanging on the wall,",
                    "And if one green bottle should accidentally fall,",
                    f"There'll be {bsp[i+1].lower()} green bottles hanging on the wall."]
        elif passages == 2:
            song = [f"{bsp[i]} green bottles hanging on the wall,",
                    f"{bsp[i]} green bottles hanging on the wall,",
                    "And if one green bottle should accidentally fall,",
                    f"There'll be {bsp[i+1].lower()} green bottle hanging on the wall."]
        elif passages == 1:
            song = [f"{bsp[i]} green bottle hanging on the wall,",
                    f"{bsp[i]} green bottle hanging on the wall,",
                    "And if one green bottle should accidentally fall,",
                    "There'll be no green bottles hanging on the wall."]
        
        bottle_song.extend(song)

        if i != take-1:
            bottle_song.append("")

        passages-= 1

    print(bottle_song)
    return bottle_song

recite(10,2)