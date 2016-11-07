__author__ = 'eladron'

import pandas
import folium
from globals import map_path
from helpers import calculateZoom


def color(proximity):
    proxColor = {
        0: 'purple',
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'lightgreen',
    }
    return proxColor.get(proximity, 'lightgray')


#read data file with headers for the columns (PROXIMITY, SIDE, NAME, STREET, CITY, COUNTRY, LAT, LONG)
df = pandas.read_csv('./Data-files/FamilyLocation.txt', names = ['PROXIMITY', 'SIDE', 'NAME', 'STREET', 'CITY', 'COUNTRY', 'LAT', 'LONG'])

#adding the center marker
zoom_start = calculateZoom(zip(df['LAT'], df['LONG']))
map    = folium.Map(location=[df['LAT'][0], df['LONG'][0]], zoom_start = zoom_start, tiles='OpenStreetMap' )
marker = folium.Marker(location=[df['LAT'][0], df['LONG'][0]], popup='Home', icon=folium.Icon(color='purple'))
map.add_children(marker)

fgParents  = folium.FeatureGroup(name='parents')
fgSiblings = folium.FeatureGroup(name='siblings')
fgUncles   = folium.FeatureGroup(name='uncles')
fgNephews  = folium.FeatureGroup(name='nephews')

for lat, long, name, proximity in zip(df['LAT'], df['LONG'], df['NAME'], df['PROXIMITY']):
    if proximity   == 1:
        fgParents.add_child(folium.Marker(location=[lat, long], popup=name, icon=folium.Icon(color=color(proximity), icon_color='black')))
    elif proximity == 2:
        fgSiblings.add_child(folium.Marker(location=[lat, long], popup=name, icon=folium.Icon(color=color(proximity), icon_color='black')))
    elif proximity == 3:
        fgUncles.add_child(folium.Marker(location=[lat, long], popup=name,   icon=folium.Icon(color=color(proximity), icon_color='black')))
    elif proximity == 4:
        fgNephews.add_child(folium.Marker(location=[lat, long], popup=name,   icon=folium.Icon(color=color(proximity), icon_color='black')))


map.add_child(fgParents)
map.add_child(fgSiblings)
map.add_child(fgUncles)
map.add_child(fgNephews)
map.add_child(folium.LayerControl())

map.save(outfile = map_path)