
#import beautifulsoup and requests
from bs4 import BeautifulSoup
import requests

#URL forecast.weather.gov 
url = 'https://forecast.weather.gov/MapClick.php?lat=40.7143&lon=-74.006'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
#Scrape - Temp, Humidity, Wind Speed, Barometer, Dewpoint, Visibilit, and Last Update data
temprature_f = soup.find('p', class_ = 'myforecast-current-lrg').text 
weather_condition = soup.find('p', class_ = 'myforecast-current').text
weather_table_data = soup.find_all('td')
#Empty dictionary to collect key:value pairs of weather_data
weather_data = {}
#Use a for loop to iterate over the td tags in the weather data
#
for index in range(0, len(weather_table_data), 2):  # Jumping in steps of 2 because one is key and the other is value
    key = weather_table_data[index].get_text(strip=True)   # Extracting text and removing any extra spaces
    value = weather_table_data[index + 1].get_text(strip=True)
    weather_data[key] = value
