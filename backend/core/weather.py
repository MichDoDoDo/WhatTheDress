import os
import requests
import pytz
import JSON

from dotenv import load_dotenv
from geopy.geocoders import cord
from datetime import date 
from timezonefinder import TimezoneFinder
load_dotenv()

class weather():
              
    def __init__(self,address):
        self.cord = self.AddressToCord(address)
        data = None
        pass
    
    def AddressToCord(self,address):
        geolocator = cord(user_agent="my_geocoder")
        location = geolocator.geocode(address)
        return location
    
    def GetTimeZone(self):
        tf = TimezoneFinder()
        timezone_name = tf.timezone_at(lng=self.cord.longitude, lat=self.cord.latitude)
        if timezone_name:
            timezone = pytz.timezone(timezone_name)
            offset = timezone.utcoffset(date.now()).total_seconds() / 3600
            hours = int(offset)
            minutes = int((offset % 1) * 60)
            return f"{hours:+03}:{minutes:02}" 
        else:
            return None
    
        
   
    def GetWeather(self):
        currDate = date.today()
        formattedDate = currDate.strftime("%Y/%m/%/d") 
        Api = os.getenv("WEATHER_API") 
        tz = self.GetTimeZone()
        
        url = f'https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={self.cord.latitude}&lon={self.cord.longitude}&date={formattedDate}&tz={tz}&appid={Api}'
        
        try:
            reponse = requests.get(url)
            self.data = JSON.dump(reponse.json())
            
        except Exception as e: 
            print("bruh")
            
    
        
    
        