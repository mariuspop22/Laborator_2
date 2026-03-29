even_numbers = [x for x in range(0, 101) if x % 2 == 0]
print(even_numbers)
cubes = [x**3 for x in range(1, 11)]
print(cubes)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = [x for x in list1 if x in list2]
print(common)
