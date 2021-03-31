import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import sys
from math import sin, cos, sqrt, atan2, radians
#from src.utils.functions import *


df = pd.read_csv('/home/apprenant/Desktop/FARIZD/taxi_nyc/taxi_nyc/Data/row_data/train.csv')

"""
    Data exploration sur un echantillon de 100,000 lignes
"""

df = df.sample(n=100000)
df.shape #100,000 lignes, 11 colonnes
df.dtypes
#id => Object,
#vendor_id => int64
#pickup_datetime => object
#dropoff_datetime => object
#passenger_count => int64
#pickup_longitude => float64
#pickup_latitude => float64
#dropoff_longitude => float64
#dropff_latitude => float
#store_and_fwd_flag => object
#trip_duration => int

"""
Changement du type des colonnes pickup_datetime et dropoff_datetime en type datetime
"""

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], format="%Y-%m-%d %H:%M:%S")
df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'], format="%Y-%m-%d %H:%M:%S")
df.dtypes
#id => Object,
#vendor_id => int64
#pickup_datetime => datetime[ns]
#dropoff_datetime => datetime[ns]
#passenger_count => int64
#pickup_longitude => float64
#pickup_latitude => float64
#dropoff_longitude => float64
#dropff_latitude => float
#store_and_fwd_flag => object
#trip_duration => int


"""
Verification sur le dataset pour reperer les doublons
"""
df.duplicated().sum()
# There are no duplicate value in this dataset


"""
Ajout d'une colonne calculant la distance de chaque trajet
"""

def haversine(lat1, lon1, lat2, lon2, to_radians=True, earth_radius=6371):
    """
        Calcul la distance entre deux points géospatiaux en connaissant leur latitude et leur longitude
    """
    if to_radians:
        lat1, lon1, lat2, lon2 = np.radians([lat1, lon1, lat2, lon2])

    a = np.sin((lat2-lat1)/2.0)**2 + \
        np.cos(lat1) * np.cos(lat2) * np.sin((lon2-lon1)/2.0)**2

    return earth_radius * 2 * np.arcsin(np.sqrt(a))


df['distance'] = haversine(df.pickup_latitude, df.pickup_longitude, df.dropoff_latitude, df.dropoff_longitude)
df["distance"] = df["distance"].round(3)


"""
INDICATOR 1 : la vitesse moyenne de chaque trajet (en km/h)
"""

def vitesse_trajet(distance, temps ):     
    """Retourne la vitesse entre les le début et la fin du trajet."""     
    res = (distance * 1000)/ temps     
    kmh = res * 3.6      
    return kmh
df['vitesse_moyenne'] = vitesse_trajet(df.distance, df.trip_duration)


"""
INDICATOR 2 : le nombre de trajets effectués en fonction du jour de la semaine
"""

# Pour avoir le nom du jour, plutot qu'un numéro
df['weekday'] = df.pickup_datetime.dt.weekday()
df['weekday'].value_counts()

"""
INDICATOR 3 : le nombre de trajets effectués en fonction de l’horaire de la journée par tranche de 4h.
"""

df.groupby(pd.Grouper(key='pickup_datetime',freq='4H'))['id'].count()


"""
INDICATOR 4 : le nombre de km parcourus par jour de la semaine
"""

df1 = df.drop(df[df["vitesse_moyenne"] == 0].index)
df1 = df.drop(df[df["vitesse_moyenne"] > 100].index)

#Nombre de km par jour de la semaine
df.groupby('weekday')['distance'].sum()

print(df.head())

df.to_csv('/home/apprenant/Desktop/FARIZD/taxi_nyc/taxi_nyc/Data/intermediate_data/train.csv')

