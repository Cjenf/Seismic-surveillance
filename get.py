from typing import Union
from pydantic import BaseModel
import json
import requests as req
import json

class ERF(BaseModel):
    REPORTCOLOR:Union[str,int]
    REPORTCONTENT:Union[str,int]
    RECORDIMAGEURI:Union[str,int]
    WEB:Union[str,int]
    ORIGINTIME:Union[str,int]
    LOCATION:Union[str,int]
    EPICENTERLATITUDE:int | float
    EPICENTERLONGITUDE:int | float
    MAGNITUDAVALUE:int

class EWFI(BaseModel):
    REPORTCOLOR:Union[str,int]
    REPORTCONTENT:Union[str,int]
    RECORDIMAGEURI:Union[str,int]
    WEB:Union[str,int]
    ORIGINTIME:Union[str,int]
    LOCATION:Union[str,int]
    EPICENTERLATITUDE:int | float
    EPICENTERLONGITUDE:int | float
    MAGNITUDAVALUE:int


#無感地震
try:
    url="https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=CWA-877EA591-BC8A-4DD2-8B60-4272DAC4BBAC&format=JSON&AreaName="

    r=req.get(url)
    data=r.json()

    file_path = 'ewfi.json'
    with open(file_path, 'w') as file:
        json.dump(data, file)

except Exception as e:
    print(e)
#有感地震
try:
    url="https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=CWA-877EA591-BC8A-4DD2-8B60-4272DAC4BBAC"

    r=req.get(url)
    data=r.json()

    file_path = 'erf.json'
    with open(file_path, 'w') as file:
        json.dump(data, file)

except Exception as e:
    print(e)    


with open("ewfi.json","r",encoding="utf-8") as f: #無感地震
    data = json.load(f)
    ewfi=EWFI(
            REPORTCOLOR=data["records"]["Earthquake"][0]["ReportColor"],
            REPORTCONTENT=data["records"]["Earthquake"][0]["ReportContent"],
            RECORDIMAGEURI=data["records"]["Earthquake"][0]["ReportImageURI"],
            WEB=data["records"]["Earthquake"][0]["Web"],
            ORIGINTIME=data["records"]["Earthquake"][0]["EarthquakeInfo"]["OriginTime"],
            LOCATION=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["Location"],
            EPICENTERLATITUDE=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLatitude"], #震央緯度
            EPICENTERLONGITUDE=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLongitude"],#震央經度
            MAGNITUDAVALUE=int(data["records"]["Earthquake"][0]["EarthquakeInfo"]["EarthquakeMagnitude"]["MagnitudeValue"]) #"芮氏規模"
    )
   

with open("erf.json","r",encoding="utf-8") as f: #有感地震
    data = json.load(f)
    erf=ERF(
            REPORTCOLOR=data["records"]["Earthquake"][0]["ReportColor"],
            REPORTCONTENT=data["records"]["Earthquake"][0]["ReportContent"],
            RECORDIMAGEURI=data["records"]["Earthquake"][0]["ReportImageURI"],
            WEB=data["records"]["Earthquake"][0]["Web"],
            ORIGINTIME=data["records"]["Earthquake"][0]["EarthquakeInfo"]["OriginTime"],
            LOCATION=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["Location"],
            EPICENTERLATITUDE=float(data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLatitude"]), #震央緯度
            EPICENTERLONGITUDE=float(data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLongitude"]),#震央經度
            MAGNITUDAVALUE=int(data["records"]["Earthquake"][0]["EarthquakeInfo"]["EarthquakeMagnitude"]["MagnitudeValue"]) #"芮氏規模"
    )