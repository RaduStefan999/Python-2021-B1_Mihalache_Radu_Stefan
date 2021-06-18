sir = str(input())

nr = 0

sir = sir.lower()

for lit in "aeiou" :
    nr += sir.count(lit) 


"""
for lit in sir :
    if (lit in "aeiouAEIOU") :
            nr = nr + 1
"""


print(nr)