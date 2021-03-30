import pandas as pd
import csv
from datetime import datetime
from time import *

from src.utils.functions import *



df = pd.read_csv('/home/apprenant/Desktop/FARIZD/taxi_nyc/taxi_nyc/Data/row_data/train.csv')

df.head()

df.dtypes

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], format="%Y-%m-%d %H:%M:%S")
df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'], format="%Y-%m-%d %H:%M:%S")

df.dtypes

df['trip_duration']= df['trip_duration'].apply(lambda x :strftime('%H:%M:%S', gmtime(x)))

df.dtypes

df = df.sample(n=100000)

df.isnull().sum()

df.duplicated().sum()


df['distance'] = haversine(df.pickup_latitude, df.pickup_longitude, df.dropoff_latitude, df.dropoff_longitude)

df["distance"] = df["distance"].round(3)

df.head()