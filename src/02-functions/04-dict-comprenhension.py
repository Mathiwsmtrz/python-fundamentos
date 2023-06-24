import random

dict1 = {}
for i in range(1, 6):
    dict1[i] = i * 2
print('dict1', dict1)

dict2 = {i : i * 2 for i in range(1, 6)}
print('dict2', dict2)



countries = ['col', 'ven', 'blv']
populations = {}
populations_v2 = {}

for country in countries:
    populations[country] = random.randint(1, 100)
print('populations', populations)

populations_v2 = {country: random.randint(1, 100) for country in countries}
print('populations_v2', populations_v2)


names = ['math', 'andre', 'majo']
ages = [18, 56, 10]

print('zip', list(zip(names, ages)))

new_dict = {name : age for (name, age) in zip(names, ages)}
print('new_dict', new_dict)

new_dict_adult = {name : age for (name, age) in zip(names, ages) if age >= 18}
print('new_dict_adult', new_dict_adult)