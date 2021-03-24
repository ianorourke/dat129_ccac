# -*- coding: utf-8 -*-
"""
Ian O'Rourke
Mar 24, 2021
Python 2 - DAT 129 - SP21
API Assignment
National Weather Service Stations Analysis
"""

# Importing necessary modules
import requests, json

# User-Agent variable set as requested by api.weather.gov
api_requester = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}

# Variable set for endpoint.

api_endpoint = 'https://api.weather.gov/stations?state=PA'
# Test to ensure status code 200.
response = requests.get(api_endpoint)

# Results blotted out after successful test.
#print(response.status_code)
#print(response.text)

# Weather results brought through as a json.
weather_objects = json.loads(response.text)

# Currently blotted out to see results and to scan through for
# potential lists from which data can be pulled and analyzed.
#print(payload_objects)

# 'Features' apparently holds the dictionaries containing the
# relevant data.
stations = weather_objects['features']

# Current data listed here is at its most organized. The relevant
# dictionary keys in order are: '@id', '@type', 'elevation', 'stationIdentifier',
# 'name', 'timeZone', 'forecast', 'county', and 'fireWeatherZone' though
# as 3/24/2021, I have not been able to find a way to better parse the
# data to answer potential questions such as how evenly distributed are
# weather stations across the state of PA or analyzing elevation to see if
# these are more isolated in mountainous parts of the state, etc.

for record in stations:
    for item in record['properties']:
        print(record['properties'][item])

