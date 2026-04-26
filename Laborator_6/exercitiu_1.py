import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#exercitiul 1
iris = load_iris()
numar_exemple, dimensiune_caracteristici = iris.data.shape

print("--- 1.2. INFORMAȚII SET DE DATE ---")
print(f"Numărul de exemple (rânduri): {numar_exemple}")
print(f"Dimensiunea caracteristicilor (coloane): {dimensiune_caracteristici}")

print("\nDenumirile coloanelor (atributelor):")

for atribut in iris.feature_names:
    print(f" - {atribut}")

print("\nNumele claselor:")
for clasa in iris.target_names:
    print(f" - {clasa}")

#exercitiul 2

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.20,
    random_state=42
)

print("\n--- 2.2. FORMA SUBSETURILOR ---")
print(f"Date de antrenament (X_train): {X_train.shape}")
print(f"Etichete de antrenament (y_train): {y_train.shape}")
print(f"Date de testare (X_test): {X_test.shape}")
print(f"Etichete de testare (y_test): {y_test.shape}")

#exercitul 3
print("\n--- 3.2. COMPARAȚIE SCALARE ---")
print("Primele 3 exemple ÎNAINTE de scalare:")

print(X_train[:3])
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

print("\nPrimele 3 exemple DUPĂ scalare:")
print(X_train_scaled[:3])

# EXERCIȚIUL 4
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)
acuratete = accuracy_score(y_test, y_pred)

print("\n--- 4.2. REZULTAT EXAMEN MODEL KNN ---")
print(f"Acuratețea modelului: {acuratete * 100}%")

# EXERCIȚIUL 5

k_interval = range(1, 16)
acurateti = []

for k in k_interval:
    model_curent = KNeighborsClassifier(n_neighbors=k)
    model_curent.fit(X_train_scaled, y_train)
    predictii_curente = model_curent.predict(X_test_scaled)
    acurateti.append(accuracy_score(y_test, predictii_curente))

plt.figure(figsize=(8, 5))
plt.plot(k_interval, acurateti, marker='o', color='b', linestyle='dashed')
plt.title('5.2. Acuratețea modelului KNN în funcție de k')
plt.xlabel('Valoarea lui k (Numărul de vecini)')
plt.ylabel('Acuratețe')
plt.xticks(k_interval)
plt.grid(True)
plt.show()

# EXERCIȚIUL 6

print("\n--- 6.1. MATRICEA DE CONFUZIE ---")
print(confusion_matrix(y_test, y_pred))

print("\n--- 6.2. RAPORT DE CLASIFICARE ---")
print(classification_report(y_test, y_pred, target_names=iris.target_names))


# EXERCIȚIUL 7
plt.figure(figsize=(8, 5))
for i, nume_clasa in enumerate(iris.target_names):
    plt.scatter(
        iris.data[iris.target == i, 2],
        iris.data[iris.target == i, 3],
        label=nume_clasa
    )
plt.title('7.1. Distribuția florilor: Lungime vs Lățime Petală')
plt.xlabel('Lungime petală (cm)')
plt.ylabel('Lățime petală (cm)')
plt.legend()
plt.show()

# 7.2
print("Introdu valorile pentru o floare găsită de tine:")
try:
    sl = float(input("Lungime sepală : "))
    sw = float(input("Lățime sepală : "))
    pl = float(input("Lungime petală : "))
    pw = float(input("Lățime petală : "))


    floare_noua = np.array([[sl, sw, pl, pw]])
    floare_noua_scalata = scaler.transform(floare_noua)

    rezultat_predictie = knn.predict(floare_noua_scalata)
    nume_specie_prezisa = iris.target_names[rezultat_predictie[0]]

    print(f"\n=> 🤖 Modelul KNN spune că floarea ta este din specia: **{nume_specie_prezisa.upper()}**!")
except ValueError:
    print("Ai introdus litere în loc de numere! Rulează din nou programul.")