#Importing Package
import numpy as np
import pandas as pd
from datetime import datetime, timedelta, timezone
import os
import winsound
print("all libraries are loaded!")

#Importing raw datasets
year_ls = [2019,2020]
for year in range(len(year_ls)):
    for x in range(100):
        folder_1 = 'pit-'+str(year_ls[year]) #2019 and 2020
        filename = "gw-geo-pit-mar-nov-"+str(year_ls[year])+"-0000000000"+"{0:0=2d}".format(x)+".csv" #from 00 to 99
        df_tempo = pd.read_csv(folder_1 + '/' + filename)
        print(filename)

        #Format timestamp to be DateTime
        df_tempo["DateTime"] = pd.to_datetime(df_tempo['timestamp'], unit='ms' , origin='unix')

        #Remove fileds not needed
        df_tempo = df_tempo.drop(columns=['timestamp', 'altitude'])

        #clean speed = -1
        df_tempo = df_tempo[df_tempo['speed'] != -1]

        #clean heading = -1
        df_tempo = df_tempo[df_tempo['heading'] != -1]

        if x == 0 and year == 0:
            df = df_tempo
        df = df.append(df_tempo)

del df_tempo

#make a list of driver_id
d_list = df['driver_id'].unique()
d_list = d_list.tolist()

for d_id in range(len(d_list)):
    print(d_id)
    #lets pick a driver_id
    example_person = d_list[d_id]
    print(example_person)
    df_indi = df[df['driver_id']== example_person]

    # To Create Directory If Not Exist
    # https://appdividend.com/2021/07/03/how-to-create-directory-if-not-exist-in-python/
    folder_2 = "pitt-DriverID"
    path = folder_2
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=False)

    #export
    df_indi.to_csv(path+ "/" + example_person + ".csv")

#FINISH
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)