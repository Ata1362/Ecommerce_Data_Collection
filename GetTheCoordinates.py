# To use this fun you need to istall the following lib
# pip install pgeocode

import pgeocode as gp


def GetTheCoordinates(country, postcode):
    Country = gp.Nominatim(country)
    Results = Country.query_postal_code(postcode)
    lat = Results["latitude"]
    lon = Results["longitude"]
    return lat, lon


#x, y = GetTheCoordinates("my", 47160)
#print("Coordinates are lat {}, Lon {} ".format(x, y))
