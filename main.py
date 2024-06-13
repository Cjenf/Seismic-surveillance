from PyQt5 import QtWidgets, QtGui, QtCore
from typing import Dict, Union, Any
from pydantic import BaseModel, ValidationError
import sys
import json
import os
import requests as req
import json
from io import BytesIO

class ERF(BaseModel):
    REPORTCOLOR:Union[str,int]
    REPORTCONTENT:Union[str,int]
    RECORDIMAGEURI:Union[str,int]
    WEB:Union[str,int]
    ORIGINTIME:Union[str,int]
    LOCATION:Union[str,int]
    EPICENTERLATITUDE:int
    EPICENTERLONGITUDE:int
    MAGNITUDAVALUE:int

class EWFI(BaseModel):
    REPORTCOLOR:Union[str,int]
    REPORTCONTENT:Union[str,int]
    RECORDIMAGEURI:Union[str,int]
    WEB:Union[str,int]
    ORIGINTIME:Union[str,int]
    LOCATION:Union[str,int]
    EPICENTERLATITUDE:int
    EPICENTERLONGITUDE:int
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

path="C:\Code\Seismic-surveillance"

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('Earthquake Alerts')
Form.resize(1800,800)

Form.setWindowIcon(QtGui.QIcon('earth.jpg'))

Form.setStyleSheet('''
        background-color:#543B3B;
        
''')

with open("ewfi.json","r",encoding="utf-8") as f: #無感地震
    data = json.load(f)
    ewfi=EWFI(
            REPORTCOLOR=data["records"]["Earthquake"][0]["ReportColor"],
            REPORTCONTENT=data["records"]["Earthquake"][0]["ReportContent"],
            RECORDIMAGEURI=data["records"]["Earthquake"][0]["ReportImageURI"],
            WEB=data["records"]["Earthquake"][0]["Web"],
            ORIGINTIME=data["records"]["Earthquake"][0]["EarthquakeInfo"]["OriginTime"],
            LOCATION=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["Location"],
            EPICENTERLATITUDE=int(data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLatitude"]), #震央緯度
            EPICENTERLONGITUDE=int(data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLongitude"]),#震央經度
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
            EPICENTERLATITUDE=int(data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLatitude"]), #震央緯度
            EPICENTERLONGITUDE=int(data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLongitude"]),#震央經度
            MAGNITUDAVALUE=int(data["records"]["Earthquake"][0]["EarthquakeInfo"]["EarthquakeMagnitude"]["MagnitudeValue"]) #"芮氏規模"
    )
   

frame=QtWidgets.QFrame(Form)
frame.setFrameShape(QtWidgets.QFrame.Box)
frame.setFrameShadow(QtWidgets.QFrame.Sunken)
frame.setLineWidth(2)
frame.setGeometry(500,40,569,721)
frame.setStyleSheet('''
    QFrame {
        background-color: #2E2828;
        border: 10px outset #7F7474;
        border-radius: 15px;
        background-color: qlineargradient(spread:reflect, 
                   x1:0, y1:0, x2:1, y2:1, stop:0 rgba(106, 100, 94, 0.8), 
                   stop:1 rgba(70, 58, 47, 0.8));  /* 設置線性漸變背景 */  
        
    }
''')

with open("C:\Code\Seismic-surveillance\data\E-A0015-003.json","r",encoding="utf-8") as f: 
    data = json.load(f)
    PICURL=data["cwaopendata"]["Dataset"]["Resource"]["ProductURL"]
    response = req.get(PICURL)
    image_data = BytesIO(response.content)
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(image_data.read())
    scaled_pixmap=pixmap.scaled(QtCore.QSize(700,799),QtCore.Qt.KeepAspectRatio)
    image_label = QtWidgets.QLabel(Form)
    image_label.setPixmap(scaled_pixmap)
    image_label.setStyleSheet('''
        QLabel{
            background-color: transparent;  /* 使背景透明 */
        } 
    ''')
    image_label.setGeometry(0, 0, 700, 799)
    
Form.show()
sys.exit(app.exec_())