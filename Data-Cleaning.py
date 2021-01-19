import pandas as pd
import glob
import os
import numpy as np
import configparser as cp
import math

def organize_dataset(path):
    col_names = ["ax","ay","az","gx","gy","gz","acx","acy","acz"]
    data = pd.read_csv(path, names = col_names)
    data = data.replace(';', '.', regex=True)
    data = data.drop('acx', axis=1)
    data = data.drop('acy', axis=1)
    data = data.drop('acz', axis=1)
    data.insert(loc = 0, column = 'time', value=data.index*0.005)

    ax = data['ax'] * data['ax']
    ay = data['ay'] * data['ay']
    az = data['az'] * data['az']
    am = ax + ay + az
    am = am.apply(lambda x: math.sqrt(x))
    data['accmagnitude'] = am
    gx = data['gx'] * data['gx']
    gy = data['gy'] * data['gy']
    gz = data['gz'] * data['gz']
    gm = gx + gy + gz
    gm = gm.apply(lambda x: math.sqrt(x))
    data['gccmagnitude'] = gm
    scaled_training_df = pd.DataFrame(data)
    path=path[21:33]
    scaled_training_df.to_csv("CSV_Dataset_Magnitude/"+path+".csv", index=False)


def Sisfall_analysis():
    path = "Sisfall_dataset/"
    allFiles = glob.glob(path + "*")
    for file_ in allFiles:
        allfiles2 =glob.glob(file_+"/*.txt")
        for file_2 in allfiles2:
            organize_dataset(file_2)
            #calculatemagnitude()
    
Sisfall_analysis()



