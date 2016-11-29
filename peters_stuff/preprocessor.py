import pandas as pd
import datetime

pitchers = pd.read_csv("./raw_data/all_star_pitchers.csv", sep=',');
batters = pd.read_csv("./raw_data/all_star_batters.csv", sep=',', parse_dates=["debut"]);

batters = batters[batters.AB != '\N'][batters.R != '\N'][batters.H != '\N'][batters['2B'] != '\N'][batters['3B'] != '\N'][batters['HR'] != '\N'][batters['RBI'] != '\N'][batters['debut'] != '\N'][batters['weight'] != '\N'][batters['height'] != '\N']


batters['age'] = batters['yearID'].astype(int) - batters['birthYear'].astype(int)
batters['num_years_in_league'] = batters['yearID'].astype(int) - pd.to_datetime(batters['debut']).dt.year

# print batters['num_years_in_league']
#df[['`','col_2']].apply(lambda x: f(*x), axis=1)
# print batters['debut']
# batters[batters['debut'].year]

batters = batters.replace({'GP': {'0': 1}})
batters = batters.replace({'GP': {'\N': 0}})
print batters[["playerID", "lgID", "yearID", "AB", "R", "H", "2B", "3B", "HR", "RBI", "GP", "height", "weight", "debut", "age", "num_years_in_league"]].to_csv(index_label=False, index=False)
