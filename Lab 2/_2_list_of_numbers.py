import math

def is_pirme (n) :
    if (n < 2) :
        return False
    elif (n == 2) :
        return True
    elif (n % 2 == 0) :
        return False
    else :
        for i in range(3, int(math.sqrt(n)), 2) :
            if (n % i == 0) :
                return False
    return True


def get_sir_prime (lista) :

    processed_list = []

    for nr in lista :
        if (is_pirme(nr)) :
            processed_list.append(nr)

    return processed_list



List = []

n = int(input())

for i in range(0, n) :
    a = int(input())
    List.append(a)


processed_list = get_sir_prime(List)

print(processed_list)