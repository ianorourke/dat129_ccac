# Inquiry of Toxic Releases on Land in Allegheny County, PA

## Sources
[TRI-Land Data](https://data.wprdc.org/dataset/toxic-release-inventory/resource/1809697b-86ed-4ce2-b813-179b95d6c833)
[NAICS](https://www.census.gov/naics/)
[NAICS Reference Manual](https://www.census.gov/naics/reference_files_tools/2017_NAICS_Manual.pdf)

## Inquiry Question
Per the data provided by TRI-Land, what companies appear to have the most reported incidents of toxic releases
in Allegheny County, PA and what chemicals are most reported? What industries are most reported as well?

To answer the question about which companies report the most incidents, of what chemicals, and of what industries.

Per in-class example (2-17-2021), the .csv file of the TRI-Land data (taken as of 2-22-2021) is read through a
data reader that pulls the data from the desired fields and places them in a dictionary. For ZIP Codes and NAICS
Industry codes, a limit is set to ensure that another dictionary will list the ZIP codes by 5 digits and two additional
dictionaries will hold the full NAICS code and the three digit code that refers to general subsector:
```
land_summary = {'inci_count':0,'location':{},'company':{},'year':{},
                'chemical':{},'industry_code':{},'ind_three':{},
                }
...
with open('tri_land.csv') as trifler:
        data_reader = csv.DictReader(trifler)
        ...
        land_fields = list(data_reader.fieldnames)
        ...
        for record in data_reader:
            ...
            land_summary['inci_count'] = land_summary['inci_count'] + 1
            if record['ZIP_CODE'][0:5] not in land_summary['location']:
                land_summary['location'][record['ZIP_CODE'][0:5]] = 1
            else:
                land_summary['location'][record['ZIP_CODE'][0:5]] += 1
            ...
```
Then functions are set to organize the data and provide the menu to access the data conveniently.
```
def menu_wheel(menu_list):
    '''Displays a menu for information to access.'''
    counter = 0
    for option in menu_list:
        counter += 1
        print(counter,') ',option,sep='')
        
def sorter(dictionary,sub_dict):
    '''Sorts a sub-dictionary from the main dictionary per user option.'''
    count = 0
    for report in sorted(dictionary[sub_dict]):
        count += 1
        print(count,') ',report,' : ',dictionary[sub_dict][report],sep='')
```
This provides the following menu of options:
!(https://user-images.githubusercontent.com/78517588/109880831-67250880-7c45-11eb-81ff-383cec65b132.png)

In response to the initial inquiry question, the results from the .csv appear as follows:

!(https://user-images.githubusercontent.com/78517588/109881168-d00c8080-7c45-11eb-9b32-e6292f024bd0.png)

US STEEL CORP appears to have the highest amount of recorded incidents at 8315.

!(https://user-images.githubusercontent.com/78517588/109881311-14981c00-7c46-11eb-8563-890219c6b209.png)

TOULENE and XYLENE appear to be the chemicals most reported at 3452 and 3804 incidents respectively.
However, it may be worth nothing that LEAD and LEAD COMPOUNDS, while smaller individually, do add to more than 4800.

!(https://user-images.githubusercontent.com/78517588/109881521-6fca0e80-7c46-11eb-84c9-bbe261e7f430.png)

Looking at industries per NAICS code:

!(https://user-images.githubusercontent.com/78517588/109881638-a2740700-7c46-11eb-9b9b-1c262d228cdd.png)

The largest appears to be industry code 325510 at 10226 incidents.
![Per the NAICS manual as of 2017,](https://www.census.gov/naics/reference_files_tools/2017_NAICS_Manual.pdf)
this would be Chemical Manufacturing : Paint and Coating Manufacturing.

Looking at general subsectors though:

!(https://user-images.githubusercontent.com/78517588/109882043-3cd44a80-7c47-11eb-805b-0c4e8630c076.png)

Subsectors 325 and 331 appear to be the highest which, ![per the NAICS manual as of 2017,](https://www.census.gov/naics/reference_files_tools/2017_NAICS_Manual.pdf)
refers to the subsectors of Chemical Manufacturing and Primary Metal Manufacturing respectively.






