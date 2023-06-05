numbers = (4, 7, 1, 4, 5, 0)
strings = ('juan', 'pedro', 'julia', 'julia')

print(numbers, type(numbers))
print(' 0 => ', numbers[0])

print(strings, type(strings))
print('pedro => ', strings.index('pedro'))
print('julia len => ', strings.count('julia'))

# convert tupla in list

my_list = list(strings)
print(my_list, type(my_list))
my_list.append('kely')
print(my_list)

# convert list in tupla

my_tuple = tuple(my_list)
print(my_tuple, type(my_tuple))