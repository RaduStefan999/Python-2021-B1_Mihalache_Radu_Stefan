def arithmetic_function (y) :

    try :
        x = 5 / y
    except ArithmeticError : 
        print ("Problema aritmetica")
    except :
        print ("Alta problema")
    else :
        print ("A mers")

#arithmetic_function("da")

def impartire (x, y) :

    if y == 0 :
        raise Exception("Babuin")
    else :
        return (x / y)

try :
    impartire(200, 20)
except Exception as msg :
    print(msg)
except :
    print("Nu stiu bo$$ ce nu a mers")
else :
    print("A mers")