#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
import pandas as pd

try:
    dt=np.dtype([('x', 'f'), ('y', 'f'), ('z', 'f'), ('pdf', 'f')])
    data=np.fromfile("loc/global.19911019.212329.grid0.loc.scat", dtype=dt)
    df=pd.DataFrame(data)
    df=df.iloc[1: , :]
    # print(df)
except IOError:
    print("Error while opening the file!")


# In[40]:


from scipy.io import loadmat

locs=pd.read_csv('1991UttarKashi.csv')
loc1=locs.iloc[0:-1, :]
loc2=locs.iloc[-1]

staloc=pd.read_csv("./loc/last.stations",header=None, sep=' ')
staloc = staloc.drop(staloc[staloc[1] < -180].index)

region = [78.70, 79.10, 30.65, 31.05 ]
topo_data = "@earth_relief_01s"
flt = loadmat('/home/vipin/Documents/GIS2000.mat')


# In[3]:


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
    x=flt['x'][0],
    y=flt['y'][0],
    pen="1p,red"
)

fig.plot(
    x=df.x,
    y=df.y,
    color=df.pdf,
    #cmap=True,
    style="c0.04",
    pen="magenta"
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
    x=locs.Longitude+0.02,
    y=locs.Latitude,
    font="7p,Helvetica,black",
    text=locs.Author
)

with fig.inset(position="jBR+w3c/3c+o0.1c", box="+gwhite+p1p"):
    # Use a plotting function to create a figure inside the inset
    fig.coast(
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
    fig.plot(data=rectangle, projection="M3c", style="r+s", pen="1p,red")

fig.show()


# In[4]:


fig = pygmt.Figure()
#fig.coast(projection="G78/36/4.5i", region="g", frame="g", land="white", water="skyblue")
fig.coast(projection="N78/15c", region="g", frame="g", land="white", water="skyblue")

fig.plot(
    x=staloc[1],
    y=staloc[2],
    style="i0.15",
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
df.to_csv("1991UttarKashi-loc.csv", index=False)


# In[38]:


# Depth distribution
fig = pygmt.Figure()
Xm = 1300
Ym = 200

fig.histogram(
    data=-df.z,
    # define the frame, add title and set background color to
    # lightgray, add annotations for x and y axis
    frame=['WSne+t"Histogram"+gwhite', 'x+l"Depth (km)"', 'y+l"Counts"'],
    # generate evenly spaced bins by increments of 5
    series=5,
    # use red3 as color fill for the bars
    fill="lightgray",
    # use a pen size of 1p to draw the outlines
    pen="1p",
    # choose histogram type 0 = counts [default]
    histtype=0,
    horizontal=True,
    region="-"+str(Ym)+"/0/0/"+str(Xm)
)

# Plot depth from literature

for dep in loc1.Depth.astype(float):
    fig.plot(region="0/"+str(Xm)+"/-"+str(Ym)+"/0",
             frame=False,
             x=[0, Xm],
             y=[-dep, -dep],
             pen="2p,blue")

print(loc2.Depth)
    
fig.plot(region="0/"+str(Xm)+"/-"+str(Ym)+"/0",
        frame=False,
        x=[0, Xm],
        y=[-1*loc2.Depth, -1*loc2.Depth],
        pen="2p,cyan")
fig.show()


# In[ ]:




