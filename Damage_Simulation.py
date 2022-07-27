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


# Damage Simulation for each building type: this part need to be edited by the user selecting appropriate fragility curve
#===========================================================================
np.random.seed(seed)
node_FC=fc.Fragility()
node_FC.add_dam_state('DS1', 1, {'Default': lognorm(0.13, scale=116.0)})  
node_FC.add_dam_state('DS2', 2, {'Default': lognorm(0.11, scale=134.1)})
node_FC.add_dam_state('DS3', 3, {'Default': lognorm(0.10, scale=151.4)})
node_FC.add_dam_state('DS4', 4, {'Default': lognorm(0.10, scale=167.0)})
idi=node[(node.type=='A2')].id                      # Select appropriate building type here (e.g. A1, A2)
mphi=node[(node.type=='A2')].mph                    # Select appropriate building type here (e.g. A1, A2)
d = {'Id':idi,'mph':mphi}
df=pd.DataFrame(d)
df.set_index('Id');
node_Pr_1 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_1)
node_damage_state_map = node_FC.get_level_map()
node_damage_val1= node_damage_state.map(node_damage_state_map)
id_val1=df.Id

ds1=node_Pr_1.DS1
ds2=node_Pr_1.DS2
ds3=node_Pr_1.DS3
ds4=node_Pr_1.DS4
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
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
node_Pr_2 = node_FC.cdf_probability(df['mph'])
node_damage_state = node_FC.sample_damage_state(node_Pr_2)
node_damage_state_map = node_FC.get_level_map()
node_damage_val2= node_damage_state.map(node_damage_state_map)
id_val2=df.Id

id_val1=id_val1.append(id_val2)
node_damage_val1=node_damage_val1.append(node_damage_val2)
ds1=ds1.append(node_Pr_2.DS1)
ds2=ds2.append(node_Pr_2.DS2)
ds3=ds3.append(node_Pr_2.DS3)
ds4=ds4.append(node_Pr_2.DS4)
#===========================================================================



# Damage Simulation Results:

idd=id_val1
rcc=node_damage_val1
DS1=ds1
DS2=ds2
DS3=ds3
DS4=ds4


sim_data = {'idd':idd,'DS1':DS1,'DS2':DS2,'DS3':DS3,'DS4':DS4, 'dmg_state':rcc}
PDD=pd.DataFrame(sim_data)

PDD.set_index('idd')
DS=PDD.sort_index()
df_dmg=node.merge(DS, left_on='id', right_on='idd')

df_dmg.drop(['idd'], axis=1,inplace=True)
df_dmg['kmh']=df_dmg.mph*1.61

df_dmg['Dislocation'] = df_dmg['dmg_state'].mask(df_dmg.dmg_state>2, 1).mask(df_dmg.dmg_state <=2, 0)