#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd

try:
    dt=np.dtype([('x', 'f'), ('y', 'f'), ('z', 'f'), ('pdf', 'f')])
    data=np.fromfile("./loc/global.19050404.005224.grid0.loc.scat", dtype=dt)
    df=pd.DataFrame(data)
    df=df.iloc[1: , :]
    print(df)
except IOError:
    print("Error while opening the file!")


# In[25]:


from scipy.io import loadmat

locs=pd.read_csv('1905Kangra.csv')
loc1=locs.iloc[0:-1, :]
loc2=locs.iloc[-1:]
staloc=pd.read_csv("./loc/last.stations",header=None, sep=' ')

region = [75, 78, 31, 34 ]
topo_data = "@earth_relief_01s" #01s
flt = loadmat('/home/vipin/Documents/GIS2000.mat')


# In[26]:


import pygmt

fig = pygmt.Figure()

# pygmt.makecpt(cmap="gray", series=[-8000, 8000])

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
    # borders='1/1p',
    shorelines=True
)

fig.plot(
    x=flt['x'][0],
    y=flt['y'][0],
    pen="1p,red"
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
    x=loc1.Longitude,
    y=loc1.Latitude,
    style="a0.6",
    color='blue'
)
fig.plot(
    x=loc2.Longitude,
    y=loc2.Latitude,
    style="a0.6",
    color='cyan'
)

fig.text(
    x=locs.Longitude,
    y=locs.Latitude-0.1,
    font="10p,Helvetica,black",
    text=locs.Author
)

with fig.inset(position="jBR+w3c/3c+o0.1c", box="+gwhite+p1p"):
    pygmt.makecpt(cmap="geo", series=[-8000, 8000])
    fig.grdimage(
        grid=topo_data,
        region=[region[0]-5, region[1]+5, region[2]-5, region[3]+5],
        projection='M3c',
        shading=True,
        frame=True,
        cmap=False
    )
    fig.coast(
        region=[region[0]-5, region[1]+5, region[2]-5, region[3]+5],
        projection="M3c",
        # borders=[1, 2],
        shorelines="1/thin",
        water="white",
        # Use dcw to selectively highlight an area
        dcw="US.MA+gred",
    )
    rectangle = [[region[0], region[2], region[1], region[3]]]
    fig.plot(data=rectangle, projection="M3c", style="r+s", pen="1p,red")
fig.show()


# In[4]:


import pygmt    
fig.grdimage(
    grid=topo_data,
    region=[region[0]-2, region[1]+2, region[2]-2.5, region[3]+1.5],
    projection='M15c',
    shading=True,
    frame=True,
    cmap=False
)
fig.coast(
    region=[region[0]-2, region[1]+2, region[2]-2.5, region[3]+1.5],
    projection="M15c",
    # borders=[1, 2],
    shorelines="1/thin",
    water="white",
    # Use dcw to selectively highlight an area
    dcw="US.MA+gred",
)
rectangle = [[region[0], region[2], region[1], region[3]]]
fig.plot(data=rectangle, projection="M15c", style="r+s", pen="1p,red")me="g", land="white", water="skyblue")
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


locs=locs[["Date", "Time", "Latitude", "Longitude", "Depth", "Author" ]]
locs.to_csv("1905Kangra-loc.csv", index=False)


# In[18]:


fig = pygmt.Figure()
fig.grdimage(
    grid=topo_data,
    region=[region[0]-2, region[1]+2, region[2]-2.5, region[3]+1.5],
    projection='M15c',
    shading=True,
    frame=True,
    cmap=False
)
fig.coast(
    region=[region[0]-2, region[1]+2, region[2]-2.5, region[3]+1.5],
    projection="M15c",
    # borders=[1, 2],
    shorelines="1/thin",
    water="white",
    # Use dcw to selectively highlight an area
    dcw="US.MA+gred",
)
rectangle = [[region[0], region[2], region[1], region[3]]]
fig.plot(data=rectangle, projection="M15c", style="r+s", pen="1p,red")
fig.show()


# In[ ]:




