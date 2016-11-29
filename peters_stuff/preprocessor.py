import pandas as pd

pitchers = pd.read_csv("./raw_data/all_star_pitchers.csv", sep=',');
batters = pd.read_csv("./raw_data/all_star_batters.csv", sep=',');

batters = batters[batters.AB != '\N'][batters.R != '\N'][batters.H != '\N'][batters['2B'] != '\N'][batters['3B'] != '\N'][batters['HR'] != '\N'][batters['RBI'] != '\N'][batters['debut'] != '\N'][batters['weight'] != '\N'][batters['height'] != '\N']
batters = batters.replace({'GP': {'0': 1}})
batters = batters.replace({'GP': {'\N': 0}})
print batters[["playerID", "lgID", "yearID", "AB", "R", "H", "2B", "3B", "HR", "RBI", "GP", "height", "weight", "debut"]].to_csv(index_label=False, index=False)
