#! python3
# item1 
# getOpenWeather.py - Prints the weather for a location from the command line.
# first key
# APPID = '66924581c8ee01ca69f17785672fe03e'
# APPID = 'ed691b0da057dcc2a08be800e77a08c6'
# Zubair key
APPID = 'get api from openweathermap'
import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: get0penWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

# TOD0: Download the JSON data from 0penWeatherMap.org's API.
# T0D0: Load JS0N data into a Python variable.

# item2
# Download the JS0N data from 0penWeatherMap.org's API.

url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location,
APPID)

response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JS0N text:
print(response.text)
# T0DO: Load JS0N data into a Python variable.

# Load JS0N data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.

w = weatherData [ 'list' ]
print('Current weather in %s :' % (location))
print(w[o]['weather'][o]['main'], ' - ', w[o][ 'weather'][o]['description' ])
print()
print('Tomorrow:')
print(w[1]['weather'][o][ 'main'], w[1]['weather'][o]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][o]['main'], ' - ', w[2]['weather'][o][ 'description'])



