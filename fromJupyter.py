import pandas as pd
import numpy as np


# #### En klass för Data-hanteringen. Den kan läsa in csv filer och skapa objekt av dom, köra pre-processing samt min-max-normalisering av data. 
# 
# #### Pre-process funktionen låter användaren välja vad som ska göras med NaN-värden genom att skriva in parametrar. "show" visar NaN värdena, "drop" droppar dom raderna som innehåller NaN, och 0 sätter NaN till 0

class Data:
    value = None

    def __init__(self, csv):
        self.csv_file = csv

    @staticmethod
    def read_csv():
        csv_dataframe = pd.read_csv(csv.csv_file)
        return csv_dataframe

    @classmethod
    def data_preprocess(cls, value):
        cls.value = value
        if value == "show":
            print(df_norm.isnull().sum())

        elif value == "drop":
            df_norm.dropna(inplace=True)

        elif value == 0:
            df_norm.fillna(0, inplace=True)
            print(f"Changed NaN values to 0.\n{df_norm.isnull().sum()}")

    @staticmethod
    def minMax_norm(dataframe):
        for column in dataframe[["index", "wheel-base", "length", "horsepower", "average-mileage", "price"]]:
            col_min = dataframe[column].min()
            col_max = dataframe[column].max()
            dataframe[column + "_normalized"] = (dataframe[column] - col_min) / (col_max - col_min)

    @staticmethod
    def minMax_norm_replace(dataframe):
        for column in dataframe:
            if "_normalized" in column:
                dataframe.drop(column, axis=1, inplace=True)

        for column in dataframe[["index", "wheel-base", "length", "horsepower", "average-mileage", "price"]]:
            col_min = dataframe[column].min()
            col_max = dataframe[column].max()
            dataframe[column] = (dataframe[column] - col_min) / (col_max - col_min)


csv = Data("Automobile_data.csv")
df = csv.read_csv()

# #### Skapar ett nytt objekt av datan för att normalisera

df_norm = csv.read_csv()
df_norm_replaced = csv.read_csv()
print(df_norm)
print(df_norm_replaced)
# #### Här väljer jag att sätta NaN värden till 0

Data.data_preprocess(0)

# #### Formeln för normalisering som används här kommer vara: **$V = (x - min) / (max - min)$** , kallad min-max normalisering

Data.minMax_norm(df_norm)

print(df_norm)

Data.minMax_norm_replace(df_norm_replaced)

print(df_norm_replaced)

Data.minMax_norm_replace(df_norm)

print(df_norm)
