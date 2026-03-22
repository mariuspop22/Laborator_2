tari_risc = ["coreea de nord", "siria", "iran"]

numar_tranzactii = int(input("Cate tranzactii vrei sa introduci? "))

tranzactii_suspecte = 0
istoric = []

for i in range(numar_tranzactii):
    print(f"\nTranzactia {i + 1}")

    suma = float(input("Suma (RON): "))
    tara = input("Tara: ").lower()

    rezultat = "Sigura"

    if suma > 10000:
        rezultat = "Suspicioasa (suma mare)"
        tranzactii_suspecte += 1

    if tara in tari_risc:
        rezultat = "Frauduloasa (tara cu risc ridicat)"
        tranzactii_suspecte += 1

    istoric.append(1)

    if len(istoric) >= 3:
        rezultat = "Suspicioasa (activitate suspecta - prea multe tranzactii)"
        tranzactii_suspecte += 1

    print(f"→ {rezultat}")

print("\nProcesare finalizata.")

if tranzactii_suspecte >= 3:
    print(" 3 tranzactii suspecte detectate! Cont blocat.")
