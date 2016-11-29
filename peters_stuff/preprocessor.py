import pandas as pd
import numpy as np

pitchers = pd.read_csv("./raw_data/all_star_pitchers.csv", sep=',');
batters = pd.read_csv("./raw_data/all_star_batters.csv", sep=',', parse_dates=["debut"]);

batters = batters[batters.AB != '\N'][batters.R != '\N'][batters.H != '\N'][batters['2B'] != '\N'][batters['3B'] != '\N'][batters['HR'] != '\N'][batters['RBI'] != '\N'][batters['debut'] != '\N'][batters['weight'] != '\N'][batters['height'] != '\N'][batters['CS'] != '\N'][batters['SB'] != '\N'][batters['BB'] != '\N'][batters['SO'] != '\N'][batters['IBB'] != '\N'][batters['SH'] != '\N'][batters['SF'] != '\N'][batters['GIDP'] != '\N']

# get rid of rows where a player played in multiple all star games
batters = batters.drop_duplicates(['playerID', 'yearID'])
pitchers = pitchers.drop_duplicates(['playerID', 'yearID'])

batters['age'] = batters['yearID'].astype(int) - batters['birthYear'].astype(int)
batters['num_years_in_league'] = batters['yearID'].astype(int) - pd.to_datetime(batters['debut']).dt.year


# print batters['num_years_in_league']
#df[['`','col_2']].apply(lambda x: f(*x), axis=1)
# print batters['debut']
# batters[batters['debut'].year]

batters = batters.replace({'GP': {'0': 1}})
batters = batters.replace({'GP': {'\N': 0}})
batters['GP'] = batters['GP'].astype(int)


def previous_all_star_appearances(player_id, curr_year):
    previous_appearances = 0
    result = batters[batters['playerID'] == player_id][batters['yearID'].astype(int) < curr_year]
    if len(result) > 0:
        previous_appearances = result['GP'].sum()
    return previous_appearances

batters['previous_appearances'] = np.vectorize(previous_all_star_appearances)(batters['playerID'], batters['yearID'].astype(int))
# bg = batters[['playerID', 'yearID']].apply(lambda b: batters.where(batters['yearID'] < b.yearID).groupby(['playerID']).agg({'GP': np.sum}).astype(int))

# Note the GP field is actually a 1 or 0 - 1 if the player has played in an all star game that year
print batters[["playerID", "lgID", "yearID", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SB", "CS", "BB", "SO", "IBB", "SH", "SF", "GIDP", "G", "GP", "height", "weight", "debut", "age", "num_years_in_league", "previous_appearances"]].to_csv(index_label=False, index=False)
