#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pygmt
import numpy as np
import pandas as pd
from scipy.io import loadmat
import matplotlib.pyplot as plt


# In[48]:


dt=np.dtype([('x', 'f'), ('y', 'f'), ('z', 'f'), ('pdf', 'f')])
pdf45=np.fromfile("1945NandaDevi/loc/global.19450604.120948.grid0.loc.scat", dtype=dt)
pdf45=pd.DataFrame(pdf45)
pdf45=pdf45.iloc[1: , :]

pdf58=np.fromfile("1958Dharchula/loc/global.19581228.053514.grid0.loc.scat", dtype=dt)
pdf58=pd.DataFrame(pdf58)
pdf58=pdf58.iloc[1: , :]

pdf64=np.fromfile("1964Dharchula/loc/global.19640926.004637.grid0.loc.scat", dtype=dt)
pdf64=pd.DataFrame(pdf64)
pdf64=pdf64.iloc[1: , :]

pdf79=np.fromfile("1979Dharchula/loc/global.19790520.225949.grid0.loc.scat", dtype=dt)
pdf79=pd.DataFrame(pdf79)
pdf79=pdf79.iloc[1: , :]


# In[49]:


print("reading locations(.csv) file...")
locs45=pd.read_csv('1945NandaDevi/locs.csv')
loc145=locs45.iloc[0:-1, :]
loc245=locs45.iloc[-1]

locs58=pd.read_csv('1958Dharchula/locs.csv')
loc158=locs58.iloc[0:-1, :]
loc258=locs58.iloc[-1]

locs64=pd.read_csv('1964Dharchula/locs.csv')
loc164=locs64.iloc[0:-1, :]
loc264=locs64.iloc[-1]

locs79=pd.read_csv('1979Dharchula/locs.csv')
loc179=locs79.iloc[0:-1, :]
loc279=locs79.iloc[-1]


# In[50]:


flt = loadmat('/home/vipin/Documents/GIS2000.mat')


# In[56]:


topo_data = "@earth_relief_01s" #01s
region = [79.5, 81, 29.25, 30.75 ]


# In[57]:


print("creating pdf plot using pygmt...")
fig1 = pygmt.Figure()

pygmt.makecpt(cmap="gray", series=[-8000, 8000])

fig1.grdimage(
    grid=topo_data,
    region=region,
    projection='M15c',
    shading=True,
    frame=True,
    cmap=True
)

fig1.basemap(
    region=region, 
    projection="M15c", 
    frame=True
)

fig1.coast(
    water='white',
    borders='1/1p',
    shorelines=True,
    map_scale="jBL+w50k+o0.5c/0.5c+f"
)

fig1.plot(
    x=pdf45.x,
    y=pdf45.y,
    color=pdf45.pdf,
    #cmap=True,
    style="c0.02",
    pen="magenta"
)
fig1.plot(
    x=pdf58.x,
    y=pdf58.y,
    color=pdf58.pdf,
    #cmap=True,
    style="c0.02",
    pen='#234F1E'
)
fig1.plot(
    x=pdf64.x,
    y=pdf64.y,
    color=pdf64.pdf,
    #cmap=True,
    style="c0.02",
    pen="darkorange"
)
fig1.plot(
    x=pdf79.x,
    y=pdf79.y,
    color=pdf79.pdf,
    #cmap=True,
    style="c0.02",
    pen="darkred"
)

fig1.plot(
    x=loc145.Longitude,
    y=loc145.Latitude,
    style="a0.4",
    color='#FC46AA'
)
fig1.plot(
    x=loc158.Longitude,
    y=loc158.Latitude,
    style="a0.4",
    color='#3DED97'
)
fig1.plot(
    x=loc164.Longitude,
    y=loc164.Latitude,
    style="a0.4",
    color='yellow'
)
fig1.plot(
    x=loc179.Longitude,
    y=loc179.Latitude,
    style="a0.4",
    color='red'
)

fig1.plot(
    x=loc245.Longitude,
    y=loc245.Latitude,
    style="a0.5",
    color='cyan'
)
fig1.plot(
    x=loc258.Longitude,
    y=loc258.Latitude,
    style="a0.5",
    color='cyan'
)
fig1.plot(
    x=loc264.Longitude,
    y=loc264.Latitude,
    style="a0.5",
    color='cyan'
)
fig1.plot(
    x=loc279.Longitude,
    y=loc279.Latitude,
    style="a0.5",
    color='cyan'
)


fig1.plot(
    x=flt['x'][0],
    y=flt['y'][0],
    pen="1p,red"
)

fig1.text(
    x=locs45.Longitude,
    y=locs45.Latitude-0.02,
    font="7p,Helvetica,black",
    text=locs45.Author
)
fig1.text(
    x=locs58.Longitude,
    y=locs58.Latitude-0.02,
    font="7p,Helvetica,black",
    text=locs58.Author
)
fig1.text(
    x=locs64.Longitude+0.07,
    y=locs64.Latitude,
    font="7p,Helvetica,black",
    text=locs64.Author
)
fig1.text(
    x=locs79.Longitude+0.07,
    y=locs79.Latitude,
    font="7p,Helvetica,black",
    text=locs79.Author
)

with fig1.inset(position="jBR+w3c/3c+o0.1c", box="+gwhite+p1p"):
    fig1.coast(
        region=[region[0]-2.5, region[1]+2.5, region[2]-2.5, region[3]+2.5],
        projection="M3c",
        land="gray",
        borders=[1, 2],
        shorelines="1/thin",
        water="white",
        # Use dcw to selectively highlight an area
        dcw="US.MA+gred",
    )
    rectangle = [[region[0], region[2], region[1], region[3]]]
    fig1.plot(data=rectangle, projection="M3c", style="r+s", pen="1p,red")

fig1.savefig('Dharchula_pdf_samples.png')
fig1.show()


# In[ ]:




