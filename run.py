import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

city_input = input("Enter city: ")

weather_data = requests.get (f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=imperial&APPID={api_key}")

