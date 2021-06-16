def cmmdc (a, b) :
    aux = 0

    while (b != 0) :
        aux = a%b
        a = b
        b = aux
    
    return a

def divizori ():
    n = a = b = 0

    n = int(input())
    a = int(input())
    
    for i in range(1, n) :
        b = int(input())
        a = cmmdc(a, b)

    text = f"Cel mai mare divizor comun este {a}"

    print(text)
    #print("Cel mai mare divizor comun este %(a)d" % {"a": a})

    return


def main ():
    divizori()

    return 

main()