import pandas as pd
import requests
import numpy as np
import time
from bs4 import BeautifulSoup

filepath = './scrape-golf-course/prefectureCourseUrls.csv'
df = pd.read_csv(filepath)
golfCourseUrls = df["0"].values



addresses = []
lons = []
lats = []
golfCourseIds = []
golfCourseNames = []

api_key = ""



for golfCourseUrl in golfCourseUrls:
    
    golfCourseId = golfCourseUrl.split("_")[1].split(".")[0]
    
    url = f'https://shotnavi.jp/gcguide/map/map_{golfCourseId}.htm'
    golfCourseIds.append(golfCourseIds)
    
    r= requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    
    golfCourseNames.append(soup.find("h1").text)
    time.sleep(1)
    soup = BeautifulSoup(r.content, "html.parser")

    dfs = pd.read_html(url)

    time.sleep(3)
    
    preAddress = dfs[0][1][0].replace(u'\xa0', ' ').split(" ")
    try:

        address = preAddress[1]+preAddress[2]

        lon = ""
        lat = ""
    
    

        try:
            url = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="+address
            r = requests.get(url)
            coordinates = r.json()[0]["geometry"]["coordinates"]
            lon = coordinates[0]
            lat = coordinates[1]
        except Exception as e:
            print("err",e)
            print("id",golfCourseId)
            url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}components=country:JP&key={api_key}"
            r = requests.get(url)
            lon = str(r.json()["results"][0]["geometry"]["location"]["lng"])
            lat = str(r.json()["results"][0]["geometry"]["location"]["lat"])
    

        
        
    

        addresses.append(address)
        lons.append(lon)
        lats.append(lat)
    except Exception as e:
        print("e",e)
        print("err 2 id",golfCourseId)
        addresses.append("")
        lons.append("")
        lats.append("")


arr1 = np.array([addresses,lons,lats])
df = pd.DataFrame(data=arr1).transpose()


df2 = pd.DataFrame({
'addresses':addresses,
'lons':lons,
'lats':lats,
"golfCourseIds":golfCourseIds,
"golfCourseNames":golfCourseNames

})

df2.to_csv('./scrape-golf-course/addressLatLon.csv')
