import os

# 設定要搜尋的目錄path = "C:\Code\Earthquake-Alerts"
path="C:\Code\Earthquake-Alerts"
# 使用 os.walk 遍歷目錄及其子目錄

a=tuple(file for file in os.listdir(path) if file.endswith('.json'))
print(a)