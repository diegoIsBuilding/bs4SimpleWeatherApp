
#import beautifulsoup and requests
from bs4 import BeautifulSoup
import requests

#URL forecast.weather.gov 
url = 'https://forecast.weather.gov/MapClick.php?lat=40.7143&lon=-74.006'

try:
    html_text = requests.get(url, timeout = 10)
    html_text.raise_for_status()
    
    soup = BeautifulSoup(html_text.text, 'lxml')
    #Scrape - Temp, Humidity, Wind Speed, Barometer, Dewpoint, Visibilit, and Last Update data
    temprature_f = soup.find('p', class_ = 'myforecast-current-lrg').text 
    weather_condition = soup.find('p', class_ = 'myforecast-current').text
    weather_table_tags = soup.find_all('td')
    #Empty dictionary to collect key:value pairs of weather_data
    weather_data = {}
    #Use a for loop to iterate over the td tags in the weather data
    #
    for td_tag in range(0, len(weather_table_tags), 2):  #Range: we atart at 0 (the beginning of the list of tags) 
        #then go up to the length of the list which is len(weather_table_tags)
        #then increment 2 because the tags have a pattern of the first item containing the key (key: humidity)
        #the second value has the vallue (value: 87%)
        key = weather_table_tags[td_tag].get_text().strip() #Key Extraction: weather_table_tags[td_tag] get the td tag from the current index/position
        #Then extracts the text from the tag and strips any spaces or newlines then stores the value in the 'key' variable
        value = weather_table_tags[td_tag + 1].get_text().strip() #Value Extraction: Gets the next tag which has the value for 
        #the key removes the spaces and newlines and stores it in the 'value' variable
        
        #We are adding the key-value pair to our dictionary - associating the key to the value 
        weather_data[key] = value
    print(weather_data)

except requests.ConnectionError:
    print('Failed to connect to the website')
except requests.Timeout:
    print('The request timed out')
except requests.RequestException as e:
    print(f'An error occurred while fetching the data: {e}')
except Exception as e: 
    print(f'An unexpected error occurred: {e}')