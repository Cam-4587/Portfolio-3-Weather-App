# **The Weather app**

- The Weather App is an interactive weather app that runs on the Code Institute mock terminal on Heroku.
- Users can choose from 4 options: a weather forecast, a 5 day weather forecast, the current pollen data for a city that the user will input, and the 4th option provides historical data for a city and dates inputted going back as far as 1940.
- Here is the live version of my project. This site was built using [The Weather app](https://portfolio-3-weather-app-996e7c78d65e.herokuapp.com/).

![image from the website I am responsive of the weather app website](/assets/images/am_i_responsive_image.png)

## **How to use the app**

- The weather app is an interactive piece of Python code that guides the users through four choices for a forecast: current weather, pollen data, and historical weather data.
- Two APIs are used in this code. One is from OpenWeatherMap, and the other is from OpenMeteo.
- The first two options retrieve weather data for that city using the OpenWeatherMap. The second two options use the OpenWeatherMap API to retrieve the inputted city's coordinates and the Open-Meteo API to retrieve the pollen data and historical data using those coordinates.
- For options three and four, the user has to input a city, and the code output will be produced.

## **Features**
### **Introduction menu**
---
- The user is presented with a line of text that tells the user that they can search for the weather in any city in the world and pollen data in select cities.
- An input section is printed below, outlining the four options for the user with a line to enter their choice.

![Introduction Menu](/assets/images/intro_menu.png)

---
### **Choice 1**
---
Choice 1 allows the user to input a city, and the OpenWeatherMap API retrieves data for that city, printing the following conditions at that current time.
- Weather
- temperature in both degrees Celsius and degrees Fahrenheit.
- What temperature does it feel like in both degrees Celsius and degrees Fahrenheit.
- The wind speed
- Humidity
- Weather description
- Sunrise and sunset
- Rain

![output for choice 1 in the weather app for Dublin, Ireland](/assets/images/choice_1_output.png)

---
### **Choice 2**
---
Choice 2 allows the user to input a city and the OpenWeatherMap API to produce a five-day forecast for that inputted city with the following conditions:.
- Weather
-Temperature in both degrees Celsius and degrees Fahrenheit.
- Wind Speed
- Humidity
- Weather description
- Rainfall

![output for choice 2 in the weather app for Dublin, Ireland](/assets/images/choice_2_output.png)  

---
### **Choice 3**
---
Choice 3 allows the user to input the city and the OpenWeatherMap API to get the city coordinates, and then use the air quality API from Open-Meteo to print out pollen data for that location at that time, specifically.
- Alder pollen
- Birch pollen
- grass pollen
- Mugwort pollen
- Olive pollen
- Ragweed pollen

![output for choice 3 in the weather app for Dublin, Ireland](/assets/images/choice_3_output.png)  

---
### **Choice 4**
---
Choice 4 allows the user to input a city and the OpenWeatherMap API to get the city coordinates. It then asks the user to input a date, and using Open-Meteo's archive API, it prints out the historical weather data for that city at that date printing out:
- Temperature in degrees Celsius
- Relative humidity
- rainfall
- snowfall
- Wind speed
- The original API printed out weather conditions for every hour, but the code is altered so that it prints out the weather for every 3 hours.

![output for choice 4 in the weather app for Dublin, Ireland](/assets/images/choice_4_output.png)

## Data validation

### Choices 1 and 2

Data validation is added for choices 1 and 2 so that if an invalid value is input for the city input or the country output, as well as if no input is entered for either, then the user is prompted to enter the input for a city and country again.

![Data validation for choices 1 and 2](/assets/images/data_validation_choices_1_and_2.png)

### Choices 3 and 4
Data validation is added for choices 3 and 3 so that if an invalid value is input for the city or if no input is entered, then the user is prompted to enter the input for the city again. For choice 4, if the user inputs a date that isn't in the correct date format or if nothing is entered, then the user is prompted to enter the date again.

![Data validation for choices 3 and 4](/assets/images/data_validation_choices_3_and_4.png)


## **Credits**
 [Weather API Tutorial in Python](https://www.youtube.com/watch?v=9P5MY_2i7K8)
This tutorial from NueralNine showed me how to extract different weather conditions from an open weather map API so they can be printed out in the console at that current time.

[Python Weather App in 8 Minutes](https://www.youtube.com/watch?v=Y84MGU_ZL18)

This weather app tutorial from Baraltech helped me include using an input method to put in the city with an if statement to deal with any 404 errors for both the weather data and the forecast data.

[Weather Past or forecast?](https://weather-past-or-forecast.herokuapp.com/)

This weather app Python project from my code institute tutor helped me incorporate the choice section in my Python code to allow the users to pick what option they want to pick from the weather app.

[Open Meteo Air quality API](https://open-meteo.com/en/docs/air-quality-api),  [Open Meteo Historical weather API](https://open-meteo.com/en/docs/historical-weather-api)

The Air Quality API and historical APIs from Open-Meteo under the Python section in API Response were used to build the code for my third and fourth choices in the Python weather app.

[How To Create And Use .env Files In Python](https://www.geeksforgeeks.org/how-to-create-and-use-env-files-in-python/)

This page helped me import the right modules to run.py, add the API_KEY to the.env file, and put in the write code to use my API_KEY for deployment on Heroku whilst also being able to hide it in.env in Gitignore for confidentiality purposes.

## **Bugs**

When I first deployed the project to Heroku, I got the error message FileNotFoundError: No such file or directory:  "api_key.txt." So I took the following steps to make sure my api_key could be read without breaching any confidentiality issues:

- I consulted the code institute tutors twice, putting the API_KEY variable in.env, placing.env in Gitignore, importing 'os', and adding 'from dotenv import load_dotenv' to run.py.
- Adding python-dotenv == 0.21.0 and requests == 2.26.0 to requirements.txt and changing the API key in config vars on Heroku to API_KEY to match the variable in.env.