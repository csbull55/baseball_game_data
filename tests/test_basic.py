import pandas as pd
from src.baseballdata import baseball_data_raw

# 2018 mlb game data
df = baseball_data_raw()

print(df.head())