from import_csv import *

preferences = sort_preferences(import_csv())

def get_line(i):
    return preferences[i]


def get_column(i):
    out = []
    for row in preferences:
        out.append(row[i])
    return out

print('DONE')