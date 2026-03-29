preturi = [100, None, 200, 50, None, 80]
fara_none = list(filter(lambda x: x is not None, preturi))
preturi_reduse = list(map(lambda x: x * 0.9, fara_none))

print(preturi_reduse)