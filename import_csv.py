import csv

order = ['TB', 'B', 'AB', 'P', 'I', 'AR']


def import_csv():
    size = 40

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


def map_func(c, i, ids):
    if c == 'TB':
        return c, 6, ids[i]
    elif c == 'B':
        return c, 5, ids[i]
    elif c == 'AB':
        return c, 4, ids[i]
    elif c == 'P':
        return c, 3, ids[i]
    elif c == 'I':
        return c, 2, ids[i]
    elif c == 'AR':
        return c, 1, ids[i]
    else:
        return c, 7, ids[i]


def sort_preferences(ids, preferences):
    temp = []
    for i, row in enumerate(preferences):
        line = []
        for j, col in enumerate(row):
            line.append(map_func(col, j, ids))
        temp.append(line)
    temp2 = []
    for row in temp:
        sorted_row = sorted(row, key=lambda tup: tup[1], reverse=True)
        temp2.append(sorted_row)
    out = []
    for i, row in enumerate(temp2):
        out.append(list(map(lambda c: c[2], row)))

    return out
