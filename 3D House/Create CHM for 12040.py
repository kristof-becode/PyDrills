import os
import numpy as np
import descartes
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
import geopandas as gpd
import rasterio as rio
import earthpy as et
import earthpy.plot as ep
import requests
import re
import numpy as np
import numpy.ma as ma
from rasterio.mask import mask
from shapely.geometry import Polygon
import plotly.graph_objects as go
import pandas as pd
pd.set_option('display.width',400)
pd.set_option('display.max_columns', 40)
"""
for i in range(0,1):

    path_in_dsm = "/media/becode/EXT/DSM_split/tile_12040.tif"

    with rio.open(path_in_dsm) as plot_dsm :
        dsm = plot_dsm.read(1, masked = True)
        dsm.meta = plot_dsm.profile


    path_in_dtm = "/media/becode/EXT/DTM_split/tile_12040.tif"

    with rio.open(path_in_dtm) as plot_dtm:
        dtm = plot_dtm.read(1, masked =True)

    chm = dsm -dtm

    plot_dsm.close()
    plot_dtm.close()

    path_out_chm = "/media/becode/EXT/CHMtile_12040.tif"
    #with rio.open(path_out_chm, "w", **metadata) as dest:
        #dest.write(img)
    with rio.open(path_out_chm, "w", **dsm.meta) as ff:
        ff.write(chm, 1)
    ff.close()


address = 'Sint-Pietersvliet 7, 2000 Antwerpen'
address_regx = re.compile("^([A-z-]+)\s(\d+),\s(\d+)\s([A-z]+)")
result = address_regx.search(address)
street = result.group(1)
nb = result.group(2)
pc = result.group(3)
city = result.group(4)

req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/adresmatch?gemeentenaam={city}&straatnaam={street}&huisnummer={nb}&postcode={pc}").json()

objectId = req["adresMatches"][0]["adresseerbareObjecten"][0]["objectId"]

req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/gebouweenheden/{objectId}").json()

objectId = req["gebouw"]["objectId"]

req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/gebouwen/{objectId}").json()

polygon = [req["geometriePolygoon"]["polygon"]]
print(polygon)
"""

pol = [{'coordinates': [[[152234.7539967969, 212884.87605375424], [152234.82894080132, 212884.9189977534], [152234.7067647949, 212885.13282175362], [152234.54202879965, 212885.42107775435], [152221.9368447885, 212878.215253748], [152216.66906878352, 212875.20392574742], [152215.47796478122, 212874.52302974463], [152215.7520127818, 212874.04302974418], [152215.85204478353, 212874.10197374597], [152216.04097278416, 212873.7709657438], [152225.4219647944, 212857.33397373557], [152225.34394878894, 212857.28994173557], [152231.24206079543, 212846.96808572486], [152231.36404479295, 212847.0380377248], [152246.52404480428, 212820.42696570978], [152246.43796480447, 212820.37493370846], [152246.70881280303, 212819.90990970656], [152246.73498880863, 212819.8649817072], [152246.9969408065, 212820.01717370749], [152247.5319168046, 212820.3279577084], [152249.9582208097, 212816.06210170686], [152251.11796481162, 212814.0229977034], [152251.02298881114, 212814.00994170457], [152251.31399680674, 212813.5079897046], [152268.9353088215, 212823.58363771066], [152268.96398082376, 212823.60002170876], [152268.93748482317, 212823.64891771227], [152268.69492482394, 212824.0969177112], [152268.59905282408, 212824.04501371086], [152267.0589568168, 212826.7189337127], [152264.98196481913, 212830.32507771626], [152265.57895682007, 212830.66510971636], [152265.7790208161, 212830.7790297158], [152265.76641281694, 212830.80117371678], [152265.50599681586, 212831.2580057159], [152265.41204481572, 212831.20398971438], [152255.79194881022, 212847.97896572575], [152255.90804481506, 212848.04699772596], [152253.85601281375, 212851.56002172828], [152253.7879808098, 212851.52002172917], [152250.20596481115, 212857.8059737347], [152250.2789888084, 212857.8480217345], [152246.09703680873, 212865.1149657406], [152246.01594880223, 212865.06894974038], [152244.21095680445, 212868.27803774178], [152244.29594880342, 212868.32699774206], [152242.26292480528, 212871.89698174223], [152242.18196479976, 212871.85096574202], [152234.7539967969, 212884.87605375424]]], 'type': 'Polygon'}]

pol22 = [{'coordinates': [[[206556.84286634624, 192353.51987956092], [206543.3967223391, 192360.54765556753], [206540.0063863322, 192354.3565515615], [206542.11006633192, 192353.20455156267], [206542.57630633563, 192351.727815561], [206545.65553833544, 192341.97523955256], [206558.30577834696, 192345.52717555687], [206559.19896234572, 192345.77799155563], [206558.13899434358, 192352.5139915608], [206558.24894634634, 192352.78496756032], [206556.84286634624, 192353.51987956092]]], 'type': 'Polygon'}]


