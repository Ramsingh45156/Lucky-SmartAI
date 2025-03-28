import requests  # pip install requests
from Feamale_Voice import speak_F
import time

def is_online(url="http://www.google.com", timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        return 200 <= response.status_code < 300
    except requests.Timeout:
        # print("Timeout Error: Internet is slow or not working.")
        return False
    except requests.ConnectionError:
        # print("Connection Error: Unable to reach the internet.")
        return False
    except Exception as e:
        # print(f"Unexpected Error: {e}")
        return False

def internet_status():
    if is_online():
        return "Hey Sir, where are you? We are online now. System status: ONLINE"
    else:
        return "Hey Sir, system status: NOT ONLINE"

prev_status = None

while True:
    current_status = internet_status()
    if current_status != prev_status:
        speak_F(current_status)
        prev_status = current_status
    time.sleep(5)  # Check status every 5 seconds
