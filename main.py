from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import json
import requests as req
import json
from io import BytesIO
import datetime
from lib import ewfi, erf

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
        color:#B6B4B4;
        font-size:17px;
        background-color:rgba(0, 0, 0, 0);        
    }
''')
monday.setFont(dfont)
if monday.text()==today_week_day:
    monday.setGeometry(910,85,42,20)
    monday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(0, 0, 0, 0);        
    }
    
    QLabel:hover{
        color: rgba(15, 11, 1, 0.27);         
    }
''')
    
tuesday=QtWidgets.QLabel(Form)
tuesday.setText("TUE")
tuesday.setGeometry(1010,85,38,20)
tuesday.setStyleSheet('''
    color:#B6B4B4;
    font-size:17px;
    background-color:rgba(0, 0, 0, 0);
''')
tuesday.setFont(dfont)
if tuesday.text()==today_week_day:
    tuesday.setGeometry(1010,85,42,20)
    tuesday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(0, 0, 0, 0);       
    }
    
    QLabel:hover{
        color: rgba(15, 11, 1, 0.27);          
    }
''')
    
wendsday=QtWidgets.QLabel(Form)
wendsday.setText("WEN")
wendsday.setGeometry(1110,85,42,20)
wendsday.setStyleSheet('''
    color:#B6B4B4;
    font-size:17px;
    background-color:rgba(0, 0, 0, 0);
''')
wendsday.setFont(dfont)
if wendsday.text()==today_week_day:
    wendsday.setGeometry(1110,85,42,20)
    wendsday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(0, 0, 0, 0);        
    }
    
    QLabel:hover{
       color: rgba(15, 11, 1, 0.27);         
    }
''')

thusday=QtWidgets.QLabel(Form)
thusday.setText("THU")
thusday.setGeometry(1210,85,37,20)
thusday.setStyleSheet('''
    color:#B6B4B4;
    font-size:17px;
    background-color:rgba(0, 0, 0, 0);
''')
thusday.setFont(dfont)
if thusday.text()==today_week_day:
    thusday.setGeometry(1210,85,38,20)
    thusday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(0, 0, 0, 0);        
    }
    
        QLabel:hover{
            color: rgba(15, 11, 1, 0.27);       
    }
''')
    
friday=QtWidgets.QLabel(Form)
friday.setText("FRI")
friday.setGeometry(1310,85,31,18)
friday.setStyleSheet('''
    color:#B6B4B4;
    font-size:17px;
    background-color:rgba(0, 0, 0, 0);
''')
friday.setFont(dfont)
if friday.text()==today_week_day:
    friday.setGeometry(1310,85,37,17)
    friday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(0, 0, 0, 0);        
    }
    
    QLabel:hover{
        color: rgba(15, 11, 1, 0.27);       
    }
''')
    
saturday=QtWidgets.QLabel(Form)
saturday.setText("SAT")
saturday.setGeometry(1410,85,36,20)
saturday.setStyleSheet('''
    color:#B6B4B4;
    font-size:17px;
    background-color:rgba(0, 0, 0, 0);
''')
saturday.setFont(dfont)
if saturday.text()==today_week_day:
    saturday.setGeometry(1410,85,42,20)
    saturday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(0, 0, 0, 0);        
    }
    
    QLabel:hover{
        color:  rgba(15, 11, 1, 0.27);          
    }
''')

sunday=QtWidgets.QLabel(Form)
sunday.setText("SUN")
sunday.setGeometry(1510,85,40,20)
sunday.setStyleSheet('''
    color:#B6B4B4;
    font-size:17px;
    background-color:rgba(0, 0, 0, 0);
''')
sunday.setFont(dfont)
if sunday.text()==today_week_day:
    sunday.setGeometry(1510,85,42,20)
    sunday.setStyleSheet('''
        QLabel{
        color:#FFFFFF;
        font-size:21px;
        background-color:rgba(0, 0, 0, 0);        
    }
    
    QLabel:hover{
        color: rgba(15, 11, 1, 0.27);         
    }
''')

timer=QtCore.QTimer()
timer.timeout.connect(_get_currect_time)
timer.start(1000)

#日期

current_date=current_date.replace(
    "-","/"
    )
date_label=QtWidgets.QLabel(Form)
date_label.setText(current_date)
date_label.setGeometry(1144,276,95,21)
date_label.setStyleSheet('''
            font-size:20px;
            color:#FFFFFF;
            background-color:rgba(0, 0, 0, 0);
''')
date_label.setFont(dfont)

day_label=QtWidgets.QLabel(Form)
day_label.setText(f"day {week_day}")
day_label.setGeometry(1279,276,45,21)
day_label.setFont(dfont)
day_label.setStyleSheet('''
            font-size:20px;
            color:#FFFFFF;
            background-color:rgba(0, 0, 0, 0);
            
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

frame=QtWidgets.QFrame(Form)
frame.setGeometry(827, 412, 823, 288)
frame.setStyleSheet('''
    border-radius: 20px;
    background-color:rgba(34, 26, 8, 0.63);
''')

