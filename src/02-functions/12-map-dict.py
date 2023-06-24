items = [
    {
        'product': 'shirt',
        'price': 100
    },
    {
        'product': 'pant',
        'price': 130
    },
    {
        'product': 'jacket',
        'price': 200
    }
]
print('items', items)

prices = list(map(lambda item : item['price'], items))
print('prices', prices)

'''
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print('new_items', new_items)
print('items', items)
'''

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print('new_items', new_items)
print('items', items)