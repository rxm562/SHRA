import time
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
from scipy.spatial import distance
from scipy.stats import expon, lognorm



Vmph=list()          #Gradient Wind Speed (mph)
for index, row in n.iterrows():
    Lat_HE = row['Lat']*3.141592654/180
    Long_HE = row['Long']*3.141592654/180
    ρ = row['ρ']
    B = row['B']
    Rmax = row['Rmax']*1000
    CP = row['CP']
    Δp = row['Δp']*100
    Vmph1=list()
    Vmph.append(Vmph1)
    for index, row in blg.iterrows():
        Lat = row['y']
        Long = row['x']
        Lat_rad = Lat*3.141592654/180
        Long_rad= Long*3.141592654/180
        delLat=Lat_HE-Lat_rad
        delLong=Long_HE-Long_rad
        a=np.sin(delLat/2)**2+np.cos(Lat_HE)*np.cos(Lat_rad)*np.sin(delLong/2)**2
        rr=2*6373*np.arcsin(np.sqrt(a))
        r=rr*1000 #distance from hurricane eye to building
        f=2*0.000073*np.sin(Lat_rad) # Coriolis parameter
        Vg=float(np.sqrt((((Rmax/r)**B)*((B*Δp*np.exp(-(Rmax/r)**B))/ρ))+((r**2)*(f**2)*0.25))-(r*f/2)) #Gradient Wind Speed
        V=Vg*2.2369362920544 #m/s to mph
        Vmph1.append(V)


VG=pd.DataFrame(Vmph)
VG1=pd.DataFrame(Vmph)*1.287*1.61 # Converting Gradient wind speed to Gust wind speed
Vg=VG.T


V3s=Vg.max(axis=1)*1.287
V3=list(blg.id)
vv= list(V3s.values)
pf = {'ind':V3,'mph':vv}
nn=pd.DataFrame(pf)


BlgW=blg.merge(nn, left_on='id', right_on='ind')