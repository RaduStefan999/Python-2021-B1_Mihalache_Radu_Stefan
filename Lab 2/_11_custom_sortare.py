lsta_de_tupluri = [('abc', 'bcd'), ('abc', 'zza')] 

lsta_de_tupluri_sortate = sorted(lsta_de_tupluri, key = lambda tuplu: ord(tuplu[1][2]))

print(lsta_de_tupluri_sortate)