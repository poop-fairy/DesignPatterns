'''
Challange:
I have a weather service that receives temprature in Celcius, but the American user can only understand Farhenite. 
Use the Adapter design pattern to help the poor American read the temprature
'''

from abc import ABC,abstractmethod
import json
import requests

class GetOpenWeatherAPI():
    
    def __init__(self):
        pass

    def getAPI(self):
        '''
        The API will not be uploaded to GitHub as I've added the JSON file with the API to .gitignore
        You can get the API from 'https://openweathermap.org/api'
        '''
        with open('OpenWeatherAPI.json') as f:
            API = json.load(f)
            API = API["API"]
            if API is None:
                raise Exception('The API Key was not found in the specified location')
            f.close()
        return API

class GetCurrentTempratureInCelcius():

    def __init__(self,city):
        self.api = GetOpenWeatherAPI().getAPI()
        self.city = city
        print("Temprature Service Initialized")

    def getTempratureForTheCity(self):
        
        #Fetching the temprature data from openweathermap
        url = f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api}'
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            #temprature returned from openweathermap is in Kelvin
            temp_in_celcius = (weather_data['main']['temp']) - 273.15
            return temp_in_celcius
        else:
            raise Exception('An unexpected error occured x.x')

class ICelciusToFarheniteAdapter(ABC):
 
    @abstractmethod
    def convertCelciusToFarhenite(self):
        #Should convert temprature in Celcius to Farhenite and return that value 
        pass

class CelciusToFarheniteAdapter(ICelciusToFarheniteAdapter):
    
    def __init__(self, GetCurrentTempratureInCelcius):
        self.temp_in_celcius = GetCurrentTempratureInCelcius.getTempratureForTheCity()
    
    def convertCelciusToFarhenite(self):
        return (self.temp_in_celcius * (9/5)) + 32
    
city = input('Enter city name: ')
current_temprature = GetCurrentTempratureInCelcius(city)
temp_in_farhenite = CelciusToFarheniteAdapter(current_temprature)
print('Hi American, the current Temprature is: {temp} F'.format(temp = temp_in_farhenite.convertCelciusToFarhenite()))