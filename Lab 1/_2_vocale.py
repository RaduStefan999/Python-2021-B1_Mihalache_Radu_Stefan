sir = str(input())

nr = 0

for lit in sir :
    if (lit in "aeiouAEIOU") :
            nr = nr + 1

print(nr)