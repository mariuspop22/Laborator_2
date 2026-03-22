inventar = []

print("Ai intrat intr-o padure magica...")
directie = input("Alegi stanga sau dreapta? ")

if directie == "stanga":
    print("Ai mers pe o carare intunecata...")

    actiune = input("Apare un lup! Fugi sau lupti? ")

    if actiune == "lupti":
        print("Ai invins lupul!")
        inventar.append("blana de lup")
    else:
        print("Ai fugit si ai scapat!")

elif directie == "dreapta":
    print("Gasesti o comoara ascunsa!")
    inventar.append("aur")

    actiune = input("Vrei sa deschizi o cutie misterioasa? (da/nu) ")

    if actiune == "da":
        print("Ai gasit o sabie magica!")
        inventar.append("sabie magica")
    else:
        print("Ai plecat mai departe...")

else:
    print("Nu ai ales corect drumul!")

print("\n Inventarul tau:", inventar)

if "aur" in inventar and "sabie magica" in inventar:
    print("Esti un adevarat aventurier!")
elif len(inventar) == 0:
    print("Nu ai gasit nimic...")
else:
    print("Ai avut o aventura interesanta!")