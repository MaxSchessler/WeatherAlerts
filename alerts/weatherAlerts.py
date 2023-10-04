import requests

import time
from alerts import send_message


def get_weather_data(latitude, longitude):
    api_url =  f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_probability_max"
	
    response = requests.get(api_url)
    weather_data = response.json()
		
    return weather_data

def get_f_degrees(celcius):
      return (celcius * (9/5) + 32)



def send_weather_update():
	# hardcode long and lat for lincoln
    latitude = 40.8136
    longitude = 96.7026

    weather_data = get_weather_data(latitude, longitude)

    temp_max = get_f_degrees(weather_data["daily"]["temperature_2m_max"])
    print(temp_max)
    
    send_message("test", "+14023264360")
	

            
send_weather_update()