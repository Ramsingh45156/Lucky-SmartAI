import requests
import random
from Text_to_speek import speak
from welcome import *


def find_my_ip():
    ip_address=requests.get('https://api.ipify.org?format=json').json()
    return ip_address["ip"]



def get_ip_location():
    text = random.choice(random_text)
    speak(text)
    try:
        ip_info = requests.get("https://ipinfo.io/json").json()
        city = ip_info.get("city", "Delhi")
        return city
    except requests.exceptions.RequestException as e:
        # print("Error occurred while fetching IP location:", e)
        return "Delhi"


def weather_forecast(city):
    api_key = "a6a270b365c923a59cf9db2086008f02"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        res = response.json()
        # print("API Response:", res)
        if res.get("cod") == 200:
            weather = res["weather"][0]["main"]
            temp = res["main"]["temp"]
            feels_like = res["main"]["feels_like"]
            return weather, temp, feels_like
        else:
            return None, None ,None
    except Exception:
        # print("Error occurred while fetching weather data:\n")
        return None
    
    
# x=find_my_ip()
# print(x)
    