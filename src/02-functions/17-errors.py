# print(0 / 0)
print('Hi')

sum = lambda x,y: x+y

assert sum(1, 3) == 4

print('Success sum 4')

# age = 10
# if age < 18:
#     raise Exception('Not Children')

# managmnet error

try:
    print(0 / 0)
except ZeroDivisionError as error:
    print('error', error)

try:
    assert 1 != 1, '1 is equal to 1'
except AssertionError as error:
    print('error', error)

try:
    age = 10
    if age < 18:
        raise Exception('Not Children')
except Exception as error:
    print('error', error)

try:
    print(0 / 0)
    assert 1 != 1, '1 is equal to 1'
    age = 10
    if age < 18:
        raise Exception('Not Children')
except ZeroDivisionError as error:
    print('error', error)
except AssertionError as error:
    print('error', error)
except Exception as error:
    print('error', error)

print('finish')