file = open('./assets/text.txt')

# read all
# print(file.read())

# read per line
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# read for line
for line in file:
    print(line)

file.close()

# file close auto when finish
with open('./assets/text.txt') as file2:
    for line in file2:
        print(line)