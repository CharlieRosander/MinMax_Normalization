import pandas as pd
import numpy as np


class Data:
    def __init__(self, csv):
        self.csv_file = csv

    @staticmethod
    def read_csv():
        csv_dataframe = pd.read_csv(csv.csv_file)
        return csv_dataframe

    @staticmethod
    def min_max_norm(dataframe):
        pass


csv = Data("Automobile_data (2).csv")
df = csv.read_csv()

# def check_dtype(columns):
#     return all(map(lambda x: isinstance(x, (int, float)), columns))
#
# results = df_norm.apply(check_dtype)
# print(results)

# def check_dtype(columns):
#     return map(lambda x: isinstance(x, (int, float)), columns)
#
# results = df_norm.apply(check_dtype)
# print(results)

# columns_to_normalise = ["index", "wheel-base", "length", "horsepower", "average-mileage", "price"]
# results = []
# for column in columns_to_normalise:
#     min = df_norm[column].min()
#     max = df_norm[column].max()
#     results.append(f"Normaliserad data i kolumn: {column} är: ")
#     for value in df_norm[column]:
#         x = value
#         results.append([(x - min) / (max - min)])
#
# print(results)


# for column in df_norm[["index", "wheel-base", "length", "horsepower", "average-mileage", "price"]]:
#     col_min = df_norm[column].min()
#     col_max = df_norm[column].max()
#     for value in df_norm[column]:
#         x = value
#         df_norm.replace(x, (x - min) / (max - min), inplace=True)

# print(df_norm.head(20))
# print(results)
# print(df_norm.loc[df_norm["index"] < -1])

df_norm = df.copy()
columns = ["index", "wheel-base", "length", "horsepower", "average-mileage", "price"]
for column in columns:
    col_min = df_norm[column].min()
    col_max = df_norm[column].max()
    df_norm[column + "_normalized"] = (df_norm[column] - col_min) / (col_max - col_min)

# print(df_norm)

for column in df_norm:
    if "_normalized" in column:
        df_norm = df_norm.drop(column, axis=1)
        # print(column)
for column in df_norm[["index", "wheel-base", "length", "horsepower", "average-mileage", "price"]]:
    col_min = df_norm[column].min()
    col_max = df_norm[column].max()
    df_norm[column] = (df_norm[column] - col_min) / (col_max - col_min)

print(df_norm)