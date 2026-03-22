import random
numar_secret= random.randint(1,50)
incercari=0
print("Am ales un nr. intre 1 si 50.")

while True:
    ghicire = int(input("Ghiceste nr. (1-50):"))
    incercari=incercari+1
    if ghicire < numar_secret:
        print("Nr. este mai mare")
    elif ghicire > numar_secret:
        print("Nr. este mai mic")
    elif ghicire == numar_secret:
        print("Felicitari!Ai castigat.")
        break