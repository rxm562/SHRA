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

# Damage Simulation Using Fragility Curves
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=116.0)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.11, scale=134.1)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=151.4)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=167.0)})
idi=node[(node.type=='A2')].id                      # Select appropriate building type here (e.g. A1, A2)
mphi=node[(node.type=='A2')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A2)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA2= node_damage_state.map(node_damage_state_map)
id_valA2=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=120.9)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.11, scale=141.1)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=158.9)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=176.6)})
idi=node[(node.type=='A6')].id
mphi=node[(node.type=='A6')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A6 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A6)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA6= node_damage_state.map(node_damage_state_map)
id_valA6=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=113.57)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=131.31)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=143.45)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=146.74)})
idi=node[(node.type=='A10')].id
mphi=node[(node.type=='A10')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A10 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A10)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA10= node_damage_state.map(node_damage_state_map)
id_valA10=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=118.22)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=138.69)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=153.49)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=158.66)})
idi=node[(node.type=='A14')].id
mphi=node[(node.type=='A14')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A14 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A14)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA14= node_damage_state.map(node_damage_state_map)
id_valA14=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=103.10)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=118.60)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=133.47)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=146.44)})
idi=node[(node.type=='A18')].id
mphi=node[(node.type=='A18')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A18 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A18)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA18= node_damage_state.map(node_damage_state_map)
id_valA18=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=106.63)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=126.51)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=140.68)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=157.88)})
idi=node[(node.type=='A22')].id
mphi=node[(node.type=='A22')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A22 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A22)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA22= node_damage_state.map(node_damage_state_map)
id_valA22=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=102.89)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=118.10)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=129.18)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=133.30)})
idi=node[(node.type=='A26')].id
mphi=node[(node.type=='A26')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A26 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A26)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA26= node_damage_state.map(node_damage_state_map)
id_valA26=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=106.66)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=126.09)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=137.42)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=142.53)})
idi=node[(node.type=='A30')].id
mphi=node[(node.type=='A30')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A30 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A30)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA30= node_damage_state.map(node_damage_state_map)
id_valA30=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=105.3)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=120.9)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=135.0)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=147.9)})
idi=node[(node.type=='A34')].id
mphi=node[(node.type=='A34')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A34 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A34)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA34= node_damage_state.map(node_damage_state_map)
id_valA34=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=109.5)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.11, scale=129.2)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=142.6)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=160.1)})
idi=node[(node.type=='A38')].id
mphi=node[(node.type=='A38')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A38 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A38)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA38= node_damage_state.map(node_damage_state_map)
id_valA38=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=105.6)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=120.5)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=131.1)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=136.0)})
idi=node[(node.type=='A42')].id
mphi=node[(node.type=='A42')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A42 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A42)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA42= node_damage_state.map(node_damage_state_map)
id_valA42=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=109.7)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.11, scale=129.1)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=139.0)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=144.1)})
idi=node[(node.type=='A46')].id
mphi=node[(node.type=='A46')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A46 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A46)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA46= node_damage_state.map(node_damage_state_map)
id_valA46=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=113.63)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=136.38)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=158.00)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=176.68)})
idi=node[(node.type=='A50')].id
mphi=node[(node.type=='A50')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A50 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A50)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA50= node_damage_state.map(node_damage_state_map)
id_valA50=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=117.64)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=139.82)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=160.69)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=179.27)})
idi=node[(node.type=='A54')].id
mphi=node[(node.type=='A54')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A54 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A54)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA54= node_damage_state.map(node_damage_state_map)
id_valA54=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=113.26)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=134.56)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=144.66)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=146.69)})
idi=node[(node.type=='A58')].id
mphi=node[(node.type=='A58')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A58 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A58)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA58= node_damage_state.map(node_damage_state_map)
id_valA58=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=117.68)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=139.27)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=153.16)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=157.78)})
idi=node[(node.type=='A62')].id
mphi=node[(node.type=='A62')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A62 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A62)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA62= node_damage_state.map(node_damage_state_map)
id_valA62=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=117.8)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=147.4)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=175.3)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=207.6)})
idi=node[(node.type=='A66')].id
mphi=node[(node.type=='A66')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A66 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A66)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA66= node_damage_state.map(node_damage_state_map)
id_valA66=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=124.5)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=153.2)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.12, scale=177.4)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.15, scale=224.9)})
idi=node[(node.type=='A70')].id
mphi=node[(node.type=='A70')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A70 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A70)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA70= node_damage_state.map(node_damage_state_map)
id_valA70=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.15, scale=118.2)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=145.4)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.12, scale=166.3)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=175.8)})
idi=node[(node.type=='A74')].id
mphi=node[(node.type=='A74')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A74 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A74)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA74= node_damage_state.map(node_damage_state_map)
id_valA74=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=124.1)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=151.6)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.12, scale=171.4)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=186.4)})
idi=node[(node.type=='A78')].id
mphi=node[(node.type=='A78')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A78 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A78)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA78= node_damage_state.map(node_damage_state_map)
id_valA78=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=116.4)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=139.8)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=160.1)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=184.2)})
idi=node[(node.type=='A82')].id
mphi=node[(node.type=='A82')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A82 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A82)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA82= node_damage_state.map(node_damage_state_map)
id_valA82=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=120.5)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.11, scale=143.2)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=162.9)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=190.2)})
idi=node[(node.type=='A86')].id
mphi=node[(node.type=='A86')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A86 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A86)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA86= node_damage_state.map(node_damage_state_map)
id_valA86=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=116.3)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.11, scale=137.4)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=145.8)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=147.9)})
idi=node[(node.type=='A90')].id
mphi=node[(node.type=='A90')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A90 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A90)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA90= node_damage_state.map(node_damage_state_map)
id_valA90=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=120.9)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=142.4)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=154.4)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=159.3)})
idi=node[(node.type=='A94')].id
mphi=node[(node.type=='A94')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A94 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A94)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA94= node_damage_state.map(node_damage_state_map)
id_valA94=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=117.8)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=147.4)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=175.3)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=207.6)})
idi=node[(node.type=='A98')].id
mphi=node[(node.type=='A98')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A98 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A98)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA98= node_damage_state.map(node_damage_state_map)
id_valA98=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=124.5)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=153.2)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.12, scale=177.4)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.15, scale=224.9)})
idi=node[(node.type=='A102')].id
mphi=node[(node.type=='A102')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A102 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A102)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA102= node_damage_state.map(node_damage_state_map)
id_valA102=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.15, scale=118.2)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=145.4)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.12, scale=166.3)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=175.8)})
idi=node[(node.type=='A106')].id
mphi=node[(node.type=='A106')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A106 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A106)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA106= node_damage_state.map(node_damage_state_map)
id_valA106=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=124.1)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=151.6)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.12, scale=171.4)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=186.4)})
idi=node[(node.type=='A110')].id
mphi=node[(node.type=='A110')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_A110 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_A110)
node_damage_state_map = node_FC.get_level_map()
node_damage_valA110= node_damage_state.map(node_damage_state_map)
id_valA110=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=142.7)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=160.9)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.13, scale=180.6)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.14, scale=188.2)})
idi=node[(node.type=='B3')].id
mphi=node[(node.type=='B3')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_B3 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_B3)
node_damage_state_map = node_FC.get_level_map()
node_damage_valB3= node_damage_state.map(node_damage_state_map)
id_valB3=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=113.93)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=137.45)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=161.16)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.06, scale=185.76)})
idi=node[(node.type=='C14')].id
mphi=node[(node.type=='C14')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_C14 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_C14)
node_damage_state_map = node_FC.get_level_map()
node_damage_valC14= node_damage_state.map(node_damage_state_map)
id_valC14=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=112.7)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=120.2)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.12, scale=132.6)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=144.3)})
idi=node[(node.type=='C15')].id
mphi=node[(node.type=='C15')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_C15 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_C15)
node_damage_state_map = node_FC.get_level_map()
node_damage_valC15= node_damage_state.map(node_damage_state_map)
id_valC15=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=117.4)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=133.5)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=150.0)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=164.6)})
idi=node[(node.type=='C22')].id
mphi=node[(node.type=='C22')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_C22 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_C22)
node_damage_state_map = node_FC.get_level_map()
node_damage_valC22= node_damage_state.map(node_damage_state_map)
id_valC22=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=104.84)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.12, scale=126.33)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.09, scale=149.14)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=160.38)})
idi=node[(node.type=='C24')].id
mphi=node[(node.type=='C24')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_C24 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_C24)
node_damage_state_map = node_FC.get_level_map()
node_damage_valC24= node_damage_state.map(node_damage_state_map)
id_valC24=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=100.16)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.11, scale=119.90)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.09, scale=142.55)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=148.21)})
idi=node[(node.type=='C25')].id
mphi=node[(node.type=='C25')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_C25 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_C25)
node_damage_state_map = node_FC.get_level_map()
node_damage_valC25= node_damage_state.map(node_damage_state_map)
id_valC25=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.14, scale=105.4)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.13, scale=119.1)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.11, scale=132.9)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=145.9)})
idi=node[(node.type=='C26')].id
mphi=node[(node.type=='C26')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_C26 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_C26)
node_damage_state_map = node_FC.get_level_map()
node_damage_valC26= node_damage_state.map(node_damage_state_map)
id_valC26=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.19, scale=120.37)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.19, scale=132.80)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.17, scale=144.93)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.15, scale=151.33)})
idi=node[(node.type=='D10')].id
mphi=node[(node.type=='D10')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_D10 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_D10)
node_damage_state_map = node_FC.get_level_map()
node_damage_valD10= node_damage_state.map(node_damage_state_map)
id_valD10=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.15, scale=112.5)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.14, scale=121.8)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.13, scale=132.7)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.14, scale=149.9)})
idi=node[(node.type=='D18')].id
mphi=node[(node.type=='D18')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_D18 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_D18)
node_damage_state_map = node_FC.get_level_map()
node_damage_valD18= node_damage_state.map(node_damage_state_map)
id_valD18=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.15, scale=112.4)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.14, scale=122.2)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.13, scale=132.5)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.15, scale=150.9)})
idi=node[(node.type=='D33')].id
mphi=node[(node.type=='D33')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_D33 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_D33)
node_damage_state_map = node_FC.get_level_map()
node_damage_valD33= node_damage_state.map(node_damage_state_map)
id_valD33=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.16, scale=128.76)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.15, scale=130.61)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.15, scale=133.78)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.14, scale=151.04)})
idi=node[(node.type=='E6')].id
mphi=node[(node.type=='E6')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_E6 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_E6)
node_damage_state_map = node_FC.get_level_map()
node_damage_valE6= node_damage_state.map(node_damage_state_map)
id_valE6=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.16, scale=120.12)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.16, scale=121.59)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.15, scale=132.01)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.09, scale=178.87)})
idi=node[(node.type=='E7')].id
mphi=node[(node.type=='E7')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_E7 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_E7)
node_damage_state_map = node_FC.get_level_map()
node_damage_valE7= node_damage_state.map(node_damage_state_map)
id_valE7=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.16, scale=103.39)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.16, scale=103.98)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.15, scale=119.89)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.09, scale=169.27)})
idi=node[(node.type=='E8')].id
mphi=node[(node.type=='E8')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_E8 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_E8)
node_damage_state_map = node_FC.get_level_map()
node_damage_valE8= node_damage_state.map(node_damage_state_map)
id_valE8=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.10, scale=108.3)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.08, scale=114.7)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.07, scale=125.6)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.11, scale=200.6)})
idi=node[(node.type=='F9')].id
mphi=node[(node.type=='F9')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_F9 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_F9)
node_damage_state_map = node_FC.get_level_map()
node_damage_valF9= node_damage_state.map(node_damage_state_map)
id_valF9=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.11, scale=102.5)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.09, scale=109.7)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.07, scale=119.9)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=205.1)})
idi=node[(node.type=='F16')].id
mphi=node[(node.type=='F16')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_F16 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_F16)
node_damage_state_map = node_FC.get_level_map()
node_damage_valF16= node_damage_state.map(node_damage_state_map)
id_valF16=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.10, scale=105.1)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.08, scale=112.9)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.08, scale=133.1)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=180.5)})
idi=node[(node.type=='F27')].id
mphi=node[(node.type=='F27')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_F27 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_F27)
node_damage_state_map = node_FC.get_level_map()
node_damage_valF27= node_damage_state.map(node_damage_state_map)
id_valF27=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.10, scale=105.4)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.08, scale=112.7)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.08, scale=133.3)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=180.2)})
idi=node[(node.type=='F34')].id
mphi=node[(node.type=='F34')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_F34 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_F34)
node_damage_state_map = node_FC.get_level_map()
node_damage_valF34= node_damage_state.map(node_damage_state_map)
id_valF34=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=97.5)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.11, scale=105.5)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.08, scale=142.5)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.09, scale=201.1)})
idi=node[(node.type=='F45')].id
mphi=node[(node.type=='F45')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_F45 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_F45)
node_damage_state_map = node_FC.get_level_map()
node_damage_valF45= node_damage_state.map(node_damage_state_map)
id_valF45=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=97.8)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.11, scale=105.5)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.08, scale=142.0)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=201.2)})
idi=node[(node.type=='F52')].id
mphi=node[(node.type=='F52')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_F52 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_F52)
node_damage_state_map = node_FC.get_level_map()
node_damage_valF52= node_damage_state.map(node_damage_state_map)
id_valF52=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.15, scale=105.45)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.15, scale=111.09)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.13, scale=118.92)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=136.03)})
idi=node[(node.type=='G4')].id
mphi=node[(node.type=='G4')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_G4 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_G4)
node_damage_state_map = node_FC.get_level_map()
node_damage_valG4= node_damage_state.map(node_damage_state_map)
id_valG4=df.Id
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.16, scale=120.5)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.14, scale=133.6)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=185.4)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.12, scale=196.0)})
idi=node[(node.type=='G5')].id
mphi=node[(node.type=='G5')].mph
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_G5 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_G5)
node_damage_state_map = node_FC.get_level_map()
node_damage_valG5= node_damage_state.map(node_damage_state_map)
id_valG5=df.Id
#===========================================================================

