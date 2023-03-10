import pandas as pd
import numpy as np


class Data:
    value = None
    columns_to_normalize = []

    def __init__(self, csv):
        self.csv_file = csv

    @staticmethod
    def read_csv():
        csv_dataframe = pd.read_csv(csv.csv_file)
        return csv_dataframe

    @classmethod
    def data_preprocess(cls, dataframe, value):
        cls.value = value
        if value == "show":
            print(dataframe.isnull().sum())

        elif value == "drop":
            dataframe.dropna(inplace=True)

        elif value == 0:
            dataframe.fillna(0, inplace=True)
            print(f"Changed NaN values to 0.\n{dataframe.isnull().sum()}")

    @staticmethod
    def check_dtype(columns):
        return all(map(lambda x: isinstance(x, (int, float)), columns))

    @classmethod
    def set_column_names(cls, dataframe):
        results = dataframe.apply(Data.check_dtype)
        Data.columns_to_normalize = results[results == True].index

    @staticmethod
    def min_max_norm(dataframe):
        for column in dataframe[Data.columns_to_normalize]:
            col_min = dataframe[column].min()
            col_max = dataframe[column].max()
            dataframe[column + "_normalized"] = (dataframe[column] - col_min) / (col_max - col_min)

    @staticmethod
    def min_max_norm_replace(dataframe):
        for column in dataframe:
            if "_normalized" in column:
                dataframe.drop(column, axis=1, inplace=True)

        for column in dataframe[Data.columns_to_normalize]:
            col_min = dataframe[column].min()
            col_max = dataframe[column].max()
            dataframe[column] = (dataframe[column] - col_min) / (col_max - col_min)

    @staticmethod
    def save_to_csv(dataframe, file_name):
        dataframe.to_csv(file_name + ".csv", index=False)


csv = Data("pokemon_data.csv")
df = csv.read_csv()
df_norm = csv.read_csv()
df_norm_replaced = csv.read_csv()

Data.set_column_names(df_norm)
print(Data.columns_to_normalize)
Data.min_max_norm_replace(df_norm)
print(df_norm)
# Data.save_to_csv(df_norm, "Normaliserad_csv")
