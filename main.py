import requests
import time
from datetime import datetime

# Yahan apni details dalein
API_KEY = "AIzaSyAF-LTCTYCI6X71tLktuwlL2xSRmNrJYJo"
VIDEO_ID = "7Qxq8EtMms_a50Q_" 

URL = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={VIDEO_ID}&key={API_KEY}"

print("Tracker Started...")

while True:
    try:
        response = requests.get(URL).json()
        views = response['items'][0]['statistics']['viewCount']
        current_time = datetime.now().strftime("%I:%M %p")
        
        print(f"{current_time} Views: {views}")
        
        time.sleep(300) 
    except Exception as e:
        print("Error aaya:", e)
        time.sleep(60)
