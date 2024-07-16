# **The Weather app**

- The Weather App is an interactive weather app that runs on the Code Institute mock terminal on Heroku.
- Users can choose from 4 options: The current weather, a 5 day weather forecast, current pollen data or historical weather data for a city on any particular day going back as far as 1940.
- Here is the live version of my project. [The Weather app](https://portfolio-3-weather-app-996e7c78d65e.herokuapp.com/).

![image from the website I am responsive of the weather app website](/assets/images/am_i_responsive_image.png)

## **User Stories**
 - I want to be able to find the current weather and a 5 day weather forecast for my city or a city I might be travelling to.
 - I want to search for current pollen levels in my city or a city I am going to as I might have hayfever or respiratory ailments that are affected by pollen.
 - I want to search for historic weather data for research purposes.
 - I want the option to clear the console, making the console more tidy and user friendly.


## **How to use the app**
- The Weather app is an interactive piece of Python code that gives the user four choices: Choice 1 which is current weather, Choice 2 which is a weather forecast, Choice 3 which is Pollen data, and Choice 4 which is historical data.
- The user then inputs either 1,2,3,4 into the choice option to access data for those respective choices.
- Options one and two require the user to input both the city and the country that the city resides in which is then used by the Open Weather Map API to retrieve data for those choices.
- Choice three asks the user for a city whose co-ordinates are collected using the open weather map API
and used by the open meteo API to collect pollen data that is then printed out for the user.
- Choice 4 is the same as choice 3 but asks the user for a date in the yyyy-mm-dd format which is also used by the open meteo API to retrieve historical weather data.
- At the bottom of the data is an option for the user clear the current console or not where the user has to input either 'yes' or 'no'. 

## **Features**
### **Introduction menu**
---
- The user is presented with a line of text that tells the user that they can search for the weather in any city in the world and pollen data in select cities.
- An input section is printed below, outlining the four options for the user with a line to enter their choice.

![Introduction Menu](/assets/images/intro_menu.png)

---
### **Choice 1**
---
Choice 1 allows the user to input both the city and the country that city resides in and the OpenWeatherMap API retrieves data for that city, printing the following conditions at that current time:
- Weather
- Temperature in both degrees Celsius and degrees Fahrenheit.
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
Choice 2 allows the user to input both a city and a country and the OpenWeatherMap API will retrieve data to produce a five-day forecast for that inputted city with the following conditions:
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
Choice 3 allows the user to input the city and the OpenWeatherMap API will get the city coordinates, and then the air quality API from Open-Meteo will retrieve pollen data to be printed out for that location at that time, specifically:
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
Choice 4 allows the user to input a city which the OpenWeatherMap API uses to get the city coordinates. It then asks the user to input a date, and using Open-Meteo's archive API, it prints out the historical weather data for that city, printing out:
- Temperature in degrees Celsius
- Relative humidity
- rainfall
- snowfall
- Wind speed
- The original API printed out weather conditions for every hour, but the code is altered so that it prints out the weather for every 2 hours.

![output for choice 4 in the weather app for Dublin, Ireland](/assets/images/choice_4_output.png)

### **Option to clear console**
At the end of each data output there is an option for the user to clear the console, clearing it will get rid of the current data output and bring the user back to the choices menu. Not clearing the console will keep the current data and show the choices menu.

![option to clear the console](/assets/images/console_clear.png)

## **Data validation**

### **Choices 1 and 2**

Data validation is added for choices 1 and 2 so that if an invalid value is input for the city input or the country output, as well as if no input is entered for either, then the user is prompted to enter the input for a city and country again.

![Data validation for choices 1 and 2](/assets/images/data_validation_choices_1_and_2.png)

### **Choices 3 and 4**
Data validation is added for choices 3 and 4 so that if an invalid value is input for the city or if no input is entered, then the user is prompted to enter the input for the city again. For choice 4, if the user inputs a date that isn't in the correct date format, nothing is entered or the date given is out of range, then the user is prompted to enter the date again.

![Data validation for choices 3 and 4](/assets/images/data_validation_choices_3_and_4.png)


### **Clearing the console**

The option to clear the console at the end of each data output has data validation making sure that if don't input a yes or no value or leave the input blank then the user user will be asked again to input either yes or no.

![Data validation clearing the console](/assets/images/console_clear_data_validation.png)

### **Option to print out co-ordinates for inputed city** 
Within the Python code there are commented out sections in all four choices giving devlopers the option to print out the latitude and longitude for any of the 4 choices which can be used for cross checking their inputs to see if the data being outputed is from the city they intended to look up.  

### **Python data validation**

My code has been put into the CI python Linter code validator and has returned no Errors.

![pep8ci python code validation](/assets/images/python_validation.png)

### **Data testing**
These are five different data tests, testing its functionality and accuracy concerning the different inputs used in scenarios against the expected output.

|Test Case|Description|Inputs|Expected Output|Result(Pass/Fail)|
|---------|-----------|------|---------------|-----------------|
|1|Current Weather(Valid input)|City: London, Country: UK|Current weather data for London, UK|Pass|
|2|5-Day Forecast (Invalid City Input)|City: Invalid City, Country: UK|Error message indicating city not found |Pass|
|3|Pollen Data (Valid Input)|City: Paris|Pollen data for Paris|Pass|
|4|Historical Data (Valid Date Range)|City: Berlin, Date: 15/08/1990|Historical weather data for Berlin on 15/08/1990|Pass|
|5|	Historical Data (Date Out of Range)|City: Rome, Date: 01/01/1930|Error message indicating date is out of range|Pass|

---
### Image of first test including both the output and corrosponding weather from the Met office
---
 ![1st data test image](/assets/images/data_testing_1.png)

---
### Image of the output from the second test
---
![2nd data test image](/assets/images/data_testing_2.png)
---
### Image of the output from the 3rd test compared to the pollen data from open meteo
---
![3rd data test image](/assets/images/data_testing_3.png)

---
 ### Image of the output from the 4th test with the data extracted from open meteo for comparison
 [API call data for Berlin, 15/08/1990](https://archive-api.open-meteo.com/v1/archive?latitude=52.5244&longitude=13.4105&start_date=1990-08-15&end_date=1990-08-15&hourly=temperature_2m,relative_humidity_2m,rain,snowfall,wind_speed_10m)
---
![4th data test image](/assets/images/data_testing_4.png)

---
 ### Image of the output from the 5th test with the data extracted from open meteo for comparison
---
![5th data test image](/assets/images/data_testing_5.png)

## **Deployment**

This project was deployed using Code Institue's mock terminal for Heroku.

- Steps for deployment:
    - Select create new app on Heroku.
    - Enter the applications name and select Europe for the region then select create app.
    - In the Settings tab, set the buildbacks to Python and NodeJs in that order.
    - In Config Vars I added my api key and port 8000.
    - in the Deploy tab, select Github for the deployment method and link the Heroku app to the Github repository.
    - Select deploy branch under manual deploy.

## **Credits**
 [Weather API Tutorial in Python](https://www.youtube.com/watch?v=9P5MY_2i7K8)
This tutorial from NueralNine showed me how to extract different weather conditions from an open weather map API so they can be printed out in the console at that current time.

[Python Weather App in 8 Minutes](https://www.youtube.com/watch?v=Y84MGU_ZL18)

This weather app tutorial from Baraltech helped me include using an input method to put in the city with an if statement to deal with any 404 errors for both the weather data and the forecast data.

[Weather Past or forecast?](https://weather-past-or-forecast.herokuapp.com/)

This weather app Python project from my code institute tutor helped give me the idea to add a choice section to my Python code to allow the users to pick what option they want to pick from the weather app.

[Open Meteo Air quality API](https://open-meteo.com/en/docs/air-quality-api),  [Open Meteo Historical weather API](https://open-meteo.com/en/docs/historical-weather-api)

The Air Quality API and historical APIs from Open-Meteo under the Python section in API Response were used to build the code for my third and fourth choices in the Python weather app.

[How To Create And Use .env Files In Python](https://www.geeksforgeeks.org/how-to-create-and-use-env-files-in-python/)

This page helped me import the right modules to run.py, add the API_KEY to the.env file, and put in the right code to use my API_KEY for deployment on Heroku whilst also being able to hide it in Gitignore for confidentiality purposes.

[Pycountry Github page](https://github.com/pycountry/pycountry)

This Pycountry Git hub page helped me incorporate 'pycountry.countries.get()' into my code as well as using 'name = country' and the alpha_2 attribute so country codes can be used in API requests to make the request more specific for the user.


[Clear console in python](https://ask.replit.com/t/clear-console-in-python/65265)

This Replit Ask webpage showed me the clear function from the replit package that I have incorporated into my code to give the users the option to clear the console.

#### **The Code institute team**
The code institute Tutoring team helped me when my code wasn't being deployed on the Heroku mock terminal so that my code would be functional on the terminal with no errors.

My code institute tutor for highlighting the error in the forecast data that lead to me adding the country inputs to my code, making the data requests more accurate for the user. Also for suggesting the clear console feature and printing dotted lines that have helped make the app for user friendly.


## **Bugs**

When I first deployed the project to Heroku, I got the error message FileNotFoundError: No such file or directory:  "api_key.txt."  So I took the following steps to make sure my api_key could be read without breaching any confidentiality issues:

- I consulted the code institute tutors twice, putting the API_KEY variable in.env, placing.env in Gitignore, importing 'os', and adding 'from dotenv import load_dotenv' to run.py.
- Adding python-dotenv == 0.21.0 and requests == 2.26.0 to requirements.txt and changing the API key in config vars on Heroku to API_KEY to match the variable in.env.

After this my console on Heroku was still running into an error message so after another discussion with a code institute tutor it was pointed out to me that on config vars on Heroku the value for my API_KEY had a blank line underneath the API value that was also being read. So after removing that blank line my API was able to be read properly and the code on the Heroku console was functional.

Before using country inputs to make my API requests more specific, there was an issue for choice 2 where if you entered Dublin it wasn't producing the forecast for Dublin, Ireland. Then when I went to the open weather map weather search and searched for Dublin the first result was Dublin in California and Dublin in Ireland was the fourth result meaning the printed results were printing Dublin in Calfornia.

- To resolve this the chatbot on the Open Weather map suggested using the country code alongside the city input when making an API request to make it more specific. 
- I applied this both choices 1 and 2 where this can be an issue, alongside the pycountry module to make these API requests more specific.