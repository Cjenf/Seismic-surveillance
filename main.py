from PyQt5 import QtWidgets, QtGui, QtCore
from typing import Union
from pydantic import BaseModel
import sys
import json
import os
import requests as req
import json
from io import BytesIO
import datetime


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

def _get_currect_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    t=[]
    t.append(current_time)
    time_label.setText(list(map(lambda s : f"      {current_time} AM" if int(current_time[0:2])<12 else f"      {current_time} PM",t))[0])

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
   
#時間


font=QtGui.QFont()
font.setFamily("STKaiti")

time_label=QtWidgets.QLabel(Form)
time_label.setGeometry(820, 55, 830, 269)
time_label.setStyleSheet('''
    color:rgba(182, 179, 173, 0.54);
    font-size:110px;
    border:5px outset rgba(18, 13, 1, 0.4);
    border-radius: 20px; 
    background-color:rgba(34, 26, 8, 0.63);                   
''')
time_label.setFont(font)

dfont=font = QtGui.QFont()  
dfont.setBold(True)

now = datetime.datetime.now()
current_date = now.strftime("%Y-%m-%d") #日期
week_day = now.weekday()
week_day_chinese = [
        "MON", 
        "TUE", 
        "WEN", 
        "THU", 
        "FRI", 
        "SAT", 
        "SUN"
    ]
today_week_day = week_day_chinese[week_day] #星期幾

monday=QtWidgets.QLabel(Form)
monday.setText("MON")
monday.setGeometry(910,85,42,20)
monday.setStyleSheet('''
    QLabel{
        color:B6B4B4;
        font-size:17px;
        background-color:rgba(34, 26, 8, 0.63);        
    }
    
    QLabel:hover{
        color: #FCCCCC;          
    }
''')
monday.setFont(dfont)
if monday.text()==today_week_day:
    monday.setGeometry(910,85,42,20)
    monday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(34, 26, 8, 0.63);        
    }
    
    QLabel:hover{
        color: #FCCCCC;          
    }
''')
    
tuesday=QtWidgets.QLabel(Form)
tuesday.setText("TUE")
tuesday.setGeometry(1010,85,42,20)
tuesday.setStyleSheet('''
    color:B6B4B4;
    font-size:17px;
    background-color:rgba(34, 26, 8, 0.63);
''')
tuesday.setFont(dfont)
if tuesday.text()==today_week_day:
    tuesday.setGeometry(1010,85,42,20)
    tuesday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(34, 26, 8, 0.63);        
    }
    
    QLabel:hover{
        color: #FCCCCC;          
    }
''')
    
wendsday=QtWidgets.QLabel(Form)
wendsday.setText("WEN")
wendsday.setGeometry(1110,85,42,20)
wendsday.setStyleSheet('''
    color:B6B4B4;
    font-size:17px;
    background-color:rgba(34, 26, 8, 0.63);
''')
wendsday.setFont(dfont)
if wendsday.text()==today_week_day:
    wendsday.setGeometry(1110,85,42,20)
    wendsday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(34, 26, 8, 0.63);        
    }
    
    QLabel:hover{
        color: #FCCCCC;          
    }
''')

thusday=QtWidgets.QLabel(Form)
thusday.setText("THU")
thusday.setGeometry(1210,85,42,20)
thusday.setStyleSheet('''
    color:B6B4B4;
    font-size:17px;
    background-color:rgba(34, 26, 8, 0.63);
''')
thusday.setFont(dfont)
if thusday.text()==today_week_day:
    thusday.setGeometry(1210,85,42,20)
    thusday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(34, 26, 8, 0.63);        
    }
    
        QLabel:hover{
            color: #FCCCCC;  
            font-size: 30px; /* 放大文字 */        
    }
''')
    
friday=QtWidgets.QLabel(Form)
friday.setText("FRI")
friday.setGeometry(1310,85,31,18)
friday.setStyleSheet('''
    color:#B6B4B4;
    font-size:17px;
    background-color:rgba(34, 26, 8, 0.63);
''')
friday.setFont(dfont)
if friday.text()==today_week_day:
    friday.setGeometry(1310,85,42,20)
    friday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(34, 26, 8, 0.63);        
    }
    
    QLabel:hover{
        color: #FCCCCC;          
    }
''')
    
saturday=QtWidgets.QLabel(Form)
saturday.setText("SAT")
saturday.setGeometry(1410,85,36,20)
saturday.setStyleSheet('''
    color:#B6B4B4;
    font-size:17px;
    background-color:rgba(34, 26, 8, 0.63);
''')
saturday.setFont(dfont)
if saturday.text()==today_week_day:
    saturday.setGeometry(1410,85,42,20)
    saturday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(34, 26, 8, 0.63);        
    }
    
    QLabel:hover{
        color: #FCCCCC;          
    }
''')

sunday=QtWidgets.QLabel(Form)
sunday.setText("SUN")
sunday.setGeometry(1510,85,40,20)
sunday.setStyleSheet('''
    color:#B6B4B4;
    font-size:17px;
    background-color:rgba(34, 26, 8, 0.63);
''')
sunday.setFont(dfont)
if sunday.text()==today_week_day:
    sunday.setGeometry(1510,85,42,20)
    sunday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(34, 26, 8, 0.63);        
    }
    
    QLabel:hover{
        color: #FCCCCC;          
    }
''')

timer=QtCore.QTimer()
timer.timeout.connect(_get_currect_time)
timer.start(1000)

#日期

current_date=current_date.replace(
    "-","/"
    )
date_label=QtWidgets.QLabel()
date_label.setText(current_date)
date_label.setGeometry(700,100,500,100)
date_label.setStyleSheet('''
            font-size:110px;
''')

fontc=QtGui.QFont()
fontc.setFamily("STKaiti")
day_label=QtWidgets.QLabel()
day_label.setText(f"day {week_day}")
day_label.setGeometry(806,250,400,100)
day_label.setStyleSheet('''
            font-size:90px;
''')
day_label.setFont(fontc)

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