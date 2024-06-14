import sys
import sqlite3
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

font_db = QFontDatabase()
fonts = font_db.families()

conn = sqlite3.connect('font.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS fonts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

for font in fonts:
    c.execute('''INSERT INTO fonts (name) VALUES (?)''', (font,))
    print(font)

conn.commit()
conn.close()

print("All fonts have been saved to font.db")