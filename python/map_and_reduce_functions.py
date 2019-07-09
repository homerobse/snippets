# map
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

#convert the map into a list, for readability:
print(list(x))


def myfunc2(a, b):
  return a + b

x = map(myfunc2, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(list(x))


# reduce

product = 1
l = [1, 2, 3, 4]
for num in l:
    product = product * num

print(product)

## which is the same as 

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)

# filter

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
