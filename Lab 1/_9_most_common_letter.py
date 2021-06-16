sir = input()

hash_table = {}

maxim = 0
lit_maxim = None

for lit in sir :
    
    lit = lit.lower()

    if (lit != ' ') :
        if (lit in hash_table.keys()) :
            hash_table[lit] = hash_table[lit]  + 1
        else :
            hash_table[lit] = 1

        if (hash_table[lit] > maxim) : 
            maxim = hash_table[lit]
            lit_maxim = lit

print(lit_maxim)
