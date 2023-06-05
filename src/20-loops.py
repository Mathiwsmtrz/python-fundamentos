matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)
print('matriz 0 =>', matriz[0])
print('matriz 0:2 =>', matriz[0][2])

for element in matriz:
    for subelement in element:
        print('item => ', subelement)