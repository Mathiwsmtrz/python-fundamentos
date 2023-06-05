tasks = ['make', 'buy', 'sell', 'call']

print(tasks[2])
tasks[-1] = 'walk'
print(tasks)

tasks.append('run')
print(tasks)

tasks.insert(1, 'kiss')
print(tasks)

numbers = [1, 9, 4, 0, 5, 6, 2, 9]
new_list = tasks + numbers
print(new_list)

print(new_list.index('walk'))
print(new_list.index(9))
# print(new_list.index('7')) # ValueError: '7' is not in lists

new_list.remove('walk')
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)


numbers2 = [1, 9, 4, 0, 5, 6, 2, 9]
numbers2.sort()
print(numbers2)

text_sort = ['re', 'ab', 'ci', 'Ai']
text_sort.sort()
print(text_sort)