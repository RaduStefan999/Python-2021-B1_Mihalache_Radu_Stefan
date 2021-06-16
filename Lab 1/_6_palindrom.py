de_validat = int(input())

copie = de_validat

raspurnat = 0

while (copie != 0) :
    raspurnat = raspurnat * 10 + copie%10
    copie = copie//10

if (de_validat == raspurnat) :
    print("Palindrom")
else :
    print("Nu e Palindrom")