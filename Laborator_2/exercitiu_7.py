cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
cuvinte_negative = ["urat", "prost", "groaznic", "dezamagitor"]

comentariu = input("Introdu un comentariu: ").lower()

pozitiv = False
negativ = False

for cuvant in cuvinte_pozitive:
    if cuvant in comentariu:
        pozitiv = True

for cuvant in cuvinte_negative:
    if cuvant in comentariu:
        negativ = True

if pozitiv:
    print("Comentariu pozitiv!")
elif negativ:
    print("Comentariu negativ!")
else:
    print("Comentariu neutru.")