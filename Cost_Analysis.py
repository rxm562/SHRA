import time
import pandas as pd
import numpy as np
import fc
import matplotlib
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
from scipy.spatial import distance
from scipy.stats import expon, lognorm
from pyproj import Proj
from pyproj import Proj, transform
from fc.Fragility import Fragility


np.random.seed(seed)
DRatio=list()
for index, row in df_dmg.iterrows():
    state = row['dmg_state']
    if state==1:
        m=(np.random.normal(0.02, 0.001, 10)).mean()
        if m<0:
            dratio=0
        else:
            dratio=m
    elif state==2:
        dratio=(np.random.normal(0.10, 0.005, 10)).mean()
    elif state==3:
        dratio=(np.random.normal(0.50, 0.025, 10)).mean()
    elif state==4:
        e=(np.random.normal(1.00, 0.050, 10)).mean()
        if e>1.0:
            dratio=1.0
        else:
            dratio=e
    else:
        dratio=0
    dratio
    DRatio.append(dratio)


np.random.seed(seed)
RCost=list()
for index, row in df_dmg.iterrows():
    state = row['dmg_state']
    taxv= row['FINALFULLB'] #Total cost of building
    if state==1:
        m=(np.random.normal(0.02, 0.001, 10)).mean()
        if m<0:
            cost=0*taxv
        else:
            cost=m*taxv
    elif state==2:
        cost=(np.random.normal(0.10, 0.005, 10)).mean()*taxv
    elif state==3:
        cost=(np.random.normal(0.50, 0.025, 10)).mean()*taxv
    elif state==4:
        e=(np.random.normal(1.00, 0.050, 10)).mean()
        if e>1.0:
            cost=1.0*taxv
        else:
            cost=e*taxv
    else:
        cost=0*taxv
    cost
    RCost.append(cost)