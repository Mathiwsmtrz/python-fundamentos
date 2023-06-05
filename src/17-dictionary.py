my_dict = {}
print(my_dict, type(my_dict))

my_dict = {
    'name': 'Mathiws',
    'lastname': 'salazar',
    'age': 24
}
print(my_dict)
print(len(my_dict))
print(my_dict['name'], my_dict['age'])
print(my_dict.get('lastname'))
print(my_dict.get('address'))
print('age' in my_dict)
print('city' in my_dict)