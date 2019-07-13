import pandas as pd
from src.baseballdata import baseball_data_raw

# 2018 mlb game data
df = baseball_data_raw()


class Allteams:
    def __init__(self):
        self.df = df

    def basic_info(self):
        # basic info on the df
        num_of_games = len(df['Date'])
        num_of_teams = len(df.groupby('HomeTeam').nunique())
        avg_duration = round(df['Duration'].mean(), 2)
        avg_length_inn = round(df['LengthInOuts'].mean(), 2) / 6

        # which stats to return
        stats = [
            num_of_games,
            num_of_teams,
            avg_duration,
            avg_length_inn,
        ]

        # prints them line by line
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


def team_data(tmdf):
    num_of_games = len(tmdf['Date'])
    return num_of_games


def game_length(tmdf):
    game_ln = round(tmdf['Duration'].mean(), 2)
    return game_ln


df_alt = df[(df['HomeTeam'] == 'ATL') | (df['VisitingTeam'] == 'ATL')]

print('\n')

print(team_data(df_alt))
print(game_length(df_alt) / 60)