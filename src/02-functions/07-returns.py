def find_volume(length, width, depth):
    return length * width * depth

# v1 = find_volume() # error
v1 = find_volume(10, 20, 3)
print('v1', v1)

def find_volume(length=1, width=1, depth=1):
    return length * width * depth

v2 = find_volume()
print('v2', v2)

v3 = find_volume(width=20)
print('v3', v3)

def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hi'

v4 = find_volume(length=20)
print('v4', v4)
print('v4 result', v4[0])

result, width, text = find_volume(length=20)
print('result', result)
print('width', width)
print('text', text)