sir = input()
dictionar = {}

for lit in sir :
    if (lit in dictionar) == False :
        dictionar[lit] = 1
    else :
        dictionar[lit] = dictionar[lit] + 1

print(dictionar)