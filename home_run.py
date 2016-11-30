import copy
import csv
import numpy as np
from datetime import datetime

#yearID,G,R,H,2B,3B,HR,salary,playerID,weight,height,bats,debut,AB,SO,BB,IBB,SH,SF,GIDP,birthYear

columns_to_stat = ["R", "H", "2B", "3B", "HR", "salary", "weight", "height", "AB", "SO", "BB", "IBB", "SH", "SF", "GIDP", "G", "RBI"]

def directory(name):
    return "./peters_stuff/" + name

#yearID,G,R,H,2B,3B,HR,salary,playerID,weight,height,bats,debut

def calc_avg(key, entries):
    return float(sum([d[key] for d in entries])) / float(len(entries))

def calc_recent(key, entries):
    return max(entries, key=lambda e: e["yearID"])[key]

def calc_std(key, entries):
    return np.std(np.array([d[key] for d in entries]))


def read_csv(filename):
    with open(directory(filename)) as f:
        reader = csv.reader(f, skipinitialspace=True)
        header = next(reader)
        data = []
        for row in reader:
            row = map(lambda r: int(r) if r.isdigit() else r, row)
            data.append(dict(zip(header, row)))

    return data

def add_stats(columns, entries, row):
    for column in columns:
        row[column + "_avg"] = calc_avg(column, entries)
        row[column + "recent"] = calc_recent(column, entries)
        row[column + "_std"] = calc_std(column, entries)


def sanitize_data(data):
    return filter(lambda row: not any(row[col] == "N" for col in columns_to_stat), data)


def split_by_player(players, data):
    players_data = {}
    for player in players:
        players_data[player] = filter(lambda row: row["playerID"] == player, data)

    return players_data

def to_csv(toCSV, filename):
    keys = toCSV[0].keys()
    with open(filename, 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)

# Must have at bats greater than 100
def remove_non_batters(data):
    return filter(lambda row: row["AB"] > 100, data)

def run():
    data = read_csv("test.csv")
    data = sanitize_data(data)
    data = remove_non_batters(data)
    print data[0]

    players_list = list(set(map(lambda row: row["playerID"], data)))
    print "splitted"
    data_by_player = split_by_player(players_list, data)

    to_remove = set()
    for row in data:
        player = row["playerID"]
        cur_year = row["yearID"]
        entries = filter(lambda x: x["yearID"] < cur_year, data_by_player[player])

        if len(entries) > 0:
            add_stats(columns_to_stat, entries, row)
            debut = datetime.strptime(row["debut"], "%Y-%m-%d %M:%H:%S")
            row["num_years_in_league"] = cur_year - debut.year
            row["age"] = cur_year - row["birthYear"]
        else:
            to_remove.add(player + "_" + str(cur_year))

    data = filter(lambda x: x["playerID"] + "_" + str(x["yearID"]) not in to_remove, data)
    
    to_csv(data, "cleansed_data.csv")


run()