rcc=node_damage_valA2.append(node_damage_valA6)
DS1=node_Pr_A2.DS1.append(node_Pr_A6.DS1)


#Append all ids
idd=id_valA2.append(id_valA6).append(id_valA10).append(id_valA14).append(id_valA18).append(id_valA22).append(id_valA26).append(id_valA30).append(id_valA34).append(id_valA38).append(id_valA42).append(id_valA46).append(id_valA50).append(id_valA54).append(id_valA58).append(id_valA62).append(id_valA66).append(id_valA70).append(id_valA74).append(id_valA78).append(id_valA82).append(id_valA86).append(id_valA90).append(id_valA94).append(id_valA98).append(id_valA102).append(id_valA106).append(id_valA110).append(id_valB3).append(id_valC14).append(id_valC15).append(id_valC22).append(id_valC24).append(id_valC25).append(id_valC26).append(id_valD10).append(id_valD18).append(id_valD33).append(id_valE6).append(id_valE7).append(id_valE8).append(id_valF9).append(id_valF16).append(id_valF27).append(id_valF34).append(id_valF45).append(id_valF52).append(id_valG4).append(id_valG5)

#Append all damage levels
rcc=node_damage_valA2.append(node_damage_valA6).append(node_damage_valA10).append(node_damage_valA14).append(node_damage_valA18).append(node_damage_valA22).append(node_damage_valA26).append(node_damage_valA30).append(node_damage_valA34).append(node_damage_valA38).append(node_damage_valA42).append(node_damage_valA46).append(node_damage_valA50).append(node_damage_valA54).append(node_damage_valA58).append(node_damage_valA62).append(node_damage_valA66).append(node_damage_valA70).append(node_damage_valA74).append(node_damage_valA78).append(node_damage_valA82).append(node_damage_valA86).append(node_damage_valA90).append(node_damage_valA94).append(node_damage_valA98).append(node_damage_valA102).append(node_damage_valA106).append(node_damage_valA110).append(node_damage_valB3).append(node_damage_valC14).append(node_damage_valC15).append(node_damage_valC22).append(node_damage_valC24).append(node_damage_valC25).append(node_damage_valC26).append(node_damage_valD10).append(node_damage_valD18).append(node_damage_valD33).append(node_damage_valE6).append(node_damage_valE7).append(node_damage_valE8).append(node_damage_valF9).append(node_damage_valF16).append(node_damage_valF27).append(node_damage_valF34).append(node_damage_valF45).append(node_damage_valF52).append(node_damage_valG4).append(node_damage_valG5)

