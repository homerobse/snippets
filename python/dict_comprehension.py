# see https://www.datacamp.com/community/tutorials/python-dictionary-comprehension

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print('original', dict1)

# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print('double values', double_dict1)
# Double each key
dict1_keys = {k*2:v for (k,v) in dict1.items()}
print('double keys', dict1_keys)

## with a condition
numbers = range(10)
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}
print('Built using a condition', new_dict_comp)


## Example of use of map and lambda function and how to substitute it with dict comprehension

# With lambda function and map()
# Initialize `fahrenheit` dictionary
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print('Built with lambda and map', celsius_dict)


# With dict comprehension
# Get the corresponding `celsius` values and create the new dictionary
celsius_dict2 = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

print('Built with dict comprehension', celsius_dict2)
