import sys
import sqlite3
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

# 初始化 QApplication
app = QApplication(sys.argv)

# 获取系统中的所有字体
font_db = QFontDatabase()
fonts = font_db.families()

# 创建 SQLite 数据库并连接
conn = sqlite3.connect('font.db')
c = conn.cursor()

# 创建字体表
c.execute('''CREATE TABLE IF NOT EXISTS fonts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

# 插入字体数据
for font in fonts:
    c.execute('''INSERT INTO fonts (name) VALUES (?)''', (font,))
    print(font)

# 提交并关闭数据库连接
conn.commit()
conn.close()

print("All fonts have been saved to font.db")