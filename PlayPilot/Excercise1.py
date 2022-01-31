import csv
import operator
import pandas as pd

with open('customers.csv', newline='') as csvFile:
    reader = csv.reader(csvFile, delimiter=';')
    reader = sorted(reader, key=operator.itemgetter(1), reverse=True)
    sortedcsv = sorted(reader, key=operator.itemgetter(2), reverse=False)
    sortedcsv = pd.DataFrame(sortedcsv)
    sortedcsv = sortedcsv.set_axis(['Name', 'Age', 'Country'], axis='columns')
    sortedcsv.to_csv('Result.csv', index=False, sep=';')