ReportColor=QtWidgets.QLabel(Form)
ReportColor.setText("ReportColor:")
ReportColor.setGeometry(869, 440, 160, 30)
ReportColor.setStyleSheet('''
    font-size: 28px ;
    color:#FFFFFF;
    background-color: rgba(0, 0, 0, 0);
''')
ReportColor.setFont(dfont)

color=QtWidgets.QLabel(Form)
color.setText(erf.REPORTCOLOR)
color.setGeometry(1033, 440, 43, 30)
color.setStyleSheet('''
    font-size: 20px ;
    color:#FFFFFF;
    background-color:rgba(0, 0, 0, 0);
''')
color.setFont(dfont)

reportcontent=QtWidgets.QLabel(Form)
reportcontent.setText("ReportContent:")
reportcontent.setGeometry(869, 490, 180, 30)
reportcontent.setStyleSheet('''
    font-size: 28px ;
    color:#FFFFFF;
    background-color: rgba(0, 0, 0, 0);
''')
reportcontent.setFont(dfont)

content=QtWidgets.QLabel(Form)
content.setText(erf.REPORTCONTENT)
content.setGeometry(1051, 496, 277, 70)
content.setStyleSheet('''
    font-size: 20px ;
    color:#FFFFFF;
    background-color: rgba(0, 0, 0, 0);
''')
content.setWordWrap(True)
content.setFont(dfont)

time=QtWidgets.QLabel(Form)
time.setText("時間:")
time.setFont(dfont)
time.setGeometry(869, 561, 105, 62)
time.setStyleSheet('''
    font-size: 28px ;
    color:#FFFFFF;
    background-color:rgba(0, 0, 0, 0);
''')

origintime=QtWidgets.QLabel(Form)
origintime.setText(erf.ORIGINTIME)
origintime.setGeometry(940, 577, 200, 27)
origintime.setStyleSheet('''
    font-size: 20px ;
    color:#FFFFFF;
    background-color: rgba(0, 0, 0, 0);
''')
origintime.setFont(dfont)

locate=QtWidgets.QLabel(Form)
locate.setText("地點")
locate.setFont(dfont)
locate.setGeometry(1377, 444, 105, 62)
locate.setStyleSheet('''
    font-size: 53px ;
    color:rgba(235, 215, 225, 0.62);
    background-color:rgba(0, 0, 0, 0);
''')

location=QtWidgets.QLabel(Form)
location.setText(erf.LOCATION)
location.setGeometry(1388, 600, 80, 43)
location.setStyleSheet('''
    font-size: 40px ;
    color:#FFFFFF;
    background-color: rgba(0, 0, 0, 0);
''')
location.setFont(dfont)

epicenterlatitude=QtWidgets.QLabel(Form)

緯度=QtWidgets.QLabel(Form)
緯度.setText("緯度:")
緯度.setFont(dfont)
緯度.setGeometry(869, 611, 105, 62)
緯度.setStyleSheet('''
    font-size: 28px ;
    color:#FFFFFF;
    background-color:rgba(0, 0, 0, 0);
''')

epicenterlatitude.setText(str(erf.EPICENTERLATITUDE))
epicenterlatitude.setGeometry(942, 628, 47, 30)
epicenterlatitude.setStyleSheet('''
    font-size: 20px ;
    color:#FFFFFF;
    background-color: rgba(0, 0, 0, 0);
''')
epicenterlatitude.setFont(dfont)

經度=QtWidgets.QLabel(Form)
經度.setText("經度:")
經度.setFont(dfont)
經度.setGeometry(1010, 611, 105, 62)
經度.setStyleSheet('''
    font-size: 28px ;
    color:#FFFFFF;
    background-color:rgba(0, 0, 0, 0);
''')

epicenterlongitude=QtWidgets.QLabel(Form)
epicenterlongitude.setText(str(float(erf.EPICENTERLONGITUDE)))
epicenterlongitude.setGeometry(1080, 629, 100, 30)
epicenterlongitude.setStyleSheet('''
    font-size: 20px ;
    color:#FFFFFF;
    background-color: rgba(0, 0, 0, 0);
''')
epicenterlongitude.setFont(dfont)

magnitudetype=QtWidgets.QLabel(Form)
magnitudetype.setText("芮氏")
magnitudetype.setGeometry(1522, 449, 102, 50)
magnitudetype.setStyleSheet('''
    font-size: 53px ;
    color:rgba(235, 215, 225, 0.62);
    background-color: rgba(0, 0, 0, 0);
''')
magnitudetype.setFont(dfont)
                            
magnitudavalue=QtWidgets.QLabel(Form)
magnitudavalue.setText(str(erf.MAGNITUDAVALUE))
magnitudavalue.setGeometry(1555, 608, 40, 30)
magnitudavalue.setStyleSheet('''
    font-size: 40px ;
    color:#FFFFFF;
    background-color: rgba(0, 0, 0, 0);
''')
magnitudavalue.setFont(dfont)

Form.show()
sys.exit(app.exec_())