#print(polygon)

#try and cut out polygon from raster :
path_chm = "/media/becode/EXT/CHMtile_12040.tif"
#with rio.open(path_chm) as plot_chm:
    #chm = plot_chm.read(1)
plot_chm = rio.open(path_chm)

#show((plot_chm, 1), cmap='terrain')
#out_img, out_transform = mask(dataset=plot_chm, shapes=polygon, crop=True)
crop_chm_img, crop_chm_transform = mask(dataset=plot_chm, shapes=pol, crop=True, nodata=0, filled=True, indexes=1)
#NO ZEROS FOR MEAN WITH MASK
z = ma.masked_values(crop_chm_img, 0)
print(z)
print(np.mean(z))
#MASK ZOALS BOVEN WERKT BETER VOOR MEAN
no_zeros1 = np.argwhere(crop_chm_img)
no_zeros2 = np.where(crop_chm_img != 0)
print(no_zeros1)
mean_height1 = np.mean(no_zeros1)
mean_height2 = np.mean(no_zeros2)
print(mean_height1,mean_height2 ) # is eigenlijk te hoog!!!
print(np.max(crop_chm_img))
print(np.min(crop_chm_img))

#show((crop_chm_img, 1), cmap='terrain')
#ep.plot_bands(crop_chm_img, title="CHM", cmap="viridis")
#plt.show()

#poly voor nummer 22
#polygon = Polygon([(206556.84286634624, 192353.51987956092), (206543.3967223391, 192360.54765556753), (206540.0063863322, 192354.3565515615), (206542.11006633192, 192353.20455156267), (206542.57630633563, 192351.727815561), (206545.65553833544, 192341.97523955256), (206558.30577834696, 192345.52717555687), (206559.19896234572, 192345.77799155563), (206558.13899434358, 192352.5139915608), (206558.24894634634, 192352.78496756032), (206556.84286634624, 192353.51987956092)])
#poly voor nummer 20
polygon = Polygon([[152234.7539967969, 212884.87605375424], [152234.82894080132, 212884.9189977534], [152234.7067647949, 212885.13282175362], [152234.54202879965, 212885.42107775435], [152221.9368447885, 212878.215253748], [152216.66906878352, 212875.20392574742], [152215.47796478122, 212874.52302974463], [152215.7520127818, 212874.04302974418], [152215.85204478353, 212874.10197374597], [152216.04097278416, 212873.7709657438], [152225.4219647944, 212857.33397373557], [152225.34394878894, 212857.28994173557], [152231.24206079543, 212846.96808572486], [152231.36404479295, 212847.0380377248], [152246.52404480428, 212820.42696570978], [152246.43796480447, 212820.37493370846], [152246.70881280303, 212819.90990970656], [152246.73498880863, 212819.8649817072], [152246.9969408065, 212820.01717370749], [152247.5319168046, 212820.3279577084], [152249.9582208097, 212816.06210170686], [152251.11796481162, 212814.0229977034], [152251.02298881114, 212814.00994170457], [152251.31399680674, 212813.5079897046], [152268.9353088215, 212823.58363771066], [152268.96398082376, 212823.60002170876], [152268.93748482317, 212823.64891771227], [152268.69492482394, 212824.0969177112], [152268.59905282408, 212824.04501371086], [152267.0589568168, 212826.7189337127], [152264.98196481913, 212830.32507771626], [152265.57895682007, 212830.66510971636], [152265.7790208161, 212830.7790297158], [152265.76641281694, 212830.80117371678], [152265.50599681586, 212831.2580057159], [152265.41204481572, 212831.20398971438], [152255.79194881022, 212847.97896572575], [152255.90804481506, 212848.04699772596], [152253.85601281375, 212851.56002172828], [152253.7879808098, 212851.52002172917], [152250.20596481115, 212857.8059737347], [152250.2789888084, 212857.8480217345], [152246.09703680873, 212865.1149657406], [152246.01594880223, 212865.06894974038], [152244.21095680445, 212868.27803774178], [152244.29594880342, 212868.32699774206], [152242.26292480528, 212871.89698174223], [152242.18196479976, 212871.85096574202], [152234.7539967969, 212884.87605375424]])

# polygon = Polygon([[206556.84286634624, 192353.51987956092], [206543.3967223391, 192360.54765556753], [206540.0063863322, 192354.3565515615]])
print("area = ", polygon.area, "length = ", polygon.length, "height = ",np.mean(z))
"""
fig = go.Figure(data=[
    go.Surface(z=crop_chm_img)

])

fig.show()
"""
#gdf = gpd.read_file(crop_chm_img)
#print(gdf)

df = pd.DataFrame(crop_chm_img[0:, 0:], index = [i for i in range(crop_chm_img.shape[0])],
        columns = [i for i in range(crop_chm_img.shape[1])])
print(crop_chm_img)
print(df)
fig = go.Figure(data=[go.Mesh3d(x=df.columns, y=df.index, z=df.values, color='lightpink', opacity=1)])
fig.show()