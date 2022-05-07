import folium
import folium.features as Features
import pandas as pd
import base64
import datetime
import time
import json

# Getting the current time and formatting it to a string.
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")

def isdaytime(curr_time):
    if curr_time >= '08:00:00' and curr_time <= '20:00:00':
        return True
    else:
        return False

#path = r'C:\Users\calin\Desktop\map project'

df1 = pd.read_csv('pandasDF_Text/benzinarii.txt')
df_Ap = pd.read_csv('pandasDF_Text/apartamente_bacau.txt')

#Gas Stations Details
lat = list(df1['Latitudine'])
lon = list(df1['Longitudine'])
desc = list(df1['Descriere'])
benz = list(df1['Benzinarie'])
num = list(df1['Numarul'])

#liste Apartamente
lat_ap = list(df_Ap['Lat'])
lon_ap = list(df_Ap['Lon'])
desc_ap = list(df_Ap['Descriere'])

#HTML Code for the Gas Stations
html ="""
<h1 style = "font-size:22px"><mark style="background-color:cyan">Informatie benzinarie:</mark></h1>
<p style = "font-size:18px">Pareri: %s</p>
<img src = "data:image/png;base64,{}">
""".format

#HTML Code for the Hotels/Flats(even though there's only one on the map)
html_Ap = """
</style>
<h1 style = "font-size:22px"><mark>Informatie Apartament:</mark></h1>
<p style = "font-size:18px">%s</p>
"""

# Checking if it's daytime or not and then changing the map's tiles.
if isdaytime(current_time):
    map = folium.Map(location = [46.5676, 26.8951], zoom_start = 12.5, tiles='CartoDB positron',
                        attr='Mapbox', show = False)
else:
    map = folium.Map(location = [46.5676, 26.8951], zoom_start = 12.5, tiles='CartoDB dark_matter',
                        attr='Mapbox', show = False, crs='EPSG3857')

#icons custom
if isdaytime(current_time):
    logo_ap = Features.CustomIcon('custom icons\house_icon.png', icon_size = (65,65))
else:
    logo_ap = Features.CustomIcon('custom icons\house_icon_npt.png', icon_size = (65,65))

fg_benz = folium.FeatureGroup(name = 'Gas Stations Bacau')
fg_ap = folium.FeatureGroup(name = 'Hotels/Flats Bacau')

#Gas Stations(not all of them, displayed the most popular ones)

for lt, ln, des, nmbnz, nr in zip(lat, lon, desc, benz, num):
    #markere pentru descrierea bzenzinariilor
    png = 'poze_benz\BENZ_%s.png' % str(nr-1)
    encoded = base64.b64encode(open(png, 'rb').read()).decode()
    if nr != 3:
        iframe = folium.IFrame(html = html(encoded) % des, width = 365, height = 320)
    else:
        iframe = folium.IFrame(html = html(encoded) % des, width = 400, height = 405)

    if isdaytime(current_time):
        icon = Features.CustomIcon('custom icons\icon_benz.png', icon_size = (40, 40))
    else:
        icon = Features.CustomIcon('custom icons\icon_benz_npt.png', icon_size = (40, 40))
    fg_benz.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe),
    icon = icon, draggable = False,tooltip = folium.Tooltip('Benzinaria ' + nmbnz)))


#Apartamente
for lt, ln, des, prop in zip(lat_ap, lon_ap, desc_ap, list(df_Ap['Proprietar'])):
    #markere pt apartamente bacau

    iframe_ap = folium.IFrame(html = html_Ap % des, width = 250, height = 130)
    fg_ap.add_child(folium.Marker(location = [lt, ln], popup =
    folium.Popup(iframe_ap),
    icon = logo_ap, draggable = False,
    tooltip = folium.Tooltip('Apartamentul lui ' + prop)))

#for coordinates in [[46.5676, 26.8967], [46.5676, 26.8951]]:
#   fg.add_child(folium.Marker(location = coordinates, popup = 'Hereee', icon = folium.Icon(color = 'green'), draggable = True, tooltip = folium.Tooltip('adresa mea', sticky = False)))

#TOPOJSON AND GeoJson

fg_rivers = folium.FeatureGroup(name = "World's Rivers", show = False)

if isdaytime(current_time):
    river_style_func = lambda x: {'color': 'blue', 'weight': '1.75'}
else:
    river_style_func = lambda x: {'color': 'lightblue', 'weight': '1.75'}

fg_rivers.add_child(folium.GeoJson(data = open('json-files/rivers.json', 'r', encoding = 'utf-8-sig').read(),
style_function = river_style_func))

fg_rom = folium.FeatureGroup(name = 'Romania and Its Counties')

if isdaytime(current_time):
    map_style_func = lambda x: {'fillColor': 'transparent', 'lineJoin': 'round',
'lineCap': 'round', 'opacity': '0.7', 'weight': '1.95', 'color': 'black'}
else:
    map_style_func = lambda x: {'fillColor': 'transparent', 'lineJoin': 'round',
    'lineCap': 'round', 'opacity': '0.7', 'weight': '1.95', 'color': 'lime'}

fg_rom.add_child(folium.TopoJson(data = open('json-files/romania.json'),
object_path = 'objects.ROU_adm1', overlay = False,
style_function = map_style_func))

map.add_child(fg_benz)
map.add_child(fg_ap)
map.add_child(fg_rom)
map.add_child(fg_rivers)
map.add_child(folium.LayerControl())
map.save('Harta1.html')