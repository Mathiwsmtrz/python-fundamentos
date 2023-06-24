set_countries_ame = {'col', 'mex', 'usa', 'col', 'cnd'}
set_countries_eur = {'es', 'po', 'fr', 'cnd'}

set_result1 = set_countries_ame.union(set_countries_eur)
print(set_result1)
print(set_countries_ame | set_countries_eur)

set_result2 = set_countries_ame.intersection(set_countries_eur)
print(set_result2)
print(set_countries_ame & set_countries_eur)

set_result3 = set_countries_ame.difference(set_countries_eur)
print(set_result3)
print(set_countries_ame - set_countries_eur)

set_result4 = set_countries_ame.symmetric_difference(set_countries_eur)
print(set_result4)
print(set_countries_ame ^ set_countries_eur)