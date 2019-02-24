from import_csv import *

ids, preferences = import_csv()

preferences = sort_preferences(ids, preferences)


def get_line(i):
    return preferences[i]


def get_column(i):
    out = []
    for row in preferences:
        out.append(row[i])
    return out


print('DONE')
