for element in range(1, 21):
    print('element', element)

my_list = [20, 1, 9, 0, 2, 50, 39, 13]

for element in my_list:
    print('element_list', element)

my_tuple = (20, 1, 9, 0, 2, 50, 39, 13)

for element in my_tuple:
    print('element_tuple', element)

person = {
    'name': 'Math',
    'city': 'Baq',
    'age': 20
}

for key in person:
    print('person', key, person[key])

for key, value in person.items():
    print(key, '=>', value)


people = [
    {
        'name': 'Math',
        'city': 'Baq',
        'age': 20
    },
    {
        'name': 'Andres',
        'city': 'Med',
        'age': 50
    },
]

for e_person in people:
    print('people-person', e_person)
    print('people-person name => ', e_person['name'])