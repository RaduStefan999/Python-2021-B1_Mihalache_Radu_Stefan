from typing import List


def operatii(A, B) :
    intersectie = list(filter(lambda el : el in B, A))

    reuniune = list( A + list(filter(lambda el: (el in A) == False, B)) )
    
    scadere_A_B = list(filter(lambda el : (el in B) == False, A))
    
    scadere_B_A = list(filter(lambda el : (el in A) == False, B))

    return(intersectie, reuniune, scadere_A_B, scadere_B_A)


a = ["do", "re", "mi", "fa"]
b = ["mi", "fa", "sol", "la", "si", "do"]

intersectie, reuniune, scadere_A_B, scadere_B_A = operatii(a, b)

print(intersectie)
print(reuniune)
print(scadere_A_B)
print(scadere_B_A)