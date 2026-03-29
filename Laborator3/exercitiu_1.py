def joaca():
    while True:
        print("\n--- Joc Rock-Paper-Scissors ---")

        jucator1 = input("Jucatorul 1 (piatra/hartie/foarfeca): ").lower()
        jucator2 = input("Jucatorul 2 (piatra/hartie/foarfeca): ").lower()

        if jucator1 == jucator2:
            print("Egalitate!")

        elif (jucator1 == "piatra" and jucator2 == "foarfeca") or \
                (jucator1 == "foarfeca" and jucator2 == "hartie") or \
                (jucator1 == "hartie" and jucator2 == "piatra"):
            print("🎉 Felicitari Jucatorul 1! Ai castigat!")

        elif (jucator2 == "piatra" and jucator1 == "foarfeca") or \
                (jucator2 == "foarfeca" and jucator1 == "hartie") or \
                (jucator2 == "hartie" and jucator1 == "piatra"):
            print("🎉 Felicitari Jucatorul 2! Ai castigat!")

        else:
            print("⚠️ Alegere invalida! Te rog alege: piatra, hartie sau foarfeca.")
            continue


joaca()