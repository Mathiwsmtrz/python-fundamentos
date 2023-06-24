numbers = []
for element in range(1, 11):
    numbers.append(element)
print('numbers', numbers)

numbers_v2 = [element for element in range(1, 11)]
print('numbers_v2', numbers_v2)

numbers_v3 = []
for element in range(1, 11):
    numbers_v3.append(element * 2)
print('numbers_v3', numbers_v3)

numbers_v4 = [element * 2 for element in range(1, 11)]
print('numbers_v4', numbers_v4)

numbers_v5 = [i * 2 for i in range(1, 11) if (i) % 2 == 0]
print('numbers_v5', numbers_v5)