import requests as req
import json
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

