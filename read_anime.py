import csv

def ani_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        header = next (reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            type_dict = {key:value for key, value in iterable}
            data.append(type_dict)
        return data
