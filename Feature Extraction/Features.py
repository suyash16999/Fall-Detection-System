import pandas as pd
import glob
import os,csv
from scipy.stats import skew, kurtosis
import math
import numpy as np
import configparser as cp
from statsmodels.tsa import stattools
import entropy as ent

#Sliding window with 50% overlap. Feature extraction can be tried for different window widths(d) to observe which one gives better results
def slot(timestamp,d=2000):
    start = 0;
    size = timestamp.count();
    print(size)
    while (start < size):
        end = start + d
        yield start, end
        start = start + int(d/2)

def getfeatures(data,start,end,axis):
    sqd_error = (data[start:end] - data[start:end].mean()) ** 2
    features = [
        data[start:end].mean(),
        data[start:end].std(),
        data[start:end].var(),
        data[start:end].min(),
        data[start:end].max(),
        skew(data[start:end]),
        kurtosis(data[start:end]),
        #math.sqrt(sqd_error.mean())
    ]
    if axis=='accmagnitude' or axis=='gccmagnitude':
        print("successful")
        features.append(ent.spectral_entropy(data[start:end], 200, method='fft'))
    print(features)
    return features

def features(data):
    for (start, end) in slot(data['time']):
        features = []
        for axis in ['ax', 'ay', 'az','gx','gy','gz','accmagnitude', 'gccmagnitude']:
            features += getfeatures(data[axis], start, end, axis)
        yield features

def get_activity(filepath):

    activity=filepath[22:]
    activity=activity[:1]
    if activity =='D':
        return 0.0
    elif activity=='F':
        return 1.0
    else:
        print("Invalid File Name")


with open('Extracted_Features.csv', 'w') as out:
    rows = csv.writer(out)   
    path = "CSV_Dataset_Magnitude/"
    allFiles = glob.glob(path + "*.csv")
    for file_ in allFiles:
        activity = get_activity(file_)
        for d in features(pd.read_csv(file_)):
            rows.writerow([activity] + d)
