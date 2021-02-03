import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as pl
import math
import butter1
from scipy import signal

data = pd.read_csv("CSV_Dataset_Magnitude/F02_SA06_R01.csv")
data1 = pd.read_csv("CSV_Dataset_Magnitude/D03_SA01_R01.csv")
y = data["ay"]
x = data["time"]

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(15, 10), sharex=False)

ax1.plot(x, y)
ax1.set_ylim([min(y) - np.std(y), max(y) + np.std(y)])
ax1.set_xlim([min(x), max(x)])

x = data1["time"]
y = data1["az"]

b, a = signal.butter(4, (2/100), 'low')
y1 = signal.filtfilt(b, a, data1["az"])
ax2.plot(x, y)
ax2.set_ylim([min(y) - np.std(y), max(y) + np.std(y)])
ax2.set_xlim([min(x), max(x)])

ax3.plot(x, y1)
ax3.set_ylim([min(y1) - np.std(y1), max(y1) + np.std(y1)])
ax3.set_xlim([min(x), max(x)])
plt.show()