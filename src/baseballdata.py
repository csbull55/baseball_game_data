import pandas as pd

# column names
raw_columns = pd.read_csv(r"F:\Projects\Programming_projects\baseball_stats\game_data\data\column_headers.csv", sep=",")
head = raw_columns['index']


# this is the source data
def baseball_data_raw():
    df = pd.read_csv(r"F:\Projects\Programming_projects\baseball_stats\game_data\data\game_data.csv")
    df.columns = head
    return df
