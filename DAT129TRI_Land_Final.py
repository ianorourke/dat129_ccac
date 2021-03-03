# -*- coding: utf-8 -*-
"""
Ian O'Rourke
Created on Mon Feb 22 21:33:50 2021
Python 2 - DAT 129 - SP21
Homework Week 3
Sorter for TRI_Land Data
"""

# Inquiry question. Which companies have the largest amount of incidents and
# which chemicals are the most reported? What years have had the most incidents
# and of what subsectors are these most likely associated with?

# Importing necessary modules.
import csv

# Defining functions.
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

def main():
    # Establishing dictionary for summary:
    land_summary = {'inci_count':0,'location':{},'company':{},'year':{},
                'chemical':{},'carcinogen':{},'industry_code':{},'ind_three':{},
                'release':{},
                }

    # Accessing TRI_Land as per in-class example. TRI_Land data set taken from website:
    # https://data.wprdc.org/dataset/toxic-release-inventory/resource/1809697b-86ed-4ce2-b813-179b95d6c833
    with open('tri_land.csv') as trifler:
        data_reader = csv.DictReader(trifler)
        # List made up from the field names for easy access.
        land_fields = list(data_reader.fieldnames)
        # Filling the land_summary dictionary with entries from the data set.
        for record in data_reader:
            # Drawing data and setting data with the land_summary dictionary.
            land_summary['inci_count'] = land_summary['inci_count'] + 1
            if record['ZIP_CODE'][0:5] not in land_summary['location']:
                land_summary['location'][record['ZIP_CODE'][0:5]] = 1
            else:
                land_summary['location'][record['ZIP_CODE'][0:5]] += 1 
            if record['STANDARDIZED_PARENT_COMPANY'] not in land_summary['company']:
                land_summary['company'][record['STANDARDIZED_PARENT_COMPANY']] = 1
            else:
                land_summary['company'][record['STANDARDIZED_PARENT_COMPANY']] += 1
            if record['PRIMARY_NAICS_CODE'] not in land_summary['industry_code']:
                land_summary['industry_code'][record['PRIMARY_NAICS_CODE']] = 1
            else:
                land_summary['industry_code'][record['PRIMARY_NAICS_CODE']] += 1
            if record['PRIMARY_NAICS_CODE'][0:3] not in land_summary['ind_three']:
                land_summary['ind_three'][record['PRIMARY_NAICS_CODE'][0:3]] = 1
            else:
                land_summary['ind_three'][record['PRIMARY_NAICS_CODE'][0:3]] += 1
            if record['REPORTING_YEAR'] not in land_summary['year']:
                land_summary['year'][record['REPORTING_YEAR']] = 1
            else:
                land_summary['year'][record['REPORTING_YEAR']] += 1
            if record['CHEM_NAME'] not in land_summary['chemical']:
                land_summary['chemical'][record['CHEM_NAME']] = 1
            else:
                land_summary['chemical'][record['CHEM_NAME']] += 1
            
    # Setting up the main menu.
    main_menu = ['Company list with incident numbers.','List of chemicals reported.',
                 'Range of reporting years with incident counts',
                 'List of incidents by individual subsectors per NAICS.',
                 'List of incidents by general subsector per NAICS.',
                 'Location by ZIP Code with incident numbers.',
                 'End program.']
    
    # Getting the wheel going so the menu will cycle through options until
    # prompted otherwise.
    option_go = True
    while option_go != False:
        print('')
        # Displaying menu.
        menu_wheel(main_menu)
        # Getting input from user for options.
        user_input = input('\nPlease select an option: ')
        # Option to list the companies with number of incidents.
        if user_input == '1':
            print('\nCompanies listed : Incident Reports\n')
            sorter(land_summary,'company')
        # Option to list the log of chemicals with number of reports.
        elif user_input == '2':
            print('\nChemicals reported : Incident counts\n')
            sorter(land_summary,'chemical')
        # Option to see the range from earliest reporting year to most recent.
        elif user_input == '3':
            print('\nRange of reporting years: \n')
            print('From ',min(land_summary['year']),' to ',max(land_summary['year']),'.',sep='')
            print('\nReported year : Number of incident counts\n')
            sorter(land_summary,'year')
        # Option to list the full individual industry subsector codes in order per NAICS.
        # The codes can be referenced at: https://www.census.gov/naics/
        elif user_input == '4':
            print('\nSubsector : Incident Reports\n')
            sorter(land_summary,'industry_code')
        # Option to list by general industry subsector codes in order per NAICS.
        elif user_input == '5':
            print('\nSubsector : Incident Reports\n')
            sorter(land_summary,'ind_three')
        # Option to list zip codes with associated incident reports.
        elif user_input == '6':
            print('\nLocation by ZIP code : Incident Reports')
            sorter(land_summary,'location')
        # Ends the program.
        elif user_input == '7':
            option_go = False
            print('\nAll done!\n')
        # In event of invalid option.
        else:
            print('\nNot a valid option. Try again.\n')

            
if __name__ == "__main__":
   main()