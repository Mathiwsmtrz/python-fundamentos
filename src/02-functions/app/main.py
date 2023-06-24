import utils
import read_csv
import charts

# data = [
#     {
#         'Country': 'Colombia',
#         'Populations': 200,
#     },
#     {
#         'Country': 'Bolivia',
#         'Populations': 300,
#     }
# ]

data = read_csv.read_csv('./../assets/world_population.csv')

def run_country():
    country = input('Set Country => ')
    result = utils.population_by_territory(data, country)
    if result:
        countryData = utils.get_ages_btw(result[0])
        labels, values = countryData
        charts.generate_bar_chart(labels, values)

def run_mundial():
    labels = list(map(lambda item : item['Country/Territory'], data))
    values = list(map(lambda item : item['World 1Population Percentage'], data))
    charts.generate_pie_chart(list(labels), list(values))



if __name__ == '__main__':
    print('Set program => 0: country | 1: mundial')
    program = input('=> ')
    
    if program == '0':
        run_country()
    else:
        run_mundial()