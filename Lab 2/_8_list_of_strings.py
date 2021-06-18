def list_of_divisible_strings (x = 1, list_strings = [], div_flag = True) :
    divisible_strings = []

    for string in list_strings :

        current_divisible_strings = []

        for lit in string :
            
            if (ord(lit) % x == 0) and div_flag == True :
                current_divisible_strings.append(lit)

            if (ord(lit) % x != 0) and div_flag == False :
                current_divisible_strings.append(lit)
        
        divisible_strings.append(current_divisible_strings)

    return divisible_strings

print(list_of_divisible_strings(2,  ["test", "hello", "lab002"], False))