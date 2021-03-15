import pandas as pd
import glob
import os
import numpy as np
import configparser as cp
import math
import matplotlib.pyplot as plt
from scipy import signal

def organize_dataset(path):
    col_names = ["ax","ay","az","gx","gy","gz","acx","acy","acz"]
    data = pd.read_csv(path, names = col_names)
    data = data.replace(';', '.', regex=True)
    data = data.drop('acx', axis=1)
    data = data.drop('acy', axis=1)
    data = data.drop('acz', axis=1)
    data.insert(loc = 0, column = 'time', value=data.index)

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
    for i in ["ax","ay","az","gx","gy","gz","accmagnitude","gccmagnitude"]:
        data[i] = filter(data[i],data['time'],i)
    scaled_training_df = pd.DataFrame(data)
    path=path[21:33]
    scaled_training_df.to_csv("CSV_Dataset_Magnitude/"+path+".csv", index=False)

def filter(Signal,t,i):
    fs = 200
    fc = 5  # Cut-off frequency of the filter
    w = fc / (fs / 2) # Normalize the frequency
    b, a = signal.butter(4, w, 'low')
    output = signal.filtfilt(b, a, Signal)
    return output

def Sisfall_analysis():
    path = "SisFall_dataset/"
    allFiles = glob.glob(path + "*")
    for file_ in allFiles:
        allfiles2 =glob.glob(file_+"/*.txt")
        for file_2 in allfiles2:
            organize_dataset(file_2)
            print("Done: ", file_2)

if __name__ == "__main__":
    if not os.path.exists('CSV_Dataset_Magnitude'):
        os.makedirs('CSV_Dataset_Magnitude')

    Sisfall_analysis()
    



