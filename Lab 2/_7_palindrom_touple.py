def is_palindrom (number) :
    copie = number
    dup = 0

    while (copie != 0) :
        dup = dup*10 + copie%10
        copie = copie//10

    return (number == dup)

def touple_from_palindrom (palindroame) :
    
    palindr = []
    
    maxim = 0

    for x in palindroame :
        if (is_palindrom(x) == True) :
            
            if (len(palindr) == 0) :
                palindr.append(x)
            
            if (x > maxim) :
                maxim = x

    palindr.append(maxim)

    return tuple(palindr)

print(touple_from_palindrom([10, 470, 99, 1000000, 707, 123321, 7447, 9999999991]))