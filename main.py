from utlis import *
from stableroomate import *
from stable_marriage import *

order = ['TB', 'B', 'AB', 'P', 'I', 'AR']
nb_duos = 18

ids, preferences = import_csv()
sorted_preferences = sort_preferences(ids, preferences)


roommate_match = stableroomate(sorted_preferences)
roommate_match = roommate_match[:nb_duos]

alone = get_alone(ids, roommate_match)

roommate_group_names = get_group_names(roommate_match)

roommate_groups_to_match = roommate_match[:4]
roommate_group_names_to_match = roommate_group_names[:4]

group_preferences = get_group_preferences(ids, preferences, roommate_group_names_to_match, alone)
alone_preferences = get_alone_preferences(ids, preferences, roommate_group_names_to_match, alone)


json = {
    "men_rankings": {},
    "women_rankings": {}
}

for i, name in enumerate(roommate_group_names_to_match):
    json["men_rankings"][name] = group_preferences[i]

for i, name in enumerate(alone):
    json["women_rankings"][name] = alone_preferences[i]

marriage_match = StableMatching(json['men_rankings'], json['women_rankings'])
marriage_match = map(lambda m: (m[0].split("_")[0], m[0].split("_")[1], m[1]), marriage_match)

for g in roommate_groups_to_match:
    roommate_match.remove(g)

final_match = []
final_match.extend(marriage_match)
final_match.extend(roommate_match)


print("ROOMMATE MATCHES:")
for m in roommate_match:
    print(m)

print("ALONE:")
print(alone)

print("MARRIAGE MATCHES:")
for m in marriage_match:
    print(m)

print("FINAL MATCH:")
for m in final_match:
    print(m)

def get_line(i):
    return preferences[i]


def get_column(i):
    out = []
    for row in preferences:
        out.append(row[i])
    return out


print('DONE')
