set_countries = {'col', 'mex', 'usa', 'col'}
print(set_countries, type(set_countries))

size = len(set_countries)
print('size =>', size)
print('col in =>', 'col' in set_countries)
print('per in =>', 'per' in set_countries)

# add
set_countries.add('per')
print(set_countries)
set_countries.add('per')
print(set_countries)

# update
set_countries.update({'arg', 'per', 'chl'})
print(set_countries)

# remove
set_countries.remove('chl')
print(set_countries)

# set_countries.remove('chl') # (error if not exits)
set_countries.discard('chl')
print(set_countries)

# clear
set_countries.clear()
print(set_countries)