import random

numere_utilizator = []

print("Introdu 6 numere intre 1 si 49:")

while len(numere_utilizator) < 6:
    nr = int(input("Numar: "))

    if nr < 1 or nr > 49:
        print("Numar invalid!")
    elif nr in numere_utilizator:
        print("Numar deja ales!")
    else:
        numere_utilizator.append(nr)

numere_castigatoare = random.sample(range(1, 50), 6)

potriviri = set(numere_utilizator) & set(numere_castigatoare)

print("\nNumerele tale:", numere_utilizator)
print("Numere castigatoare:", numere_castigatoare)
print("Ai ghicit", len(potriviri), "numere!")

if len(potriviri) == 6:
    print("Jackpot!!!")
elif len(potriviri) >= 3:
    print("Ai castigat ceva!")
else:
    print("Mai incearca")