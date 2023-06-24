def range_sum(init, end):
    sum = 0
    for x in range(init, end):
        sum += x
    return sum

print(range_sum(1, 10))


result = range_sum(1, 20)
print('result', result)