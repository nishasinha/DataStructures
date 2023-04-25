import pandas as pd


def read_csv(filename):
    df = pd.read_csv(filename)
    # print(df.info)
    return df


def clean_df(df, column_names):
    # print("Filling zeros for column_names: " + str(column_names))
    for col in column_names:
        df[col].fillna(0, inplace=True)


def subtract(df1, df2, column_names):
    result = pd.DataFrame()

    for col in column_names:
        # print("Subtracting for column name: " + col)
        result[col] = df1[col] - df2[col]

    print("Result DF")
    print(result)
    return result


def main():
    preprod = read_csv('./preprod.csv')
    prod = read_csv('./prod.csv')

    all_columns = list(prod.columns.values)
    non_numerical_columns = ['AsOfDt', 'YTC_Date', 'InsertDt', 'UpdateDt', 'UpdatedBy',
                             'FA_YTC_Date', 'FA_YTW_Date', 'YTW_Date']
    numerical_columns = []
    for col in all_columns:
        if col not in non_numerical_columns:
            numerical_columns.append(col)

    # print("all_columns:\n" + str(all_columns))
    # print("non_numerical_columns:\n" + str(non_numerical_columns))
    # print("numerical_columns:\n" + str(numerical_columns))

    clean_df(preprod, numerical_columns)
    clean_df(prod, numerical_columns)

    result = subtract(prod, preprod, numerical_columns)


if __name__ == '__main__':
    main()

