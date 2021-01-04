import pandas as pd
import glob

def organize_dataset(path):
    col_names = ["ax","ay","az","gx","gy","gz","acx","acy","acz"]
    data = pd.read_csv(path, names = col_names)
    data = data.replace(';', '.', regex=True)
    data = data.drop('acx', axis=1)
    data = data.drop('acy', axis=1)
    data = data.drop('acz', axis=1)
    data.insert(loc = 0, column = 'time', value=data.index*0.005)
    data['path'] = path
    print(data.head(2))
    data['rolling_mean'] = data['ax'].rolling(window=200).mean()
    data = data[['time', 'rolling_mean', 'ax']]
    print(data.tail(2))
    print(data.shape)

def Sisfall_analysis():
    path = "Sisfall_dataset/"
    allFiles = glob.glob(path + "*")
    for file_ in allFiles:
        allfiles2 =glob.glob(file_+"/*.txt")
        for file_2 in allfiles2:
            organize_dataset(file_2)

Sisfall_analysis()



