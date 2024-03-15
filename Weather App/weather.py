import gradio as gr
import requests
from datetime import datetime

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def is_valid_zip_code(zip_code):
    return zip_code.isdigit() and len(zip_code) == 5  

def get_weather_info(location_input):
    api_key = "5229ff7d855af9108a0dcbff68b41eff"

    if is_valid_zip_code(location_input):
        query = f'zip={location_input}'
    else:
        query = f'q={location_input}'

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?{query}&appid={api_key}'

    response = requests.get(weather_url)
    weather_info = response.json()

    if response.status_code == 200:
        kelvin = 273
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        result = f"Weather of: {location_input}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        result = f"Weather for '{location_input}' not found!\nKindly enter a valid city name or zip code."

    return result

# Define Gradio interface
input_text = gr.Textbox(label="Enter city name or zip code")
output_text = gr.Textbox(label="Weather Info")

gr.Interface(get_weather_info, inputs=input_text, outputs=output_text, title="Weather Info", description="Enter a city name or zip code to get the weather information.").launch()