#Append all DS1

DS1=node_Pr_A2.DS1.append(node_Pr_A6.DS1).append(node_Pr_A10.DS1).append(node_Pr_A14.DS1).append(node_Pr_A18.DS1).append(node_Pr_A22.DS1).append(node_Pr_A26.DS1).append(node_Pr_A30.DS1).append(node_Pr_A34.DS1).append(node_Pr_A38.DS1).append(node_Pr_A42.DS1).append(node_Pr_A46.DS1).append(node_Pr_A50.DS1).append(node_Pr_A54.DS1).append(node_Pr_A58.DS1).append(node_Pr_A62.DS1).append(node_Pr_A66.DS1).append(node_Pr_A70.DS1).append(node_Pr_A74.DS1).append(node_Pr_A78.DS1).append(node_Pr_A82.DS1).append(node_Pr_A86.DS1).append(node_Pr_A90.DS1).append(node_Pr_A94.DS1).append(node_Pr_A98.DS1).append(node_Pr_A102.DS1).append(node_Pr_A106.DS1).append(node_Pr_A110.DS1).append(node_Pr_B3.DS1).append(node_Pr_C14.DS1).append(node_Pr_C15.DS1).append(node_Pr_C22.DS1).append(node_Pr_C24.DS1).append(node_Pr_C25.DS1).append(node_Pr_C26.DS1).append(node_Pr_D10.DS1).append(node_Pr_D18.DS1).append(node_Pr_D33.DS1).append(node_Pr_E6.DS1).append(node_Pr_E7.DS1).append(node_Pr_E8.DS1).append(node_Pr_F9.DS1).append(node_Pr_F16.DS1).append(node_Pr_F27.DS1).append(node_Pr_F34.DS1).append(node_Pr_F45.DS1).append(node_Pr_F52.DS1).append(node_Pr_G4.DS1).append(node_Pr_G5.DS1)


#Append all DS2

DS2=node_Pr_A2.DS2.append(node_Pr_A6.DS2).append(node_Pr_A10.DS2).append(node_Pr_A14.DS2).append(node_Pr_A18.DS2).append(node_Pr_A22.DS2).append(node_Pr_A26.DS2).append(node_Pr_A30.DS2).append(node_Pr_A34.DS2).append(node_Pr_A38.DS2).append(node_Pr_A42.DS2).append(node_Pr_A46.DS2).append(node_Pr_A50.DS2).append(node_Pr_A54.DS2).append(node_Pr_A58.DS2).append(node_Pr_A62.DS2).append(node_Pr_A66.DS2).append(node_Pr_A70.DS2).append(node_Pr_A74.DS2).append(node_Pr_A78.DS2).append(node_Pr_A82.DS2).append(node_Pr_A86.DS2).append(node_Pr_A90.DS2).append(node_Pr_A94.DS2).append(node_Pr_A98.DS2).append(node_Pr_A102.DS2).append(node_Pr_A106.DS2).append(node_Pr_A110.DS2).append(node_Pr_B3.DS2).append(node_Pr_C14.DS2).append(node_Pr_C15.DS2).append(node_Pr_C22.DS2).append(node_Pr_C24.DS2).append(node_Pr_C25.DS2).append(node_Pr_C26.DS2).append(node_Pr_D10.DS2).append(node_Pr_D18.DS2).append(node_Pr_D33.DS2).append(node_Pr_E6.DS2).append(node_Pr_E7.DS2).append(node_Pr_E8.DS2).append(node_Pr_F9.DS2).append(node_Pr_F16.DS2).append(node_Pr_F27.DS2).append(node_Pr_F34.DS2).append(node_Pr_F45.DS2).append(node_Pr_F52.DS2).append(node_Pr_G4.DS2).append(node_Pr_G5.DS2)


