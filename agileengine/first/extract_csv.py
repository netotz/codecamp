import numpy as np
import pandas as pd


def solution(files):
    '''
    ! didn't work with all datasets
    '''
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    dataframes = [pd.read_csv(path, parse_dates=[0]) for path in files]
    reports = list()
    for df in dataframes:
        reports.append([
            df.loc[
                df.groupby(df['date'].dt.year)['vol'].idxmax()
            ][
                ['date', 'vol']
            ].reset_index().drop(['index'], axis=1),
            df.loc[
                df.groupby(df['date'].dt.year)['close'].idxmax()
            ][
                ['date', 'close']
            ].reset_index().drop(['index'], axis=1),
            
        ])
    return reports


print(solution([
    'data\\throwsh.csv',
    'data\\twerche.csv'
]))
