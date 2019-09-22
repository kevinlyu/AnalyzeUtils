import pandas as pd
from tqdm import tqdm

PATH = input("Input directory of System.map: ")
SYSTEM_MAP_PATH = PATH + "/System.map"

# use nrows=N to read first N lines
df = pd.read_csv(SYSTEM_MAP_PATH, sep=" ", encoding="utf-8", names=["Address", "Type", "Name"])

print("[Processing]")

# add "Size" column
df.insert(3, "Size", 0)

n_row, n_col = df.shape

for i in tqdm(range(1, n_row-1)):
    df.loc[i, "Size"] = int(df.loc[i+1, "Address"], 16) - int(df.loc[i, "Address"], 16)

# sort by memory usage
df = df.sort_values(["Size"], ascending=False)

# save without row index numbers
df.to_excel("memory_usage.xlsx", index=False)

print("[Done]")

