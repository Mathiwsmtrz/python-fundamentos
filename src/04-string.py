name = 'mathiws'
last_name = 'montropez'
fullname = name + ' ' + last_name

print("I'm " + name)
print('my fullname is "' + fullname + '"')

template = 'Hi, my first name is ' + name + ' and my last name is ' + last_name
print('v1', template)

template = 'Hi, my first name is {} and my last name is {}'
print('v2', template.format(name, last_name))

template = f'Hi, my first name is {name} and my last name is {last_name}'
print('v3', template.format(name, last_name))
