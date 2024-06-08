from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import json
import requests as req
import os

path="C:\Code\Earthquake-Alerts"
_EWFI,_ERF=tuple(file for file in os.listdir(path) if file.endswith('.json'))

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('Earthquake Alerts')
Form.resize(700, 600)
Form.setWindowIcon(QtGui.QIcon('earth.jpg'))

Form.setStyleSheet(
    "background-color: #411F1F;"
)

with open(_EWFI,"r",encoding="utf-8") as f:
    data = json.load(f)

grview = QtWidgets.QGraphicsView(Form)
grview.setGeometry(20, 20, 260, 200)     
scene = QtWidgets.QGraphicsScene()
scene.setSceneRect(0, 0, 120, 160)  
SeismogramsURL=data["cwaopendata"]["Dataset"]["Resource"]["ProductURL"]
Seismograms=QtGui.QPixmap(QtGui.QImage(SeismogramsURL))
img=Seismograms.scaled(120,160)   
scene.addPixmap(img)
grview.setScene(scene)
Form.show()
sys.exit(app.exec_())