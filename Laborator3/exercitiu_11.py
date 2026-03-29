even_set = {x for x in range(0, 20) if x % 2 == 0}
print(even_set)
text = "programare"
letters = {c for c in text}
print(letters)

text = "Ana are mere rosii si pere galbene"
words = {word for word in text.split() if len(word) >= 5}
print(words)