squares = {x: x**2 for x in range(1, 11)}
print(squares)

text = "banana"

freq = {c: text.count(c) for c in text}
print(freq)

divisors = {x: [d for d in range(1, x+1) if x % d == 0] for x in range(1, 11)}
print(divisors)