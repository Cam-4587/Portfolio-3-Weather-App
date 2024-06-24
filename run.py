import datetime as dt
import requests

api_key = '7081ca516f3263f1ef1b7cf00ee9cd26'

print("Welcome to the Weather App! This app will allow you to search for the weather in any city in the world.")
while True:
    print("Press 1 for current weather\nPress 2 for 5 day forecast")
    choice = input("Enter your choice: ")
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice: ")
    else:
        if choice == '1':
                city_input = input("Enter city: ")
                weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=imperial&APPID={api_key}").json()
                if weather_data['cod'] == '404':
                        print("No City Found") 
                        city_input = input("Enter city: ")
                else:
                    weather = weather_data['weather'][0]['main']
                    temp = round(weather_data['main']['temp'])
                    temp_celsius = round((temp-32) * 5.0/9.0)
                    feels_like_F = round(weather_data['main']['feels_like'])
                    feels_like_C = round((feels_like_F - 32) * 5.0/9.0)
                    wind_speed = round(weather_data['wind']['speed'])
                    humidity = weather_data['main']['humidity']
                    description = weather_data['weather'][0] ['description']
                    timezone_offset = weather_data['timezone']
                    sunrise = dt.datetime.fromtimestamp(weather_data['sys']['sunrise'] + timezone_offset)
                    sunset = dt.datetime.fromtimestamp(weather_data['sys']['sunset'] + timezone_offset)
                    print(f"The weather in {city_input} is: {weather}")
                    print(f"The temperature in {city_input} is: {temp}ºF or {temp_celsius}ºC")
                    print(f"The temperature feels like: {feels_like_F}ºF or {feels_like_C}ºC")
                    print(f"The wind speed in {city_input} is: {wind_speed} mph")
                    print(f"The humidiy in {city_input} is: {humidity}%")
                    print(f"The description in {city_input} is: {description}")
                    print(f"The sunrise in {city_input} is: {sunrise}")
                    print(f"The sunset in {city_input} is: {sunset}")
        elif choice == '2':
                city_input = input("Enter city: ")
                forecast_data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_input}&appid={api_key}").json()
                if forecast_data['cod'] == '404':
                        print("No City Found")
                        city_input = input("Enter city: ")
                else:
                    print(f"\n5-Day Weather Forecast for {city_input}:\n")
                    current_date = ""
                    for forecast in forecast_data['list']:
                        forecast_time = dt.datetime.fromtimestamp(forecast['dt'])
                        if forecast_time.date() != current_date:
                            current_date = forecast_time.date()
                            temp_kelvin = forecast['main']['temp']
                            temp_celsius = temp_kelvin - 273.15
                            temp_fahrenheit = temp_celsius * (9/5) + 32
                            feels_like_kelvin = forecast['main']['feels_like']
                            feels_like_celsius = feels_like_kelvin - 273.15
                            feels_like_fahrenheit = feels_like_celsius * (9/5) + 32
                            wind_speed = forecast['wind']['speed']
                            humidity = forecast['main']['humidity']
                            description = forecast['weather'][0]['description']

                            print(f"City: {city_input}")
                            print(f"Date: {current_date}")
                            print(f"- General Weather: {description.capitalize()}")
                            print(f"- Temperature: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
                            print(f"- Feels Like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
                            print(f"- Humidity: {humidity}%")
                            print(f"- Wind Speed: {wind_speed} m/s\n")