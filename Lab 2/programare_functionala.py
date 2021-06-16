import math


def enumerate_function () :

    for index, nume in enumerate(["Radu", "Stefan", "Mihalache"]) :
        print("%8s %d"%(nume, index))

    #range(1, 8)
    #enumerate


def patrate_function () :
    lista = [i**2 for i in range(1, 10)]
    print(lista)


def modulo_sapte () :
    lista = [i for i in range(1, 100) if (i%7 == 0)]
    print(lista)


def prime_function () :
    lista = [x for x in range(2, 100) 
                if len(
                    [div for div in range(2, int(math.sqrt(x)) + 1) if x%div==0 ]
                ) == 0 ]

    print(lista)

def multipli_noua_unusprezece() :
    lista = [[a, b] for a in range(1, 30) if a%11 == 0 for b in range(1, 30) if b%13 == 0]
    print(lista)

def lambda_function () :
    adunare = lambda x, y : x+y
    print(adunare(10, 19))

def main () :
    lambda_function()

main ()