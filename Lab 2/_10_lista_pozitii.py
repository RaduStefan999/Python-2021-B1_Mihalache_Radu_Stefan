def split_in_touple_list (*lists) :

    maxim = 0

    for list in lists :
        if (len(list) > maxim) : maxim = len(list)

    split_list_in_touples = []

    for column in range(0, maxim) :

        lista_poz_n = []

        for row in range(0, len(lists)) :
            if (column < len(lists[row])) : 
                lista_poz_n.append(lists[row][column])
            else :
                lista_poz_n.append(None)


        split_list_in_touples.append(tuple(lista_poz_n))

    return split_list_in_touples


print(split_in_touple_list([1,2,3], [5,6,7], ["a", "b", "c"]))