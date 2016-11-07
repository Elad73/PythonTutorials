__author__ = 'eladron'


import googlemaps
import folium
import pandas

#fileParams
googleDirectionsAPIKey = 'AIzaSyCROYC-QxBQnO1joU7p1vTf-M7Y7AOaBag'
defaultAddress         = 'Kdoshey Hashoha 26, Tel Aviv, Israel'
zs                     = 14
map_path               = './App2-Leaflet_Webmaps/map_test.html'
#map_path               = '/Users/eladron/Work/development_projects/python/Udemy/Mega_Course/App2-Leaflet_Webmaps/map_test.html'

usrAddress     = raw_input("Enter address: ")
usrAddressType = raw_input("What is this address: ")
lsUsr          = usrAddress.split(',')

#df = pandas.read_csv("Data-files/FamilyLocation.csv")

gmaps = googlemaps.Client(key=googleDirectionsAPIKey)

# Geocoding an address
geocode_result = gmaps.geocode(usrAddress) # the result is a list containing 1 dictionary
geocodeDict = geocode_result[0]
geoLocation = geocodeDict['geometry']['location'] #extracting the location
lat  = geoLocation['lat']
long = geoLocation['lng']

map = folium.Map(location=[lat, long], zoom_start = zs, tiles='OpenStreetMap' )
marker = folium.Marker(location=[lat, long], popup=usrAddressType, icon=folium.Icon(color='purple'))

map.add_children(marker)

map.add_child(folium.LayerControl())

map.save(outfile = map_path)








