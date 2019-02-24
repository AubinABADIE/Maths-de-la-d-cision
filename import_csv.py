import csv


def import_csv():
    size = 11

    ids = []
    preferences = []

    with open('preferences.csv') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            if read.line_num == 1:
                ids = row[1:size+1]
            elif read.line_num <= size + 1:
                preferences.append(row[1:size+1])
    return ids, preferences