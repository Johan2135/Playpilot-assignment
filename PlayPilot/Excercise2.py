from operator import index
import pandas as pd
import csv
import math

def check(data):
    '''Checks if data is correct'''
    data = data.values.tolist()
    for x in range(len(data)):
        counter = 0
        for y in range(1, len(data[0])):
            if data[x][y] == "''":
                continue
            if y == 1:
                if data[x][y].isnumeric() == False:
                    raise SystemExit('Wrong in data, see: line = ' + str(x) + 'column = ' + str(y))
            if y == 2:
                if data[x][y].startswith('tt') == False:
                    raise SystemExit('Wrong in data, see: line = ' + str(x) + 'column = ' + str(y))
            if y == 3:
                if data[x][y].isupper() == False:
                    raise SystemExit('Wrong in data, see: line = ' + str(x) + 'column = ' + str(y))

def mergefunction(data1, data2):
    '''Takes in the data and merges, saves results as two files: manual and confident'''
    '''The confident list are the ones where we have information about title, release date, origin, and imdb-id.
    The data from data1 and data 2 should also match.'''
    output = pd.merge(data1, data2, on='Title', 
                   how='outer')
    test = output.values.tolist()
    confident = []
    Manual = []
    for x in range(len(test)):
        counter = 0
        for y in range(1,len(test[0])//2 + 1):
            y2 = y + 3
            if (pd.isna(test[x][y]) or (test[x][y] == str("''"))):
                if test[x][y2] in test[x][:y]:
                    y2 += -1
                test[x][y] = test[x][y2]
            if (pd.isna(test[x][y2]) or (test[x][y2] == str("''"))):
                test[x][y2] = test[x][y]
            if test[x][y] == test[x][y2]:
                if test[x][y] != "''":
                    counter += 1
        if x == 43:
            print(test[43])
        if counter < 3:
            Manual.append(test[x])
        else:
            confident.append(test[x])


    confident = pd.DataFrame(confident)
    Manual = pd.DataFrame(Manual)
    confident = confident.drop(columns=[4,5,6])
    confident = confident.set_axis(['Title', 'Release date', 'IMDB-id', 'origin'], axis='columns')
    Manual = Manual.set_axis(['Title', 'Release date_1', 'IMDB-id_1', 'origin_1', 'Release date_2', 'IMDB-id_2', 'origin_2'], axis='columns')
    confident.to_csv('"confident".csv', index=False, sep=';')
    Manual.to_csv('Manual.csv', index=False, sep=';')

def main():
    data1 = pd.read_csv('titles-1.csv', delimiter=';', header=None, lineterminator='\n', names=['Title', 'Release date', 'IMDB-id', 'origin'])
    data2 = pd.read_csv('titles-2.csv',delimiter=';', header=None, lineterminator='\n', names=['Title', 'Release date', 'IMDB-id', 'origin'])
    check(data1)
    check(data2)
    mergefunction(data1, data2)

if __name__ == "__main__" :
    main()


