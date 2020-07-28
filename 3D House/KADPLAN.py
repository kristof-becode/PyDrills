import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
import pandas as pd
import geopandas as gpd
import rasterio as rio
import rasterio as rio # Import Rasterio, a library for working with geospatial raster data
from rasterio.mask import mask # to mask or clip functionality
#from rasterio.plot import show # functionality to plot
import earthpy as et
import earthpy.plot as ep
import geopy
from geopy.geocoders import Nominatim # I need to explicitly import Nominatim as such
#import folium
from pyproj import Proj, transform
import plotly.graph_objects as go
from shapely.geometry import Polygon
pd.set_option('display.width',400)
pd.set_option('display.max_columns', 40)
from descartes import PolygonPatch
import fiona
"""

plot_loc = gpd.read_file('/home/becode/KadPlan/Bpn_CaPa.shp')
print(plot_loc.head(10))
#plot_loc.plot()
#plt.show()

dbf_data = gpd.read_file('/home/becode/KadPlan/Bpn_CaPa.dbf') #plotting this gives same as plotting shape .shp and plotting dataframe is also exactly the same
print(dbf_data.head(10))
dbf_data.plot()
plt.show()

# POLYGONEN UIT MYMINFIN SITE
#71382D0700/00G000 ik zie 3 polygonen
# Diestersesteenweg 26
dbf_data = gpd.read_file('/home/becode/KadPlan/Bpn_CaPa.dbf')
print(dbf_data.geometry[dbf_data.CaPaKey == '71382D0700/00G000'])

pol = [{'coordinates': [[[206534.2682743296, 192365.31859957054], [206530.00075432658, 192368.42951157317], [206530.8269943297, 192369.56295157224], [206530.41918632388, 192369.8602955714], [206530.48101032525, 192369.94503157213], [206528.22667432576, 192371.58829557523], [206528.15307432413, 192371.48730357364], [206525.51358632743, 192373.41127157584], [206525.5873143226, 192373.5122635737], [206523.34193832427, 192375.14899957553], [206523.27320232242, 192375.0546635762], [206522.8639863208, 192375.35303157568], [206522.32254632562, 192374.61024757475], [206520.88382632285, 192372.63648757339], [206517.7801463157, 192374.89882357419], [206509.276594311, 192367.44179956988], [206509.40965031087, 192367.0547915697], [206510.5666423142, 192365.8169035688], [206510.51800231636, 192365.43866356835], [206514.20517031848, 192362.8288715668], [206515.60933031887, 192363.4139595665], [206521.32811432332, 192359.1675595641], [206521.83781032264, 192359.87706356496], [206524.36389032006, 192357.92442356423], [206526.1016183272, 192358.66336756572], [206527.9004663229, 192357.28672756255], [206529.9454583302, 192359.86618356407], [206534.2682743296, 192365.31859957054]]], 'type': 'Polygon'}]
#print(pol['coordinates'][0])
print(pol[0]['coordinates'][0])
wat = pol[0]['coordinates'][0]
#print(wat.istype())
#for item in pol:
 #   print(item)

plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaBu.dbf')
print(plot_loc.head(10))
plot_loc.plot()
#plt.show()

#plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaBu.sbx')
#print(plot_loc.head(10))
#plot_loc.plot()
#plt.show()
plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaBu.shp')
print(plot_loc.head(10))
plot_loc.plot()
#plt.show()
plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaBu.shx')
print(plot_loc.head(10))
plot_loc.plot()
#plt.show()

plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaPa.dbf')
print(plot_loc.head(10))
plot_loc.plot()
#plt.show()

#plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaPa.sbx')
#print(plot_loc.head(10))
#plot_loc.plot()
#plt.show()
plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaPa.shp')
print(plot_loc.head(10))
plot_loc.plot()
#plt.show()
plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaPa.shx')
print(plot_loc.head(10))
plot_loc.plot()
#plt.show()

plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_ReBu.dbf')
print(plot_loc.head(10))
plot_loc.plot()
#plt.show()

#plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaPa.sbx')
#print(plot_loc.head(10))
#plot_loc.plot()
#plt.show()
plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_ReBu.shp')
print(plot_loc.head(10))
plot_loc.plot()
#plt.show()
plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_ReBu.shx')
print(plot_loc.head(10))
plot_loc.plot()
#plt.show()


 from shapely.geometry import Point
>>> point = Point(0.0, 0.0)
>>> q = Point((0.0, 0.0))
from shapely.geometry import Polygon
>>> polygon = Polygon([(0, 0), (1, 1), (1, 0)])
"""
plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaPa.shp')
plottie = plot_loc.geometry[plot_loc.CaPaKey == '12014A0611/00K002'].iloc[0]
print(type(plottie))
#plo = list.plottie
#for item in plottie:
#    print(item)
#print(plo)
#print(plottie[1])
#pol = Polygon(plottie)
#print(type(pol))
#POLYGON ((174532.8472395137 196816.7190645691, 174532.616604247 196816.4407896465, 174523.0568751268 196817.5251375716, 174515.6441300806 196818.3659276916, 174515.6101660554 196818.6638342934, 174510.3920028495 196864.5200496474, 174510.3406573319 196864.9712596387, 174519.2143794749 196866.3361144643, 174523.9550981545 196867.065256088, 174526.335057734 196867.431375768, 174526.3398578609 196867.432175206, 174526.4109910142 196866.8780619754, 174532.8472395137 196816.7190645691))
fig = plt.figure()
ax = fig.gca()
ax.add_patch(PolygonPatch(plottie))
ax.axis('scaled')
plt.show()



#map_chm = rio.open('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/tile_chm_k22_136.tif')
#mask_chm, mask_chm_transform = mask(dataset=map_chm, shapes=plottie, crop=True, nodata=0, filled=True, indexes=1)
map_chm = fiona.open('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/tile_chm_k22_136.tif')
mask_chm, mask_chm_transform = rio.mask.mask(dataset=map_chm, shapes=plottie, crop=True)
print('-> mask succesful')
#fig = go.Figure(data=[go.Surface(z=mask_chm)])
#fig.update_layout(title='3D Plot' , width=750, height=750)
#fig.show()


#print(plot_loc.head(10))
#plot_loc.plot()
#plt.show()
#plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_ReBu.shp')
#print(plot_loc.head(10))
#plot_loc.plot()
#plt.show()
#plot_loc = gpd.read_file('/home/becode/Downloads/HEIST-OP-DEN-BERG_L72_2020/Bpn_CaBu.shp')
#print(plot_loc.head(10))
#plot_loc.plot()
#plt.show()