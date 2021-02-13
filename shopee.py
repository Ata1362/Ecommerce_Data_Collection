# This Class will be contain all smart system to extract the data and inforation relates to Shoppe e-commerce
import pandas as pd
import numpy as np
import pgeocode as pg
import glob as glb

def GetTheCoordinates(country, postcode):
    """ This Function needs pgeocode to be installed.
     It will return the exact coordination of input postcode from a specific country"""
    Country = pg.Nominatim(country)
    Results = Country.query_postal_code(postcode)
    lat = Results["latitude"]
    lon = Results["longitude"]
    return lat, lon

# The input data should be a string, address of the main folder that *.xls files are stored
# Address sample is "G:\Google\Electronic Design\python_projects\Insight of Ecommerce Data/2020\*"
# which will take all files in the main folder#

def read_headers(address):
    """ This function will return the mutual headers among all *.xls format in the main folder.
     Make sure that you provide the full address. "*" will address all files in the 2020 folder.
     Exp: G:\Google\Electronic Design\python_projects\Insight of Ecommerce Data/2020\* """
    header = []
    for item in glb.glob(address):
        data = pd.read_excel(item,
                             sheet_name="orders",
                             header=None,
                             index_col=None)
        data_np = data.to_numpy()
        header.append(data_np[0, :])

    # Now we just make sure that the extracted labels are mutual among all files...
    # to avoid wrong attributes enter to our data

    mutual_headers = np.intersect1d(header[0], header[1])
    for i in range(len(header)):
        mutual_headers = np.intersect1d(mutual_headers, header[i])
    return mutual_headers



