from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import json
import os
import requests as req
import json
from io import BytesIO
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
_EWFI,_ERF=tuple(file for file in os.listdir(path) if file.endswith('.json'))

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('Earthquake Alerts')
Form.resize(1800,800)

Form.setWindowIcon(QtGui.QIcon('earth.jpg'))

Form.setStyleSheet(
    "background-color: #411F1F;"
)

with open(_EWFI,"r",encoding="utf-8") as f: #無感地震
    data = json.load(f)
    erf={}

    erf.update(
        _REPORTCOLOR=data["records"]["Earthquake"][0]["ReportColor"],
        _REPORTCONTENT=data["records"]["Earthquake"][0]["ReportContent"],
        _RECORDIMAGEURI=data["records"]["Earthquake"][0]["ReportImageURI"],
        _WEB=data["records"]["Earthquake"][0]["Web"],
        _ORIGINTIME=data["records"]["Earthquake"][0]["EarthquakeInfo"]["OriginTime"],
        _LOCATION=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["Location"],
        _EPICENTERLATITUDE=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLatitude"], #震央緯度
        _EPICENTERLONGITUDE=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLongitude"],#震央經度
        _MAGNITUDAVALUE=data["records"]["Earthquake"][0]["EarthquakeInfo"]["EarthquakeMagnitude"]["MagnitudeValue"], #"芮氏規模"
    )
    
with open(_ERF,"r",encoding="utf-8") as f: #有感地震
    ewfi={}
    data = json.load(f)
    ewfi.update(
        _REPORTCOLOR=data["records"]["Earthquake"][0]["ReportColor"],
        _REPORTCONTENT=data["records"]["Earthquake"][0]["ReportContent"],
        _RECORDIMAGEURI=data["records"]["Earthquake"][0]["ReportImageURI"],
        _WEB=data["records"]["Earthquake"][0]["Web"],
        _ORIGINTIME=data["records"]["Earthquake"][0]["EarthquakeInfo"]["OriginTime"],
        _LOCATION=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["Location"],
        _EPICENTERLATITUDE=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLatitude"], #震央緯度
        _EPICENTERLONGITUDE=data["records"]["Earthquake"][0]["EarthquakeInfo"]["Epicenter"]["EpicenterLongitude"],#震央經度
        _MAGNITUDAVALUE=data["records"]["Earthquake"][0]["EarthquakeInfo"]["EarthquakeMagnitude"]["MagnitudeValue"], #"芮氏規模"
    )

with open("C:\Code\Seismic-surveillance\data\E-A0015-003.json","r",encoding="utf-8") as f: 
    data = json.load(f)
    PICURL=data["cwaopendata"]["Dataset"]["Resource"]["ProductURL"]
    response = req.get(PICURL)
    image_data = BytesIO(response.content)
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(image_data.read())
    scaled_pixmap=pixmap.scaled(QtCore.QSize(500,420),QtCore.Qt.KeepAspectRatio)
    IMGlabel = QtWidgets.QLabel(Form)
    IMGlabel.setPixmap(scaled_pixmap)

font = QtGui.QFont()  
font.setFamily('源柔黑體')
font.setPointSize(20)  
label = QtWidgets.QLabel(Form)   
label.setText(erf["_REPORTCOLOR"])     
label.setFont(font)

Form.show()
sys.exit(app.exec_())