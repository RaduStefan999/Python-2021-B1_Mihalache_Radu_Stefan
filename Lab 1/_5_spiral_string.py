M = ["firs", "n_lt", "oba_", "htyp"]

n = 4

array_of_strings = []

for rama in range(0, int(n/2) ) :
    for i in range(rama, n - rama) :
        array_of_strings.append(M[rama][i])
    for i in range(rama + 1, n - rama) :
        array_of_strings.append(M[i][n - rama - 1])
    for i in range(n - rama - 2, rama - 1, -1) :
        array_of_strings.append(M[n - rama - 1][i])
    for i in range(n - rama - 2, rama, -1) :
        array_of_strings.append(M[i][rama])

resault_string = ''.join(array_of_strings)

print(resault_string)