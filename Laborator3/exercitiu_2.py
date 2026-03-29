def genereaza_factura(nume_client, **produse):
    print(f"Factura pentru: {nume_client}")
    print("-" * 30)

    total = 0

    for produs, pret in produse.items():
        print(f"{produs}: {pret} lei")
        total += pret

    print("-" * 30)
    print(f"Total: {total} lei")

genereaza_factura(
        "Ana Popescu",
        paine=5,
        lapte=7,
        oua=10
    )