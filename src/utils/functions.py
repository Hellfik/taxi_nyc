
import numpy as np
from math import sin, cos, sqrt, atan2, radians

def haversine(lat1, lon1, lat2, lon2, to_radians=True, earth_radius=6371):
    """
        Calcul la distance entre deux points géospatiaux en connaissant leur latitude et leur longitude
    """
    if to_radians:
        lat1, lon1, lat2, lon2 = np.radians([lat1, lon1, lat2, lon2])

    a = np.sin((lat2-lat1)/2.0)**2 + \
        np.cos(lat1) * np.cos(lat2) * np.sin((lon2-lon1)/2.0)**2

    return earth_radius * 2 * np.arcsin(np.sqrt(a))


def vitesse_trajet(distance, temps ):     
    """Retourne la vitesse entre les le début et la fin du trajet."""     
    res = (distance * 1000)/ temps     
    kmh = res * 3.6      
    return kmh