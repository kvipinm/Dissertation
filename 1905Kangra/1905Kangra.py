#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
import pandas as pd

# Create a dtype with the binary data format and the desired column names
try:
    print("reading pdf(.scat) file...")
    dt=np.dtype([('x', 'f'), ('y', 'f'), ('z', 'f'), ('pdf', 'f')])
    data=np.fromfile("./loc/global.19050404.005224.grid0.loc.scat", dtype=dt)
    df=pd.DataFrame(data)
    df=df.iloc[1: , :]
    # print(df)
    #df.to_csv("global.20031203.073729.grid0.loc.scat.asc", sep='\t',index=False)
except IOError:
    print("Error while opening the file!")


# In[50]:


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
region = [74, 79, 30, 35 ]


# In[36]:


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
    # borders='1/1p',
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
    style="c0.06",
    pen="magenta"
)

fig1.plot(
    x=loc1.Longitude,
    y=loc1.Latitude,
    style="a0.6",
    color='blue'
)
fig1.plot(
    x=loc2.Longitude,
    y=loc2.Latitude,
    style="a0.6",
    color='cyan'
)

fig1.text(
    x=locs.Longitude,
    y=locs.Latitude-0.15,
    font="10p,Helvetica,black",
    text=locs.Author
)

with fig1.inset(position="jBR+w3c/3c+o0.1c", box="+gwhite+p1p"):
    fig1.coast(
        # Use a plotting function to create a figure inside the inset
        region=[region[0]-5, region[1]+5, region[2]-5, region[3]+5],
        projection="M3c",
        land="gray",
        borders=[1, 2],
        shorelines="1/thin",
        water="white",
        # Use dcw to selectively highlight an area
        # dcw="US.MA+gred",
    )
    rectangle = [[region[0], region[2], region[1], region[3]]]
    fig1.plot(data=rectangle, projection="M3c", style="r+s", pen="1p,red")
# fig1.show()


# In[46]:


import pygmt

print("plotting stations using pygmt...")
fig2 = pygmt.Figure()
# fig2.coast(projection="E78/36/4.5i", region="g", frame="g", land="white", water="skyblue")
fig2.coast(projection="N78/15c", region="g", frame="ag", land="white", water="skyblue")

fig2.plot(
    x=staloc[1],
    y=staloc[2],
    style="i0.1",
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


# In[54]:


import matplotlib.pyplot as plt

Xm, Ym = 1500, 150
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


# In[44]:


# Save figures to png
print("saving figures...")
fig1.savefig('pdf.png')
fig1.savefig('pdf.pdf')
fig2.savefig('sta.png')
fig2.savefig('sta.pdf')

# To generate a table of time and location of the earthquake
# calculated by various authors
# locs=pd.read_csv("eqdata.csv")
# locs=locs[["Date", "Time", "Latitude", "Longitude", "Depth", "Author" ]]
# locs.to_csv("loctable.csv", index=False)

print("all operation completed.")


# In[ ]:


# Depth distribution
# fig = pygmt.Figure()

# fig.histogram(
#     data=-df.z,
#     # define the frame, add title and set background color to
#     # lightgray, add annotations for x and y axis
#     frame=['WSne+t"Histogram"+gwhite', 'x+l"Depth (km)"', 'y+l"Counts"'],
#     # generate evenly spaced bins by increments of 5
#     series=5,
#     # use red3 as color fill for the bars
#     fill="lightgray",
#     # use a pen size of 1p to draw the outlines
#     pen="1p",
#     # choose histogram type 0 = counts [default]
#     histtype=0,
#     horizontal=True,
#     region="-"+str(Ym)+"/0/0/"+str(Xm)
# )

# # Plot depth from literature

# for dep in loc1.Depth.astype(float):
#     fig.plot(region="0/"+str(Xm)+"/-"+str(Ym)+"/0",
#              frame=False,
#              x=[0, Xm],
#              y=[-dep, -dep],
#              pen="2p,blue")

# print(loc2.Depth)
    
# fig.plot(region="0/"+str(Xm)+"/-"+str(Ym)+"/0",
#         frame=False,
#         x=[0, Xm],
#         y=[-1*loc2.Depth, -1*loc2.Depth],
#         pen="2p,cyan")
# fig.show()


# In[1]:


# import cv2
# import numpy as np

# # load image and get dimensions
# img = cv2.imread("depth_prob.png")
# h, w, c = img.shape

# # create zeros mask 2 pixels larger in each dimension
# mask = np.zeros([h + 2, w + 2], np.uint8)

# # do floodfill
# result = img.copy()
# cv2.floodFill(result, mask, (0,0), (255,255,255), (3,151,65), (3,151,65), flags=8)
# cv2.floodFill(result, mask, (38,313), (255,255,255), (3,151,65), (3,151,65), flags=8)
# cv2.floodFill(result, mask, (363,345), (255,255,255), (3,151,65), (3,151,65), flags=8)
# cv2.floodFill(result, mask, (619,342), (255,255,255), (3,151,65), (3,151,65), flags=8)

# # write result to disk
# cv2.imwrite("soccer_floodfill.png", result)

# # display it
# cv2.imshow("result", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# In[ ]:




