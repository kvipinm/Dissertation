#!/usr/bin/env python
# coding: utf-8

# plot.ipynb : Vipin Maurya
# jupyter-nbconvert --to pdfviahtml plot.ipynb
import pandas as pd
import pygmt

loc = pd.read_csv('loc.csv')
loc


region = [65, 95, 10, 35 ]
fig = pygmt.Figure()
fig.basemap(region=region, projection="M15c", frame=True)
fig.coast(land="white", water="skyblue")
pygmt.makecpt(cmap="viridis", series=[loc.longitude.min(), loc.longitude.max()])
fig.plot(
    x=loc.longitude,
    y=loc.latitude,
    color=loc.longitude,
    cmap=True,
    style="a0.3c",
    pen="black"
)
fig.text(text=loc.Author, x=loc.longitude, y=loc.latitude)
fig.colorbar(frame='af+l"Longitude (km)"')
fig.show()

fig = pygmt.Figure()
# Orthographic
fig.coast(projection="G86/26/12c", region="g", frame="g", land="white", water="skyblue")
fig.plot(
    x=loc.longitude,
    y=loc.latitude,
    style="a0.3c",
    color="red",
    pen="black"
)
fig.show()


data = pd.read_csv('data.csv')
data


region = [
    data.Longitude.min() - 1,
    data.Longitude.max() + 1,
    data.Latitude.min() - 1,
    data.Latitude.max() + 1,
]
fig = pygmt.Figure()
# Orthographic
# fig.basemap(
# #     # set map limits to theta_min = 0, theta_max = 90, radius_min = 3480,
# #     # radius_max = 6371 (Earth's radius)
#     region=[0, 360, 0, 6371],
# #     region = region,
#     # set map width to 5 cm and interpret input data as geographic azimuth instead
#     # of standard angle, rotate coordinate system counterclockwise by 45 degrees
#     projection="P5c+a+t45",
#     # set the frame and color
#     frame=["xa30f", "ya", "WNse+gbisque"],
# )
fig.coast(projection="G86/26/12c", region="g", frame="g", land="white", water="skyblue")
fig.plot(
    x=loc.longitude,
    y=loc.latitude,
    color="red",
    style="a0.3c",
    pen="black"
)
fig.plot(
    x=data.Longitude,
    y=data.Latitude,
    style="i0.3c",
    color="violet",
    pen="black"
)
fig.show()

