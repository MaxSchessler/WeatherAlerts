import requests

import time
from alerts import send_message, get_f_degrees


def get_weather_data(latitude, longitude):
    api_url =  f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_probability_max"
	
    response = requests.get(api_url)
    weather_data = response.json()
		
    return weather_data


def send_weather_update():
	# hardcode long and lat for lincoln
    latitude = 40.8136
    longitude = 96.7026

    weather_data = get_weather_data(latitude, longitude)

    temp_max = get_f_degrees(weather_data["daily"]["temperature_2m_max"][0])
    temp_min =  get_f_degrees(weather_data["daily"]["temperature_2m_min"][0])
    sunrise = weather_data["daily"]["sunrise"][0]
    sunset = weather_data["daily"]["sunset"][0]
    precipitation_probibility = weather_data["daily"]["precipitation_probability_max"][0]
    
    message_body = f"""
    Good Morning Max,

    Current Today in Lincoln Nebraska:
    High: {temp_max}
    Low: {temp_min}
    Sunrise: {sunrise}
    Sunset: {sunset}
    Percent chance of rain: {precipitation_probibility}

    Have a wonderful day!
"""

    print(message_body)
    
    send_message(message_body, "+14023264360")
	

            
send_weather_update()