import openmeteo_requests
import requests_cache
import datetime as dt
import requests
from retry_requests import retry
import pandas as pd

api_key = open('api_key.txt', 'r').read()

print("Welcome to the Weather App! This app will allow you to search for the weather in any city in the world.")
while True:
    print("Press 1 for current weather\nPress 2 for 5 day forecast\nPress 3 for current Pollen data (data available in Europe as far eastwards as Armenia and including North Africa)")
    choice = input("Enter your choice: ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1,2 or 3.")
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
                    rain = weather_data.get('rain', {'3h': 0})
                    timezone_offset = weather_data['timezone']
                    sunrise = dt.datetime.fromtimestamp(weather_data['sys']['sunrise'] + timezone_offset)
                    sunset = dt.datetime.fromtimestamp(weather_data['sys']['sunset'] + timezone_offset)
                    print(f"The weather in {city_input} is: {weather}\n")
                    print(f"The temperature in {city_input} is: {temp}ºF or {temp_celsius}ºC\n")
                    print(f"The temperature feels like: {feels_like_F}ºF or {feels_like_C}ºC\n")
                    print(f"The wind speed in {city_input} is: {wind_speed} mph\n")
                    print(f"The humidiy in {city_input} is: {humidity}%\n")
                    print(f"The description in {city_input} is: {description}\n")
                    print(f"The sunrise in {city_input} is: {sunrise}\n")
                    print(f"The sunset in {city_input} is: {sunset}\n")
                    print(f"The current rainfall in {city_input} is: {rain.get('1h', 0)}mm\n")
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
                            rain = forecast.get('rain', {}).get ('3h', 0)

                            print(f"City: {city_input}")
                            print(f"Date: {current_date}")
                            print(f"- General Weather: {description.capitalize()}")
                            print(f"- Temperature: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
                            print(f"- Feels Like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
                            print(f"- Humidity: {humidity}%")
                            print(f"- Wind Speed: {wind_speed} m/s")
                            print(f"- Rainfall: {rain}mm")
                            print("\n")
        elif choice == '3':
                while True:
                    city_name = input("Enter the city name: ")
                    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}"
                    response = requests.get(url)
                    data = response.json()

                    if response.status_code == 404 or not data:
                        print("City not found. Please enter a valid city name.")
                        continue

                    # Assuming API returns data, take the first result
                    if data:
                        lat = data[0]['lat']
                        lon = data[0]['lon']
                        print(f"Latitude: {lat}, Longitude: {lon}")
                        break

                cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
                retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
                openmeteo = openmeteo_requests.Client(session = retry_session)


                pollen_data = "https://air-quality-api.open-meteo.com/v1/air-quality"
                params = {
                    "latitude": lat,
                    "longitude": lon,
                    "current": ["alder_pollen", "birch_pollen", "grass_pollen", "mugwort_pollen", "olive_pollen", "ragweed_pollen"],
                    "start_date": "2024-06-28",
                    "end_date": "2024-06-28"
                }
                responses = openmeteo.weather_api(pollen_data, params=params)


                response = responses[0]


                current = response.Current()
                current_alder_pollen = current.Variables(0).Value()
                current_birch_pollen = current.Variables(1).Value()
                current_grass_pollen = current.Variables(2).Value()
                current_mugwort_pollen = current.Variables(3).Value()
                current_olive_pollen = current.Variables(4).Value()
                current_ragweed_pollen = current.Variables(5).Value()

                print(f"\n{city_name}")
                print(f"\nCurrent alder pollen {current_alder_pollen} Grains/m³\n")
                print(f"Current birch pollen {current_birch_pollen} Grains/m³\n")
                print(f"Current grass pollen {current_grass_pollen} Grains/m³\n")
                print(f"Current mugwort pollen {current_mugwort_pollen} Grains/m³\n")
                print(f"Current olive pollen {current_olive_pollen} Grains/m³\n")
                print(f"Current ragweed pollen {current_ragweed_pollen} Grains/m³\n")
