import pandas as pd
pitchers = pd.read_csv("./raw_data/all_stars_pitchers.csv", sep=',');
batters = pd.read_csv("./raw_data/all_stars_batters.csv", sep=',');
print pitchers
print pitchers[["playerID"]]
print batters[["playerID"]]
