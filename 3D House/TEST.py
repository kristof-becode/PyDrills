import re
import requests

import os
import numpy as np
import numpy.ma as ma
import pandas as pd
import descartes
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import matplotlib.colors as colors
from matplotlib.colors import ListedColormap
import seaborn as sns

sns.set_style("white")
import geopandas as gpd
import rasterio as rio
from rasterio.mask import mask
from rasterio.plot import show
from shapely.geometry import Polygon

import earthpy as et
import earthpy.plot as ep
import shapely
import plotly.graph_objects as go
from rasterio import Affine as A
from rasterio.warp import calculate_default_transform, reproject, Resampling
"""
address = 'Paal-Dorp 20, 3583 Beringen'
address_regx = re.compile("^([A-z-]+)\s(\d+),\s(\d+)\s([A-z]+)")
result = address_regx.search(address)
street = result.group(1)
nb = result.group(2)
pc = result.group(3)
city = result.group(4)

req = requests.get(
    f"https://api.basisregisters.dev-vlaanderen.be/v1/adresmatch?gemeentenaam={city}&straatnaam={street}&huisnummer={nb}&postcode={pc}").json()

objectId = req["adresMatches"][0]["adresseerbareObjecten"][0]["objectId"]

req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/gebouweenheden/{objectId}").json()

objectId = req["gebouw"]["objectId"]

req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/gebouwen/{objectId}").json()

polygon = [req["geometriePolygoon"]["polygon"]]
print(polygon)

print("Polygon coords : ", polygon[0]['coordinates'][0])
print(type(polygon))

address = 'Paal-Dorp 20, 3583 Beringen'
req = requests.get(f"http://loc.geopunt.be/geolocation/location?q={address}&c=1", )
x = req.json()['LocationResult'][0]['Location']['X_Lambert72']
y = req.json()['LocationResult'][0]['Location']['Y_Lambert72']
print("Lambert72 coords of provided address: x= ", x, " y= ", y)

maps = pd.read_csv('/media/becode/EXT/DSMsplit/dsm.csv', sep= ',')
maps = maps.filename[(maps.left < x) &  (x < maps.right) & (maps.bottom < y) &( y < maps.top)]
path_open = maps.iloc[0]
#path_open = maps[['filename']][(maps.left < x) &  (x < maps.right) & (maps.bottom < y) &( y < maps.top)]
print(maps.iloc[321, 2])
#path = path_open.iloc[0:1]
#path_open = str(maps.filename[(maps.left < x < maps.right) & (maps.bottom < y < maps.top)])
print(path_open.iloc[0])
#map_chm = rio.open(path_open)
"""
path = '/media/becode/EXT/CHMsplit/tile_chm_k22_136.tif'
with rio.open(path) as chm_plot:
    chm =  chm_plot.read(1)
"""
# Define the colors you want
cmap = ListedColormap(["white", "tan", "springgreen", "darkgreen"])

# Define a normalization from values -> colors
norm = colors.BoundaryNorm([0, 2, 10, 20, 30], 5)

fig, ax = plt.subplots(figsize=(10, 5))

chm_plot = ax.imshow(chm,
                     cmap=cmap,
                     norm=norm)

plt.show()
"""
rio.plot.show(chm, cmap='plasma')