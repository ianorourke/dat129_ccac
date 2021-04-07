# -*- coding: utf-8 -*-
"""
Ian O'Rourke
Mar 24, 2021
Python 2 - DAT 129 - SP21
API Assignment
National Weather Service Stations Analysis
"""

# Inquiry question: Looking at the elevation provided in the data, how does the
# distribution of weather stations look in the state of Pennsylvania? Are they
# evenly distributed throughout the state or do they appear to be restricted to
# more mountainous areas of the time?

# Importing necessary modules
import requests, json

def api_requestor():
    '''Makes the API request.'''
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
    return payload_objects  

# Originally these functions were intended to help create a menu for
# the user to navigate the data conveniently, however these are currently
# still under construction.
    
#def menu_displayer(menu_list):
#    '''Displays a menu for information to access.'''
#    counter = 0
#    for option in menu_list:
#        counter += 1
#        print(counter,') ',option,sep='')
        
#def list_sorter(raw_list):
#    '''Sorts into alphabetical order entries from a dictionary value.'''
#    count = 0
#    for report in sorted(raw_list):
#        count += 1
#        print(count,') ',report,sep='')

def list_compmaker(dictionary,sub_dict):
    '''Takes a variable holding nested data and makes a list comprehension.'''
    list_comp = [i[sub_dict] for i in dictionary]
    return list_comp

def list_setter(list_comp,list_one,list_two,sublist_one,sublist_two):
    '''Makes two lists from two parts of a list comprehension.'''
    for item in list_comp:
        list_one.append(item[sublist_one])
        list_two.append(item[sublist_two])

# Under construction for when the issues that arose with the menu functions
# are resolved.
        
#def station_sorter(list_comp,sublist_one,sublist_two):
#    '''Makes a printable list of stations IDs with their associated towns.'''
#   station_counter = 0
#    for item in list_comp:
#        station_counter += 1
#        print(station_counter,') ',item[sublist_one],':',item[sublist_two])

def elev_grabber(l_list,l_sublist,empty_list):
    '''Makes a list from nested values pulled from the lambda function.'''
    for item in l_list:
        empty_list.append(item[l_sublist])
        
def zipper(list_one,list_two,list_three):
    '''Takes three lists and runs them through a zip so that they display nicely.'''
    zip_counter = 0
    for (a,b,c) in zip(list_one,list_two,list_three):
        zip_counter += 1
        print(zip_counter,') ',a,':',b,':',c)
        
def float_maker(mixed_up_list):
    '''Takes a list and ensures its values are all floating.'''
    new_list = []
    for item in mixed_up_list:
        # Values of 0 have been entered as int.
        if item == '0':
            new_list.append(float(0.0))
        # Values of 381 have been entered as int rather than 381.0.
        elif item == '381':
            new_list.append(float(381.0))
        # Ensures everything else is added as is.
        else:
            new_list.append(item)
    return new_list

def none_remover(list_with_nones):
    '''Removes data-type NoneType entries from a list.'''
    for item in list_with_nones:
        if item == None:
            list_with_nones.remove(item)
    return list_with_nones
        
def range_isolator(raw_list,ft_min,ft_range):
    '''Gets the count of how many in a list fit within a range of feet.'''
    temp_list = []
    for item in raw_list:
        if item >= float(ft_min) and item <= float(ft_range):
            temp_list.append(item)
    print(len(temp_list))
    
# Defining main().
def main():
    '''The main to-do.'''
    # Making API contact.
    weather_stations = api_requestor()
    
    # From initial examination of the dictionary. 'features' appears to contain
    # the data needed for the inquiry. Variable created to help isolate the
    # desired data.
    stations = weather_stations['features']
    
    # List comprehension to narrow desired data further.
    station_IDs = list_compmaker(stations,'properties')
    
    # Setting up lists for zip function so that three lists of data will display.
    sta_ids = []
    town_ids = []
    elev_list = []
    
    # Places station ID and town values into the lists.
    list_setter(station_IDs,sta_ids,town_ids,'stationIdentifier','name')
        
    # Lambda funcion to isolate the elevation values.
    lambda_list = list(map(lambda lambda_list: lambda_list['elevation'], station_IDs))
    
    # Places elevation values extracted from the lambda function into the remaining list.
    elev_grabber(lambda_list,'value',elev_list)

    # Greeting the user.
    print('''\nWelcome! Here is a list of weather stations and their locations
    in the state of Pennsylvania as provided by the National Weather Service
    at https://www.weather.gov.''')
    # Instructing the user.
    print('')
    
    # Prints station IDs paired with their locations and elevations.
    #zipper(sta_ids,town_ids,elev_list)
    float_list = float_maker(elev_list)
    # One value for AV195: N36WC-2 Oxford must be excluded from this
    # average as no value was provided.
    clean_list = none_remover(float_list)
    # Lambda functions as recommended for float values from:
    # https://www.geeksforgeeks.org/python-min-max-value-in-float-string-list/
    min_elev = min(clean_list,key=lambda x: float(x))
    max_elev = max(clean_list,key=lambda x: float(x))
    # Getting variables for the counts and averages with the newly cleaned lists.
    count_elev = len(clean_list)
    avg_elev = sum(clean_list)/len(clean_list)
    # Printing out the results for the user.
    print('\nMinimum elevation: ',min_elev,'(Sea Level)')
    print('\nMaximum elevation: ',max_elev,)
    print('\nAverage elevation from the provided total: ',round(avg_elev,3))
    print('''(Please note that this excludes one value, AV195: N3GWC-2 Oxford
as no value was provided)''')
    print('\nTotal number of stations in PA excluding the aforementioned:')
    print(count_elev)
    
    # Groupings by elevation.
    print('\nList of stations elevated between 0 (Sea Level) and 100 ft.')
    range_isolator(clean_list,min_elev,'100.0')
    print('\nList of stations elevated between 100 and 300 ft.')
    range_isolator(clean_list,'100.0','300.0')
    print('\nList of stations elevated between 100 and 500 ft.')
    range_isolator(clean_list,'100.0','500.0')
    print('\nList of stations elevated between 100 and 1000 ft.')
    range_isolator(clean_list,'100.0','1000.0')
    print('\nList of stations elevated between 300 and 500 ft.')
    range_isolator(clean_list,'300.0','500.0')
    print('\nList of stations elevated between 300 and 1000 ft.')
    range_isolator(clean_list,'300.0','1000.0')
    print('\nList of stations elevated between 500 and 1000 ft.')
    range_isolator(clean_list,'500.0','1000.0')
    print('\nList of stations elevated over 1000 ft.')
    range_isolator(clean_list,'1000.0',max_elev)
        
    
# Main incantation.
if __name__ == "__main__":
   main()