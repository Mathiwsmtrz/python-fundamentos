# continue write
with open('./assets/text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('new line\n')
    file.write('new line2\n')

# total write
with open('./assets/text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('new line\n')
    file.write('new line2\n')