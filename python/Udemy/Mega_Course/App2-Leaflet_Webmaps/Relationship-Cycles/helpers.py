from geopy.distance import vincenty
from globals import zoom_start


#lsLocations = [[32.128302, 34.792693], [32.146087, 34.983676], [32.703002, 35.164252], [31.679973, 34.563714], [31.822281, 34.819500], [32.176590, 35.015884]]
def calculateZoom(lsLocations):
    northLocation = southLocation = westLocation = eastLocation =  lsLocations[0]
    zoom = zoom_start

    for location in lsLocations:
        if location[0] > northLocation[0]:
            northLocation = location
        elif location[0] < southLocation[0]:
            southLocation = location
        if location[1] < westLocation[1]:
            westLocation = location
        elif location[1] > eastLocation[1]:
            eastLocation = location

    #finding the max vertical
    verticalMiles = vincenty(northLocation, southLocation).kilometers

    #finding the max horizontal
    horzMiles = vincenty(westLocation, eastLocation).kilometers

    if verticalMiles or horzMiles < 30: zoom = 15
    elif (verticalMiles or horzMiles) > 30 or (verticalMiles or horzMiles) < 60: zoom = 12
    else: zoom = 9

    return zoom


