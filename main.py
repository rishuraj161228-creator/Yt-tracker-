import requests
import time
from datetime import datetime

# 1. Yahan apni API Key dalein!
API_KEY = "AIzaSyAF-LTCTYCI6X71tLktuwlL2xSRmNrJYJo" 

# 2. Yahan apni ek Video ki ID dalein
VIDEO_ID = "cXDhlsXxJn4"

URL = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={VIDEO_ID}&key={API_KEY}"

purane_views = None

# Yeh function numbers ko K ya M mein badal dega
def format_k(number):
    if number >= 1000000:
        return f"{number / 1000000:.1f}M"  # 1 Million se upar ke liye
    elif number >= 1000:
        return f"{number / 1000:.1f}K"     # 1 Thousand se upar ke liye
    else:
        return str(number)                 # 1000 se kam ho toh normal dikhayega

print("Smart 'K' Tracker Started...", flush=True)

while True:
    try:
        current_time = datetime.now().strftime("%I:%M %p")
        response = requests.get(URL).json()
        
        if 'items' in response and len(response['items']) > 0:
            aaj_ke_views = int(response['items'][0]['statistics']['viewCount'])
            
            if purane_views is None:
                print(f"{current_time} Views: {format_k(aaj_ke_views)}  (Tracking shuru...)", flush=True)
            else:
                naye_aaye_views = aaj_ke_views - purane_views
                
                # Total aur naye views dono ko format_k ke through nikalna
                print(f"{current_time} Views: {format_k(aaj_ke_views)}  (+{format_k(naye_aaye_views)} naye views)", flush=True)
            
            purane_views = aaj_ke_views
        else:
            print(f"{current_time} Error - Data nahi mila", flush=True)
            
        # Smart Timer (00, 05, 10 par chalne ke liye)
        now = datetime.now()
        seconds_to_wait = 300 - ((now.minute % 5) * 60 + now.second)
        time.sleep(seconds_to_wait)
        
    except Exception as e:
        print("Error aaya:", e, flush=True)
        time.sleep(60)
