sir = input()

index = 0

nr = 0

while (sir[index].isdigit() == False and index < len(sir)) :
    index = index + 1

while (sir[index].isdigit() == True and index < len(sir)) :
    nr = nr*10 + int(sir[index])
    index = index + 1

print(nr)