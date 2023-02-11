import pandas as pd


class Data:
    value = None

    def __init__(self, csv):
        self.csv_file = csv

    @staticmethod
    def read_csv():
        csv_dataframe = pd.read_csv(csv.csv_file)
        return csv_dataframe

    @staticmethod
    def minMax_norm(dataframe):
        for column in dataframe[["index", "wheel-base", "length", "horsepower", "average-mileage", "price"]]:
            col_min = dataframe[column].min()
            col_max = dataframe[column].max()
            dataframe[column + "_normalized"] = (dataframe[column] - col_min) / (col_max - col_min)


csv = Data("Automobile_data (2).csv")
df = csv.read_csv()

# print(df)

column_names = []


def check_dtype(columns):
    return all(map(lambda x: isinstance(x, (int, float)), columns))


def set_column_names():
    results = df.apply(check_dtype)
    column_names = results[results == True].index


set_column_names()

# print(column_names)
results = df.apply(check_dtype)
# for col_name in results.index:
#     column_names.append(col_name)
print(results)
# print(column_names)
# for column in df:
#     print(s)
