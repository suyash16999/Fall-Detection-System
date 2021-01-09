import pandas as pd
import glob

def read_txt(path):
    col_names = ["ax","ay","az","gx","gy","gz","acx","acy","acz"]
    data = pd.read_csv(path, names = col_names)
    data = data.replace(';', '.', regex=True)
    data = data.drop('acx', axis=1)
    data = data.drop('acy', axis=1)
    data = data.drop('acz', axis=1)
    data['path'] = path
    data['index'] = data.index
    print(data.head(5))
    data['Datetime'] = pd.to_datetime(data['index'])
    print(data.head(5))
    data['rolling_mean'] = data['ax'].rolling(window=200).mean()
    data = data[['Datetime', 'rolling_mean', 'ax']]
    print(data.tail(10))
    print(data.shape)

'''import numpy as np
sequence = np.random.normal(size=10000) + np.arange(10000)


def running_average_simple(seq, window=100):
    result = np.zeros(len(seq) - window + 1)
    for i in range(len(result)):
        result[i] = np.mean(seq[i:i + window])
    return result

print(running_average_simple(sequence))'''

def converting():
    path = "Sisfall_dataset/"
    allFiles = glob.glob(path + "*")
    for file_ in allFiles:
        allfiles2 =glob.glob(file_+"/*.txt")
        for file_2 in allfiles2:
            read_txt(file_2)

converting()



