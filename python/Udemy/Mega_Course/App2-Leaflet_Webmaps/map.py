__author__ = 'eladron'

import folium


#variables
lat  = 32.12830
long = 34.79269
loc = [lat,long]
zs   = 18
tls  = 'Stamen Terrain'
map_path = 'App2-Leaflet_Webmaps/map_test.html'


map = folium.Map(location=loc, zoom_start = zs)
map.simple_marker(location=loc, popup='My address' , marker_color='purple')

map.create_map(map_path)
