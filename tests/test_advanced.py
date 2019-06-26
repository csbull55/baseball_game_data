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
        avg_duration = round(df['Duration'].mean(), 2)
        avg_length_inn = round(df['LengthInOuts'].mean(), 2) / 6

        stats = [
            num_of_games,
            num_of_teams,
            avg_duration,
            avg_length_inn,
        ]

        info = '\n'.join(map(str, stats))
        return info


    def score_info(self):
        avg_home_score = df['HomeRunsScore'].mean()
        avg_away_scores = df['VisitorRunsScored'].mean()

        stats = [
            avg_home_score,
            avg_away_scores,
        ]

        info = '\n'.join(map(str, stats))
        return info


gm2018 = Games(df)

print(gm2018.basic_info())
print(gm2018.score_info())