import sys

print(sys.path)

import re
text = 'My number is 331 309 9089, the country number is +57'

result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
format = time.asctime(local)
print(format)
print(timestamp)

import collections
numbers = [1, 1, 2, 2, 1, 4, 5, 5, 21]
counter = collections.Counter(numbers)
print(counter)