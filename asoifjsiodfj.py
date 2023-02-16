import pandas as pd
import numpy as np

df = pd.read_csv("Automobile_data (2).csv")

col = df.columns
# print(col)
for i in col:
    print(np.dtype(df[i].values))
    if isinstance(df[i].values, (int, float)):
        for value in df[i]:
            print(value)
# (dataframe[column] - col_min) / (col_max - col_min)
# print(df)