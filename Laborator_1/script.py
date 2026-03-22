type(1)   # int
type(-10) # int
type(0)   # int
type(0.0) # float
type(2.2) # float
type(4E2) # float - 4*10 to the power of 2

# Arithmetic
10 + 3
10 - 3
10 * 3
10 ** 3
10 / 3
10 // 3
10 % 3


pow(5, 2)
abs(-50)
round(5.46)
round(5.468, 2)
bin(512)
hex(512)


age = input("How old are you?")
age = int(age)
pi = input("What is the value of pi?")
pi = float(pi)






type('Helllooooooo')

'I\'m thirsty'
"I'm thirsty"
"\n"
"\t"

'Hey you!'[4]
name = 'John Doe'
print(name[2])
print(name[:])
print(name[1:])
print(name[:1])
print(name[-1])
print(name[::1])
print(name[::-1])
print(name[0:7:2])


'Hi there ' + 'Timmy'
print('*'*10)


len('turtle')


'  I am alone '.strip()
'On an island'.strip('d')
'but life is good!'.split()
'Help me'.replace('me', 'you')
'Need to make fire'.startswith('Need')
'and cook rice'.endswith('rice')
'bye bye'.index('e')
'still there?'.upper()
'HELLO?!'.lower()
'ok, I am done.'.capitalize()
'oh hi there'.find('i')
'oh hi there'.count('e')


name1 = 'Andrei'
name2 = 'Sunny'
print(f'Hello there {name1} and {name2}')
print('Hello there {} and {}'.format(name1, name2))
print('Hello there %s and %s' %(name1, name2))

word = 'reviver'
p = bool(word.find(word[::-1]) + 1)
print(p)


bool(True)
bool(False)


print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))


my_list = [1, 2, '3', True]

len(my_list)
my_list.index('3')
my_list.count(2)

my_list[3]
my_list[1:]
my_list[:1]
my_list[-1]
my_list[::1]
my_list[::-1]
my_list[0:3:2]

# Add to List
my_list * 2
my_list + [100]
my_list.append(100)

my_list.extend([100, 200])
my_list.insert(2, '!!!')

' '.join(['Hello', 'There'])

# Copy a List
basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]



# Remove from List
[1, 2, 3].pop()
[1, 2, 3].pop(1)
[1, 2, 3].remove(2)
[1, 2, 3].clear()
del [1, 2, 3][0]

# Ordering
[1, 2, 5, 3].sort()
[1, 2, 5, 3].sort(reverse=True)
[1, 2, 5, 3].reverse()
sorted([1, 2, 5, 3])
list(reversed([1, 2, 5, 3]))


# Useful operations
1 in [1, 2, 5, 3]
min([1, 2, 3, 4, 5])
max([1, 2, 3, 4, 5])
sum([1, 2, 3, 4, 5])

# Get First and Last element of a list
mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
first, *x, last = mList

print(first)
print(last)

# Read line of a file into a list
with open("../myfile.txt") as f:
    lines = [line.strip() for line in f]

    my_dict = {'name': 'John Doe', 'age': 25, 'magic_power': False}

    my_dict['name']
    len(my_dict)
    list(my_dict.keys())
    list(my_dict.values())
    list(my_dict.items())

    my_dict[
        'favourite_snack'] = 'Grapes'
    my_dict.get('age')
    my_dict.get('ages', 0)


    del my_dict['name']
    my_dict.pop('name', None)

my_tuple = ('apple', 'grapes', 'mango', 'grapes')
apple, grapes, mango, grapes = my_tuple
len(my_tuple)
my_tuple[2]
my_tuple[-1]

# Immutability
#my_tuple[1] = 'donuts'
#my_tuple.append('candy')



my_set = set()
my_set.add(1)
my_set.add(100)
my_set.add(100)

new_list = [1, 2, 3, 3, 3, 4, 4, 5, 6, 1]
set(new_list)

my_set.remove(100)
my_set.discard(100)
my_set.clear()
new_set = {1, 2, 3}.copy()

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)
set6 = set1.symmetric_difference(set2)

set1.issubset(set2)
set1.issuperset(set2)
set1.isdisjoint(set2)

type(None)
a=None
