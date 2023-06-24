import csv

def read_csv(path):
    list = []
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader)
        for row in reader:
            dataLine = {key: value for key, value in zip(headers, row)}
            list.append(dataLine)
    return list

if __name__ == '__main__':
    list = read_csv('./../assets/world_population.csv')
    print(list)