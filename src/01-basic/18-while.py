counter = 0

while counter < 20: 
    counter += 1
    if counter == 15 : break
    print('it was done', counter)

counter = 0

while counter < 20: 
    counter += 1
    if counter < 15 : continue
    print('continue', counter)