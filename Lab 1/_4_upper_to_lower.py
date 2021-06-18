for_converting = input()

array_of_strings = []

index  = 0

while (index < len(for_converting) - 1) :
    
    if (for_converting[index + 1].isupper()) :
        
        array_of_strings.append(for_converting[:index + 1].lower())
        array_of_strings.append("_")
        
        for_converting = for_converting[index+1:]
        index = 0
    else :
        index = index + 1

array_of_strings.append(for_converting.lower())

converted = ''.join(array_of_strings)

print(converted)

#trebuie sa o refac