#Append all DS3

DS3=node_Pr_A2.DS3.append(node_Pr_A6.DS3).append(node_Pr_A10.DS3).append(node_Pr_A14.DS3).append(node_Pr_A18.DS3).append(node_Pr_A22.DS3).append(node_Pr_A26.DS3).append(node_Pr_A30.DS3).append(node_Pr_A34.DS3).append(node_Pr_A38.DS3).append(node_Pr_A42.DS3).append(node_Pr_A46.DS3).append(node_Pr_A50.DS3).append(node_Pr_A54.DS3).append(node_Pr_A58.DS3).append(node_Pr_A62.DS3).append(node_Pr_A66.DS3).append(node_Pr_A70.DS3).append(node_Pr_A74.DS3).append(node_Pr_A78.DS3).append(node_Pr_A82.DS3).append(node_Pr_A86.DS3).append(node_Pr_A90.DS3).append(node_Pr_A94.DS3).append(node_Pr_A98.DS3).append(node_Pr_A102.DS3).append(node_Pr_A106.DS3).append(node_Pr_A110.DS3).append(node_Pr_B3.DS3).append(node_Pr_C14.DS3).append(node_Pr_C15.DS3).append(node_Pr_C22.DS3).append(node_Pr_C24.DS3).append(node_Pr_C25.DS3).append(node_Pr_C26.DS3).append(node_Pr_D10.DS3).append(node_Pr_D18.DS3).append(node_Pr_D33.DS3).append(node_Pr_E6.DS3).append(node_Pr_E7.DS3).append(node_Pr_E8.DS3).append(node_Pr_F9.DS3).append(node_Pr_F16.DS3).append(node_Pr_F27.DS3).append(node_Pr_F34.DS3).append(node_Pr_F45.DS3).append(node_Pr_F52.DS3).append(node_Pr_G4.DS3).append(node_Pr_G5.DS3)


