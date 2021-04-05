# -*- coding: utf-8 -*-
"""
Ian O'Rourke
Mar 24, 2021
Python 2 - DAT 129 - SP21
API Assignment
National Weather Service Stations Analysis
"""

# Test run. Test run 2.

# Inquiry question: Looking at the elevation provided in the data, how does the
# distribution of weather stations look in the state of Pennsylvania? Are they
# evenly distributed throughout the state or do they appear to be restricted to
# more mountainous areas of the time?

# Importing necessary modules
import requests, json

# Defining main().
def main():
    # Setting up User-Agent per instruction from https://api.weather.gov
    api_requester = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    # Variable set up for API endpoint.
    api_endpoint = 'https://api.weather.gov/stations?state=PA'
    # Variable set for response from API endpoint as well as status_code test
    # to ensure status code 200.
    response = requests.get(api_endpoint)
    #print(response.status_code)
    # JSON-object dictionary generated from successful response.
    payload_objects = json.loads(response.text)
    
    # From initial examination of the dictionary. 'features' appears to contain
    # the data needed for the inquiry. Variable created to help isolate the
    # desired data.
    stations = payload_objects['features']
    
    # List comprehension to narrow desired data further.
    new_list = [i['properties'] for i in stations]
    
    sta_ids = []
    town_ids = []
    
    for item in new_list:
        sta_ids.append(item['stationIdentifier'])
        town_ids.append(item['name'])
        
    #counter = 0
    #for item in town_ids:
    #    counter += 1
    #    print(counter,') ',item)
    
    # List of stations with associated towns/cities.
    #counter = 0
    #for item in new_list:
    #    counter += 1
    #    print(counter,') ',item['stationIdentifier'],':',item['name'])
    
    # Lambda funcion to isolate the elevation values.
    newer_list = list(map(lambda newer_list: newer_list['elevation'], new_list))
    elev_list = []
    for item in newer_list:
        elev_list.append(item['value'])
    
    # Zip function to display them.
    counter = 0
    for (a,b,c) in zip(sta_ids,town_ids,elev_list):
        counter += 1
        print(counter,') ',a,':',b,':',c)
        
    #counter = 0
    #for item in newer_list:
    #    counter += 1
    #    print(counter,') ',item['value'])
        
    
# Main incantation.
if __name__ == "__main__":
   main()