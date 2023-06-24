def increment(x):
    return x + 1
print('normal', increment(10))

increment_l = lambda x : x + 1
print('lambda', increment_l(10))

fullname = lambda name, lastname : f'Full name is {name.title()} {lastname.title()}'
print(fullname('mathis', 'salazar'))