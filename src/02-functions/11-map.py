numbers = [1, 2, 3, 4]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)

print('v1', numbers)
print('v2', numbers_v2)

numbers_v3 = list(map(lambda i : i * 2, numbers))
print('v3', numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [0, 4, 6, 8]

result = list(map(lambda x, y : x + y , numbers_1, numbers_2))

print('v4', numbers_1)
print('v4', numbers_2)
print('v4', result)