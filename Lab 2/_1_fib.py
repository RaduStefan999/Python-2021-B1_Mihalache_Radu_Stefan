def fibonacci(n) :
    fib_list = [1, 1]

    for index in range(2, n) :
        fib_list.append(fib_list[index - 1] + fib_list[index - 2])
    
    return fib_list

Lista = fibonacci(10)

print (Lista)