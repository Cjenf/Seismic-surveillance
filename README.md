### 🌏Seismic-surveillance GUI
🔔Inquiry/Notification Information in the event of an earthquake. <br>
※※💀 btw it's a work in progress , and the interface is quite rudimentary
### **Download the Project**
```bash
git clone https://github.com/Cjenf/Seismic-surveillance.git
cd Seismic-surveillance
```
### Run code
```py
main.py
```
### API
```py
import requests

# GET /erf
erf_response = requests.get("https://seismic-surveillance-ydzk.vercel.app/erf")
if erf_response.status_code == 200:
    erf_data = erf_response.json()
    print("ERF Data:", erf_data)
else:
    print("Failed to retrieve ERF data")
```
