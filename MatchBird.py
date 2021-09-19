import pandas as pd
import glob, os

path = os.path.dirname(os.path.realpath(__file__)) + '/'
data = pd.read_excel(path + 'NewBirdData.xlsx')
locations = pd.read_csv(path + 'locations.csv')

matchBirds = data.loc[:, ["Species scientific name", "Species common name", "Body mass (g)", "UCT", "LCT"]]
matchBirds["Most Northerly"] = ""
matchBirds["Most Southerly"] = ""
for ind in data.index:
    mslat = 180
    mslong = 0
    mnlat = -180
    mnlong = 0
    
    years = ["(2019)", "(2018)", "(2017)", "(2016)", "(2015)"]
    for i in years:
        rowNorth = locations[locations["Original"]==data["Northern City "+ i][ind]]
        rowSouth = locations[locations["Original"]==data["Southern City "+ i][ind]]
        if not rowNorth.empty and float(rowNorth["Latitude"])>float(mnlat):
            mnlat = float(rowNorth["Latitude"])
            mnlong = float(rowNorth["Longitude"])
        if not rowSouth.empty and float(rowSouth["Latitude"])<float(mslat):
            mslat = float(rowSouth["Latitude"])
            mslong = float(rowSouth["Longitude"])
    matchBirds["Most Northerly"][ind] = "_" + str(mnlat) + "," + str(mnlong)
    matchBirds["Most Southerly"][ind] = "_" + str(mslat) + "," + str(mslong)


matchBirds.to_csv(path+'matchBirds.csv')