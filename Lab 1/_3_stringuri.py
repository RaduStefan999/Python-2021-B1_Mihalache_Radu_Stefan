sir_A = str(input())
sir_B = str(input())

#print(sir_A.index("||*"))

nr = 0

nr = sir_A.count(sir_B)

"""
while (sir_B in sir_A) :
    sir_A = sir_A.split(sir_B, 1)[1]
    nr = nr + 1
"""
print(nr)

#print("||" in (sir_A.split("||")[-1]))