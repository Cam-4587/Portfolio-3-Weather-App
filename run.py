import os
from dotenv import load_dotenv
import openmeteo_requests
import requests_cache
import datetime as dt
import requests
from retry_requests import retry
import pandas as pd
import re
from replit import clear
import pycountry

#Load environment variables from .env file
load_dotenv() 
api_key = (os.getenv("API_KEY"))

#Print welcome message to the user
print("Welcome to the Weather App! This app will allow you to search for the weather in any city in the world, and pollen data for selected cities.")

#Start an infiinite loop to keep the program running
while True:
    # Print the options for the user
    print("Press 1 for current weather\nPress 2 for 5 day forecast\nPress 3 for current Pollen data (data available in Europe as far eastwards as\nArmenia and including North Africa)\nPress 4 for historical data going as far back as 1940")
    
    # Get the user's choice
    choice = input("Enter your choice: ")

    #validate the user's choice
    while choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter 1,2,3 or 4.")
        choice = input("Enter your choice: ")
    #handle the user's choice
    else:
        if choice == '1':
            # Get the current weather for a city
            while True:
                city_input = input("Enter city: ")
                country_input = input("Enter country: ")
                country_code = pycountry.countries.get(name=country_input)
                if country_code is None:
                    print("Invalid country name. Please enter a valid country name.")
                    continue

                # Validate city and country input
                url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_input},{country_code.alpha_2}&appid={api_key}"
                response = requests.get(url)
                data = response.json()
                if response.status_code == 404 or not data:
                    print("City not found. Please enter a valid city name and country.")
                    continue
                
                lat = data[0]['lat']
                lon = data[0]['lon']

                country_code = data[0]['country']
                weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_input},{country_code}&units=imperial&APPID={api_key}").json()

                # Check if the city was found
                if weather_data['cod'] == '404':
                    print("No City Found")
                    continue
                # Extract the current weather data for that city
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
                    # Print the weather data for that city
                    print("\n"*3)
                    print("-------------------------------------------------------")
                    print(f"The weather in {city_input} is: {weather}")
                    print("-------------------------------------------------------")
                    #option to print latitude and longitude for city
                    print(f"Latitude: {lat}, Longitude: {lon}")
                    print("-------------------------------------------------------")
                    print(f"The temperature in {city_input} is: {temp}ºF or {temp_celsius}ºC\n")
                    print(f"The temperature feels like: {feels_like_F}ºF or {feels_like_C}ºC\n")
                    print(f"The wind speed in {city_input} is: {wind_speed} mph\n")
                    print(f"The humidiy in {city_input} is: {humidity}%\n")
                    print(f"The description in {city_input} is: {description}\n")
                    print(f"The sunrise in {city_input} is: {sunrise}\n")
                    print(f"The sunset in {city_input} is: {sunset}\n")
                    print(f"The current rainfall in {city_input} is: {rain.get('1h', 0)}mm\n")
                    print("-------------------------------------------------------")
                    break
        elif choice == '2':
            # Get the 5-day weather forecast for a city
            while True:
                city_input = input("Enter city: ")
                country_input = input("Enter country: ")
                country_code = pycountry.countries.get(name=country_input)
                if country_code is None:
                    print("Invalid country name. Please enter a valid country name.")
                    continue

                # Validate city and country input
                url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_input},{country_code.alpha_2}&appid={api_key}"
                response = requests.get(url)
                data = response.json()
                if response.status_code == 404 or not data:
                    print("City not found. Please enter a valid city name.")
                    continue

                lat = data[0]['lat']
                lon = data[0]['lon']

                country_code = data[0]['country']
                forecast_data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_input},{country_code}&appid={api_key}").json()

                # Check if the city was found
                if forecast_data['cod'] == '404':
                    print("No City Found")
                    continue
                # Extract the 5 day weather forecast data for that city
                else:
                    print("\n"*3)
                    print("-------------------------------------------------------")
                    print(f"5-Day Weather Forecast for {city_input}:")
                    #option to print latitude and longitude for city
                    print("-------------------------------------------------------")
                    print(f"Latitude: {lat}, Longitude: {lon}")
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
                        # print the 5 day weather forecast for that city
                            print("-------------------------------------------------------")
                            print(f"City: {city_input}")
                            print(f"Date: {current_date}")
                            print(f"- General Weather: {description.capitalize()}")
                            print(f"- Temperature: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
                            print(f"- Feels Like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
                            print(f"- Humidity: {humidity}%")
                            print(f"- Wind Speed: {wind_speed} m/s")
                            print(f"- Rainfall: {rain}mm")
                            print("-------------------------------------------------------")
                break
        elif choice == '3':
            # Get current pollen data for a city
                while True:
                    city_name = input("Enter the city name: ")
                    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}"
                    response = requests.get(url)
                    data = response.json()
            # Check if the city was found
                    if response.status_code == 404 or not data:
                        print("City not found. Please enter a valid city name.")
                        continue

            # Extract latitude and longitued for the city
                    if data:
                        lat = data[0]['lat']
                        lon = data[0]['lon']
                        break
            # Set up caching and retry mechanisms
                cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
                retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
                openmeteo = openmeteo_requests.Client(session = retry_session)

            # Specifying the Parameters needed to make a request to the API that provides pollen data.
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

            # Extract pollen data
                current = response.Current()
                current_alder_pollen = current.Variables(0).Value()
                current_birch_pollen = current.Variables(1).Value()
                current_grass_pollen = current.Variables(2).Value()
                current_mugwort_pollen = current.Variables(3).Value()
                current_olive_pollen = current.Variables(4).Value()
                current_ragweed_pollen = current.Variables(5).Value()
                # Print pollen data and city name
                print("\n"*3)
                print("-------------------------------------------------------")
                print(f"{city_name}")
                #option for future users to print co-ordinates for cross-checking
                #print("-------------------------------------------------------")
                #print(f"Latitude: {lat}, Longitude: {lon}")
                print("-------------------------------------------------------")
                print(f"Current alder pollen {current_alder_pollen} Grains/m³\n")
                print(f"Current birch pollen {current_birch_pollen} Grains/m³\n")
                print(f"Current grass pollen {current_grass_pollen} Grains/m³\n")
                print(f"Current mugwort pollen {current_mugwort_pollen} Grains/m³\n")
                print(f"Current olive pollen {current_olive_pollen} Grains/m³\n")
                print(f"Current ragweed pollen {current_ragweed_pollen} Grains/m³\n")
                print("-------------------------------------------------------")
        elif choice == '4':
            cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
            retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
            openmeteo = openmeteo_requests.Client(session=retry_session)

            while True:
            # Get historical weather data for a city
                city_name = input("Enter the city name: ")
                url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}"
                response = requests.get(url)
                data = response.json()
            
            # Check if the city was found
                if response.status_code == 404 or not data:
                    print("City not found. Please enter a valid city name.")
                    continue
            # Extract latitude and longitude for the city
                if data:
                    lat = data[0]['lat']
                    lon = data[0]['lon']
                    break
            while True:
            # Date input from the user
                date = input("Enter a valid date format (YYYY-MM-DD): ")
            # Date validation
                if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
                    print("Error: Invalid date format. Please try again.")
                    continue
                break
            url = "https://archive-api.open-meteo.com/v1/archive"
            # Specifying the Parameters needed to make a request to the API that provides the historical data.
            params = {
                "latitude": lat,
                "longitude": lon,
                "start_date": date,
                "end_date": date,
                "hourly": ["temperature_2m", "relative_humidity_2m", "rain", "snowfall", "visibility", "wind_speed_10m"]
            }

            # Retrieve the weather data from the Open-Meteo API
            responses = openmeteo.weather_api(url, params=params)
            response = responses[0]

            # Extract historical data
            hourly = response.Hourly()
            hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
            hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
            hourly_rain = hourly.Variables(2).ValuesAsNumpy()
            hourly_snowfall = hourly.Variables(3).ValuesAsNumpy()
            hourly_wind_speed_10m = hourly.Variables(5).ValuesAsNumpy()

            # Create a dictionary to store three-hourly data
            three_hourly_data = {"Date and time": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(hours=2),
            inclusive="left")
            }

            # Populate the dictionary with data, selecting every 3rd hour
            three_hourly_data["Temperature °C"] = hourly_temperature_2m[::2] # Select every 3rd hour 
            three_hourly_data["Relative humidity %"] = hourly_relative_humidity_2m[::2]
            three_hourly_data["Rain mm"] = hourly_rain[::2]
            three_hourly_data["Snowfall"] = hourly_snowfall [::2]
            three_hourly_data["Wind speed kph"] = hourly_wind_speed_10m[::2]
            
            # Create a DataFrame from the dictionary
            three_hourly_dataframe = pd.DataFrame(data=three_hourly_data)

            # Print the data row by row
            print("\n"*3)
            print("-------------------------------------------------------")
            print(f"Historical Weather Data for {city_name} on {date}:")
            #option for future users to print co-ordinates for cross-checking
            #print("-------------------------------------------------------")
            #print(f"Latitude: {lat}, Longitude: {lon}")
            print("-------------------------------------------------------")
            for index, row in three_hourly_dataframe.iterrows():
                print(row.to_string())
                print("-------------------------------------------------------")       
            # Ask the user if they would like to clear the console
        clear_console = input("Would you like to clear the console? (yes/no): ").lower()
        if clear_console in ['yes', 'y']:
            clear()
        while clear_console not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            clear_console = input("Would you like to clear the console? (yes/no): ").lower()
        