#Append all DS4

DS4=node_Pr_A2.DS4.append(node_Pr_A6.DS4).append(node_Pr_A10.DS4).append(node_Pr_A14.DS4).append(node_Pr_A18.DS4).append(node_Pr_A22.DS4).append(node_Pr_A26.DS4).append(node_Pr_A30.DS4).append(node_Pr_A34.DS4).append(node_Pr_A38.DS4).append(node_Pr_A42.DS4).append(node_Pr_A46.DS4).append(node_Pr_A50.DS4).append(node_Pr_A54.DS4).append(node_Pr_A58.DS4).append(node_Pr_A62.DS4).append(node_Pr_A66.DS4).append(node_Pr_A70.DS4).append(node_Pr_A74.DS4).append(node_Pr_A78.DS4).append(node_Pr_A82.DS4).append(node_Pr_A86.DS4).append(node_Pr_A90.DS4).append(node_Pr_A94.DS4).append(node_Pr_A98.DS4).append(node_Pr_A102.DS4).append(node_Pr_A106.DS4).append(node_Pr_A110.DS4).append(node_Pr_B3.DS4).append(node_Pr_C14.DS4).append(node_Pr_C15.DS4).append(node_Pr_C22.DS4).append(node_Pr_C24.DS4).append(node_Pr_C25.DS4).append(node_Pr_C26.DS4).append(node_Pr_D10.DS4).append(node_Pr_D18.DS4).append(node_Pr_D33.DS4).append(node_Pr_E6.DS4).append(node_Pr_E7.DS4).append(node_Pr_E8.DS4).append(node_Pr_F9.DS4).append(node_Pr_F16.DS4).append(node_Pr_F27.DS4).append(node_Pr_F34.DS4).append(node_Pr_F45.DS4).append(node_Pr_F52.DS4).append(node_Pr_G4.DS4).append(node_Pr_G5.DS4)


# In[81]:


sim_data = {'idd':idd,'DS1':DS1,'DS2':DS2,'DS3':DS3,'DS4':DS4, 'dmg':rcc}
PDD=pd.DataFrame(sim_data)

PDD.set_index('idd')
DS=PDD.sort_index()
dmg=node.merge(DS, left_on='id', right_on='idd')

dmg.drop(['idd'], axis=1,inplace=True)
dmg['kmh']=dmg.mph*1.61

dmg['Dislocation'] = dmg['dmg'].mask(dmg.dmg>2, 1).mask(dmg.dmg <=2, 0)