def get_populations():
    keys = ['col', 'bol', 'arg']
    values = [200, 500, 140]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result

def population_by_territory(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

def get_ages_btw(item):
    value = {}
    for key in item:
        fourFirstChars = str(key[:4])
        if fourFirstChars.isdigit():
            value[fourFirstChars] = int(item[key])
    return value.keys(), value.values()

A = 'a'