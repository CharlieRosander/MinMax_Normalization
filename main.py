import pandas as pd


class Data:
    value = None
    columns_to_normalize = []

    def __init__(self, csv):
        self.csv_file = csv

    @staticmethod
    def read_csv():
        try:
            csv_dataframe = pd.read_csv(csv.csv_file)
            return csv_dataframe
        except ValueError:
            print(ValueError, "The CSV-file is empty.")
            exit()

    @classmethod
    def data_preprocess(cls, dataframe, value):
        cls.value = value
        print(f"Columns containing NaN-values:\n{dataframe.isnull().sum()[dataframe.isnull().sum() > 0]}")

        if value == "show":
            print(dataframe.isnull().sum())

        elif value == "drop":
            dataframe.dropna(inplace=True)

        elif value == 0:
            dataframe.fillna(0, inplace=True)
            print(f"\nChanged all NaN values to 0.\n{dataframe.isnull().sum()}")

    @classmethod
    def set_columns(cls, dataframe):
        if "index" or "idx" or "ix" in dataframe.columns:
            for col in dataframe.columns[1:]:
                if all(isinstance(x, (int, float)) for x in dataframe[col]):
                    if not dataframe[col].dtype in ['bool']:
                        Data.columns_to_normalize.append(col)
        else:
            for col in dataframe.columns:
                if all(isinstance(x, (int, float)) for x in dataframe[col]):
                    if not dataframe[col].dtype in ['bool']:
                        Data.columns_to_normalize.append(col)

        return print(f"These are the columns that will be normalized: \n{Data.columns_to_normalize}")

    @staticmethod
    def min_max_norm(dataframe):
        for column in dataframe[Data.columns_to_normalize]:
            col_min = dataframe[column].min()
            col_max = dataframe[column].max()
            dataframe[column] = ((x for x in dataframe[column]) - col_min) / (col_max - col_min)

    @staticmethod
    def save_to_csv(dataframe):
        file_name = input("\nEnter the name for the CSV file: ")
        dataframe.to_csv(file_name + ".csv", index=False)


if __name__ == "__main__":
    csv = Data("Automobile_data.csv")
    df = csv.read_csv()
    df_norm = csv.read_csv()

    Data.data_preprocess(df_norm, "drop")
    Data.set_columns(df_norm)
    Data.min_max_norm(df_norm)
    Data.save_to_csv(df_norm)
