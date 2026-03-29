def normalizare(data):
    max_val = max(data)
    min_val = min(data)

    lista_normalizata = []

    for element in data:
        x = (element - min_val) / (max_val - min_val)
        lista_normalizata.append(x)
    return lista_normalizata
data = [10, 20, 30, 40, 50]
d = normalizare(data)
print(d)