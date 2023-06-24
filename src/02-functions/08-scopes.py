price = 100 # global

def increment():
    price = 200 # local
    price = price + 10
    return price

price_2 = increment()
print('price', price)
print('price increment', price_2)

def increment():
    price = 200 # local
    result = price + 10
    return result
price_3 = increment()
print('price new', price_3)