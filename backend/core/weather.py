import os
from dotenv import load_dotenv
from geopy.geocoders import cord

load_dotenv()

class weather():
    def AddressToCord(self,address):
        geolocator = cord(user_agent="my_geocoder")
        location = geolocator.geocode(address)
        return location
        
        
        
    def __init__(self,address):
        self.cord = AddressToCord(address)
        pass
        
    
        