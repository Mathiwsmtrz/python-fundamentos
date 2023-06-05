numbers = [9, 5, 6, 7, 0]
tasks = ['make', 'buy', 'sell', 'call']
types = [True, 'Juan', 5, False, 0, 'PEdro']

print(numbers)
print(type(numbers))

print(numbers[1])
print(tasks[0])


tasks[0] = 'walk'
print(tasks)
print(tasks[:3])
print(True in types)
print('Juan' in types)
print('Luz' in types)
