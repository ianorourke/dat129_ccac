# National Weather Forecast API Assignment

## Sources

[National Weather Service](https://www.weather.gov/)
[Maps & Geographical Information](https://www.statelibrary.pa.gov/GeneralPublic/Learn/Genealogy-and-Local-History/Pages/Maps--Geographical-Information.aspx)

(to provide some context)
Peer learning sources:

[Lambda Functions as explained by Rachael Shockey](https://github.com/rachaelshockey/peer_teaching_lambda)
[Line Comprehensions as explained by Alissa Horton](https://github.com/ahort0bCCAC/dat129_ccac/blob/main/peerTeaching_Comprehensions.py)
[Additional sources for lambda functions:](https://www.geeksforgeeks.org/python-min-max-value-in-float-string-list/)
And as always:
Deitel, P. J., & Deitel, H. M. (2020). Intro to Python for computer science and data science: Learning to program with AI, 
big data and the cloud. Upper Saddle River, NJ: Pearson.

## About the Data Provided

Following the in-class exercise, a function has been set up to send a request to the API endpoint as provided by https://www.weather.gov.
A large number of endpoints are provided and the one settled one was Stations, provided a list, state by state of the number of weather
stations per state. For the purposes of the assignment, weather stations for Pennsylvania were chosen and after a successful test.
Per the instructions of the website, a variable for the 'User-Agent' was requested but this resulted in not being necessary. After a successful
status code of 200, the results were converted into a JSON-object to be further scanned for any meaningful data.

```
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
```
Some research into the JSON object itself in order to find the right values to parse was required resulting in these particular values
of note.

```
# From initial examination of the dictionary. 'features' appears to contain
    # the data needed for the inquiry. Variable created to help isolate the
    # desired data.
    stations = weather_stations['features']

```

It would be here that the notable data of weather station IDs, their locations, and a list of elevations could be derived allowing the
formation of inquiry question for further investigation.


## Inquiry Question

Looking at the elevation provided in the data, how does the distribution of weather stations look in the state of Pennsylvania? 
Are they evenly distributed throughout the state or do they appear to be restricted to more mountainous areas of the time?

Due to the desired data being quite well nested, a number of different methods were needed to extract the necessary data.
First, by list comprehension, to extract data regarding station IDs and station locations:
```

    # List comprehension to narrow desired data further.
    station_IDs = list_compmaker(stations,'properties')
    
```
Then lambda functions to extract the remaining desired data, the data regarding elevations, that continued to be further nested as
a value.
```
# Lambda funcion to isolate the elevation values.
    lambda_list = list(map(lambda lambda_list: lambda_list['elevation'], station_IDs))
    
```

This data would be put into three new lists for convenient access.
```
# Setting up lists for zip function so that three lists of data will display.
    sta_ids = []
    town_ids = []
    elev_list = []
    
    # Places station ID and town values into the lists.
    list_setter(station_IDs,sta_ids,town_ids,'stationIdentifier','name')
        
    ...
    
    # Places elevation values extracted from the lambda function into the remaining list.
    elev_grabber(lambda_list,'value',elev_list)

```

Furthermore, due to the elevation data listed as floating values, an additional function was created to ensure all values
such as '0' (sea level, of which there were 8) and '381' (ft., of which there were 3) would be interpreted as floating. Only one value, 
the value for Station ID: AV195: N3GWC-2 Oxford, had no value at all (None) and had to be removed using another function for the 
purposes of trying to come up with average elevation.

```
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

...

    float_list = float_maker(elev_list)
    # One value for AV195: N36WC-2 Oxford must be excluded from this
    # average as no value was provided.
    clean_list = none_remover(float_list)
    
```
Here, additional lambda functions were used to generate the minimum and maximum elevations
```
    min_elev = min(clean_list,key=lambda x: float(x))
    max_elev = max(clean_list,key=lambda x: float(x))

```

From here, the results could now be generated.

![Min and max elevation, total, average, and note of exclusions](https://github.com/ianorourke/dat129_ccac/blob/a61532068c9eaf961622c11b5a499064f0c0a857/api1.png)

And for more meaningful results with which to answer the initial inquiry question, an additional
function was constructed and ran with a number of ranges to provide totals within those ranges to
get a better glimpse of what those elevations could tell the user.

```
...

def range_isolator(raw_list,ft_min,ft_range):
    '''Gets the count of how many in a list fit within a range of feet.'''
    temp_list = []
    for item in raw_list:
        if item >= float(ft_min) and item <= float(ft_range):
            temp_list.append(item)
    print(len(temp_list))
    
...

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
    
```
Producing these results:

![Ranges of elevation](https://github.com/ianorourke/dat129_ccac/blob/a61532068c9eaf961622c11b5a499064f0c0a857/api2.png)

From the results generated here, out of a total of 928 (including Oxford, which was excluded from the average due to no value
being provided), the average given in 308.826 (ft) and only one result over 1000 ft suggesting (and that is the maximum value) 
that these are not necessarily isolated to the more mountainous areas of the state, rather than they tend to be evenly distributed 
across the state though arguably in more hilly areas as the values are largely between elevations of 100 and 500 ft with only
94 that are at an elevation below 100 ft. A fair number are between 300 and 500 ft (295) and between 500 and 1000 ft (151) but the
majority (832) all fall within 100 and 1000 ft.

## Potential For Future Developments

Initially, a menu system was planned to navigate through the data for the user but could not be implemented completely. Generator
functions could also potentially be added as the list of all 928 entries with station ID, location, and elevation are compiled
but limitations prevent an easy scrolling through the list. A zip function was created for that data to display for the user
and the results appear as so:

![ID:Location:Elevation](https://github.com/ianorourke/dat129_ccac/blob/a61532068c9eaf961622c11b5a499064f0c0a857/api3.png)

Potentially, a generator function of a sort could be used to display the list at smaller increments by user choice but that could not
be completely implemented at this time.

