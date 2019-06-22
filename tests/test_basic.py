import pandas as pd

head = list(range(1, 162))
df = pd.read_csv(r"F:\Projects\Programming_projects\baseball_stats\game_data\data\game_data.csv")

print(df.head())

attend_avg = df['18'].mean()

print(attend_avg)