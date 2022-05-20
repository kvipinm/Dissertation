#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

try:
    dt=np.dtype([('x', 'f'), ('y', 'f'), ('z', 'f'), ('pdf', 'f')])
    data=np.fromfile("./loc/global.19990328.190532.grid0.loc.scat", dtype=dt)
    df=pd.DataFrame(data)
    df=df.iloc[1: , :]
    print(df)
except IOError:
    print("Error while opening the file!")


# In[2]:


import pandas as pd
from scipy.io import loadmat

locs=pd.read_csv('1999Chamoli.csv')
loc1=locs.iloc[0:-1, :]
loc2=locs.iloc[-1:]
staloc=pd.read_csv("./loc/last.stations",header=None, sep=' ')

region = [79.1, 79.8, 30.1, 30.8 ]
topo_data = "@earth_relief_01s" #01s
flt = loadmat('/home/vipin/Documents/GIS2000.mat')


# In[5]:


import pygmt

fig = pygmt.Figure()

pygmt.makecpt(cmap="gray", series=[-8000, 8000])

fig.grdimage(
    grid=topo_data,
    region=region,
    projection='M15c',
    shading=True,
    frame=True,
    cmap=True
)

fig.basemap(
    region=region, 
    projection="M15c", 
    frame=True
)

fig.coast(
    water='white',
    borders='1/1p',
    shorelines=True
)

fig.plot(
    x=df.x,
    y=df.y,
    color=df.pdf,
    #cmap=True,
    style="c0.02",
    pen="magenta"
)

fig.plot(
    x=flt['x'][0],
    y=flt['y'][0],
    pen="1p,red"
)

fig.plot(
    x=loc1.Longitude,
    y=loc1.Latitude,
    style="a0.4",
    color='blue'
)
fig.plot(
    x=loc2.Longitude,
    y=loc2.Latitude,
    style="a0.4",
    color='cyan'
)

fig.text(
    x=locs.Longitude+0.03,
    y=locs.Latitude,
    font="7p,Helvetica,black",
    text=locs.Author
)

with fig.inset(position="jBR+w3c/3c+o0.1c", box="+gwhite+p1p"):
    # Use a plotting function to create a figure inside the inset
    fig.coast(
        region=[region[0]-4, region[1]+2.5, region[2]-4, region[3]+2.5],
        projection="M3c",
        land="gray",
        borders=[1, 2],
        shorelines="1/thin",
        water="white",
        # Use dcw to selectively highlight an area
        dcw="US.MA+gred",
    )
    rectangle = [[region[0], region[2], region[1], region[3]]]
    fig.plot(data=rectangle, projection="M3c", style="r+s", pen="1p,red")

fig.show()


# In[3]:


import pygmt

fig = pygmt.Figure()
fig.coast(projection="E78/36/4.5i", region="g", frame="g", land="white", water="skyblue")
fig.plot(
    x=staloc[1],
    y=staloc[2],
    style="i0.1",
    color="red",
    pen="0.001p,black"
)

fig.plot(
    x=loc2.Longitude,
    y=loc2.Latitude,
    style="a0.3",
    color='blue'
)

fig.show()


# In[3]:


df=locs[["Date", "Time", "Latitude", "Longitude", "Depth", "Author" ]]
df.to_csv("1999Chamoli-loc.csv", index=False)


# In[ ]:




