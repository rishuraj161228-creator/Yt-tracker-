import requests
import time
from datetime import datetime

# Yahan apni API Key daalna mat bhoolna!
API_KEY = "AIzaSyAF-LTCTYCI6X71tLktuwlL2xSRmNrJYJo" 
VIDEO_ID = "VKBtenfifHI"

URL = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={VIDEO_ID}&key={API_KEY}"

print("Tracker Started...", flush=True)

while True:
    try:
        response = requests.get(URL).json()
        
        if 'error' in response:
            print("API Key ya limit ka Error:", response['error']['message'], flush=True)
        elif 'items' in response and len(response['items']) == 0:
            print("Error: Video nahi mili! Shayad link galat hai ya video Private hai.", flush=True)
        else:
            views = response['items'][0]['statistics']['viewCount']
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"{current_time} Views: {views}", flush=True)
        
        # Naya Smart Timer: Yeh time ko 00, 05, 10, 15 par lock karega
        now = datetime.now()
        seconds_to_wait = 300 - ((now.minute % 5) * 60 + now.second)
        time.sleep(seconds_to_wait)
        
    except Exception as e:
        print("Kuch aur error aaya:", e, flush=True)
        time.sleep(60)
