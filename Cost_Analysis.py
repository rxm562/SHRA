import time
import sp
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
from scipy.spatial import distance
from scipy.stats import expon, lognorm
from sp.Intensity import Intensity
from sp.PFragility import plot_FC
from pyproj import Proj
from pyproj import Proj, transform


np.random.seed(seed)
DRatio=list()
for index, row in dmg.iterrows():
    state = row['dmg']
    if state==1:
        m=(np.random.normal(0.02, 0.001, 10)).mean()
        if m<0:
            cost=0
        else:
            cost=m
    elif state==2:
        cost=(np.random.normal(0.10, 0.005, 10)).mean()
    elif state==3:
        cost=(np.random.normal(0.50, 0.025, 10)).mean()
    elif state==4:
        e=(np.random.normal(1.00, 0.050, 10)).mean()
        if e>1.0:
            cost=1.0
        else:
            cost=e
    else:
        cost=0
    cost
    DRatio.append(cost)


np.random.seed(seed)
RCost=list()
for index, row in dmg.iterrows():
    state = row['dmg']
    taxv= row['FINALFULLB']
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