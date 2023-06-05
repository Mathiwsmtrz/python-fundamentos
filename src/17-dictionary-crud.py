person = {
    'name': 'Mathiws',
    'lastname': 'salazar',
    'age': 24,
    'langs': ['python', 'php', 'js']
}
print(person)

person['lastname'] = 'Montropez'
person['age'] -= 4
person['langs'].append('html')
person.update({'twitter': '@mathiws'})
print(person)

del person['lastname']
print(person)

person.pop('age')
print(person)

print('items =>', person.items())
print('keys =>', person.keys())
print('values =>', person.values())
