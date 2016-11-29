import copy
import csv
from datetime import datetime


columns_to_avg = ["R", "H", "2B", "3B", "HR", "salary", "weight", "height"]

def directory(name):
    return "./peters_stuff/" + name

#yearID,G,R,H,2B,3B,HR,salary,playerID,weight,height,bats,debut

def calc_avg(key, entries):
    return float(sum([d[key] for d in entries])) / float(len(entries))


def read_csv(filename):
    with open(directory(filename)) as f:
        reader = csv.reader(f, skipinitialspace=True)
        header = next(reader)
        data = []
        for row in reader:
            row = map(lambda r: int(r) if r.isdigit() else r, row)
            data.append(dict(zip(header, row)))

    return data

def add_avgs(columns, entries, row):
    for column in columns:
        row[column + "_avg"] = calc_avg(column, entries)


def sanitize_data(data):
    return filter(lambda row: not any(row[col] == "N" for col in columns_to_avg), data)


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

def run():
    data = read_csv("test.csv")
    data = sanitize_data(data)
    print data[0]

    players_list = list(set(map(lambda row: row["playerID"], data)))
    print "splitted"
    data_by_player = split_by_player(players_list, data)

    for row in data:
        player = row["playerID"]
        cur_year = row["yearID"]
        entries = filter(lambda x: x["yearID"] <= cur_year, data_by_player[player])

        add_avgs(columns_to_avg, entries, row)

        debut = datetime.strptime(row["debut"], "%Y-%m-%d %M:%H:%S")
        row["num_years_in_league"] = cur_year - debut.year

    to_csv(data, "cleansed_data.csv")


run()
