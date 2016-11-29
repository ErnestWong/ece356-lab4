import pandas as pd
pitchers = pd.read_csv("./raw_data/all_stars_pitchers.tsv", sep=',');
batters = pd.read_csv("./raw_data/all_stars_batters.tsv", sep=',');
print pitchers
print pitchers[["playerID"]]
print batters[["playerID"]]
