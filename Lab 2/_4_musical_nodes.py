def compose (note, mutari, pornire) :
    
    pozitie = pornire%(len(note))
    
    note_parcurse = []

    note_parcurse.append(note[pozitie])

    for mutare in mutari :
        pozitie = (pozitie + mutare)%(len(note))
        note_parcurse.append(note[pozitie])


    return note_parcurse

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
