import pandas as pd

# assigns numbers to the column headers
head = list(range(1, 162))


# this is the source data
def baseball_data():
    df = pd.read_csv(r"F:\Projects\Programming_projects\baseball_stats\game_data\data\game_data.csv")
    return df
