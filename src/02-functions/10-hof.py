sum = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b

def exec_operation(func, a, b):
    return func(a, b)

print('sum', exec_operation(sum, 1, 2))
print('sub', exec_operation(sub, 1, 2))
print('mul', exec_operation(mul, 1, 2))
print('div', exec_operation(div, 1, 2))
