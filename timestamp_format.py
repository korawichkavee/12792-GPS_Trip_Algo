import pandas as pd
from datetime import datetime, timedelta, timezone
import os
import winsound

#Importing raw datasets
filename =
path =
df = pd.read_csv(path + '/' + filename)

#Format timestamp to be DateTime
#ms is milisec
df["DateTime"] = pd.to_datetime(df['timestamp'], unit='ms' , origin='unix')

#export
filename =
path =
df.to_csv(path+ "/" + filename + ".csv")

#FINISH
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)