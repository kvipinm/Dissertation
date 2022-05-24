#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd

try:
    print("reading pdf(.scat) file...")
    dt=np.dtype([('x', 'f'), ('y', 'f'), ('z', 'f'), ('pdf', 'f')])
    data=np.fromfile("loc/global.19911019.212329.grid0.loc.scat", dtype=dt)
    df=pd.DataFrame(data)
    df=df.iloc[1: , :]
    # print(df)
except IOError:
    print("Error while opening the file!")


# In[12]:


from scipy.io import loadmat

print("reading locations(.csv) file...")
locs=pd.read_csv('locs.csv')
loc1=locs.iloc[0:-1, :]
loc2=locs.iloc[-1]

print("reading stations(.stations) file...")
staloc=pd.read_csv("./loc/last.stations",header=None, sep=' ')
staloc = staloc.drop(staloc[staloc[1] < -180].index)

print("reading faults(.mat) file...")
flt = loadmat('/home/vipin/Documents/GIS2000.mat')

topo_data = "@earth_relief_01s" #01s
region = [78.70, 79.10, 30.65, 31.05 ]


# In[13]:


import pygmt

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
    shorelines=True
)

fig1.plot(
    x=flt['x'][0],
    y=flt['y'][0],
    pen="1p,red"
)

fig1.plot(
    x=df.x,
    y=df.y,
    color=df.pdf,
    #cmap=True,
    style="c0.04",
    pen="magenta"
)

fig1.plot(
    x=loc1.Longitude,
    y=loc1.Latitude,
    style="a0.4",
    color='blue'
)
fig1.plot(
    x=loc2.Longitude,
    y=loc2.Latitude,
    style="a0.4",
    color='cyan'
)

fig1.text(
    x=locs.Longitude+0.02,
    y=locs.Latitude,
    font="7p,Helvetica,black",
    text=locs.Author
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

# fig1.show()


# In[4]:


print("plotting stations using pygmt...")
fig2 = pygmt.Figure()
#fig2.coast(projection="G78/36/4.5i", region="g", frame="g", land="white", water="skyblue")
fig2.coast(projection="N78/15c", region="g", frame="g", land="white", water="skyblue")

fig2.plot(
    x=staloc[1],
    y=staloc[2],
    style="i0.15",
    color="red",
    pen="0.001p,black"
)

fig2.plot(
    x=loc2.Longitude,
    y=loc2.Latitude,
    style="a0.3",
    color='blue'
)
# fig2.show()


# In[6]:


import matplotlib.pyplot as plt

Xm, Ym = 1300, 200
psum=sum(df.pdf)

print("creating depth-probability plot...")
plt.rcParams["figure.figsize"] = (10, 15)

plt.hist(
    df.z,
    weights=df.pdf/psum,
    bins=int(Ym/5),
    orientation="horizontal",
    range=[0, Ym],
    color='gray',
    histtype='bar',
    ec='black'
)

for dep in loc1.Depth:
    plt.axhline(y=dep, color='blue')
plt.axhline(y=loc2.Depth, color='cyan')

plt.ylim(ymin=0)
# plt.title('Title',fontsize=30)
plt.xlabel('Probability')
plt.ylabel('Depth') #,fontsize=30)
# plt.legend(loc='upper right',fontsize=30)
# plt.xticks(fontsize = 20) 
# plt.yticks(fontsize = 20) 

ax=plt.gca()                            # get the axis
ax.set_ylim(ax.get_ylim()[::-1])        # invert the axis
ax.xaxis.tick_top()                     # and move the X-Axis    
ax.xaxis.set_label_position('top')

plt.savefig('depth_prob.pdf')
# plt.savefig('depth_prob.png')
plt.savefig('depth_prob.png', bbox_inches='tight')
# plt.show() 


# In[14]:


# Save figures to png
print("saving figures...")
fig1.savefig('pdf.png')
# fig1.savefig('pdf.pdf')
fig2.savefig('sta.png')
# fig2.savefig('sta.pdf')

# To generate a table of time and location of the earthquake
# calculated by various authors
# locs=pd.read_csv("eqdata.csv")
# locs=locs[["Date", "Time", "Latitude", "Longitude", "Depth", "Author" ]]
# locs.to_csv("loctable.csv", index=False)

print("all operation completed.")


# In[ ]:




