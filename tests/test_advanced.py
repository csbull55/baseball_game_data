import pandas as pd
from src.baseballdata import baseball_data_raw

# 2018 mlb game data
df = baseball_data_raw()


class Games:
    def __init__(self, df):
        self.df = df

    def basic_info(self):
        # basic info on the df
        num_of_games = len(df['Date'])
        num_of_teams = len(df.groupby('HomeTeam').nunique())

        # returns basic info
        stats = [
            num_of_games,
            num_of_teams,
        ]

        info = '\n'.join(map(str, stats))
        return info


gm1 = Games(df)

print(gm1.basic_info())
