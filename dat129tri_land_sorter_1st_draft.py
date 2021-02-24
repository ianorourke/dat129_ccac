# -*- coding: utf-8 -*-
"""
Ian O'Rourke
Created on Mon Feb 22 21:33:50 2021
Python 2 - DAT 129 - SP21
Homework Week 3
Sorter for TRI_Land Data
"""

# Importing necessary modules.
import csv

def menu_wheel(menu_list):
    '''Displays a menu for information to access.'''
    counter = 0
    for option in menu_list:
        counter += 1
        print(counter,') ',option,sep='')
        
# Inquiry question. Which companies have the largest total release amounts
# and of those amounts, what chemicals are involved and what industries are
# these companies of?

def main():
    # Establishing dictionary for summary:
    land_summary = {'inci_count':0,'location':{},'company':{},'year':{},
                'chemical':{},'carcinogen':{},'industry_code':{},'release':{},
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
            if record['ZIP_CODE'] not in land_summary['location']:
                land_summary['location'][record['ZIP_CODE']] = 1
            else:
                land_summary['location'][record['ZIP_CODE']] += 1 
            if record['STANDARDIZED_PARENT_COMPANY'] not in land_summary['company']:
                land_summary['company'][record['STANDARDIZED_PARENT_COMPANY']] = 1
            else:
                land_summary['company'][record['STANDARDIZED_PARENT_COMPANY']] += 1
            if record['PRIMARY_NAICS_CODE'] not in land_summary['industry_code']:
                land_summary['industry_code'][record['PRIMARY_NAICS_CODE']] = 1
            else:
                land_summary['industry_code'][record['PRIMARY_NAICS_CODE']] += 1
            if record['REPORTING_YEAR'] not in land_summary['year']:
                land_summary['year'][record['REPORTING_YEAR']] = 1
            else:
                land_summary['year'][record['REPORTING_YEAR']] += 1
            if record['CHEM_NAME'] not in land_summary['chemical']:
                land_summary['chemical'][record['CHEM_NAME']] = 1
            else:
                land_summary['chemical'][record['CHEM_NAME']] += 1
            if record['CARCINOGEN'] not in land_summary['carcinogen']:
                land_summary['carcinogen'][record['CARCINOGEN']] = 1
            else:
                land_summary['carcinogen'][record['CARCINOGEN']] += 1
            if record['TOTAL_RELEASE'] not in land_summary['release']:
                land_summary['release'][record['TOTAL_RELEASE']] = 1
            else:
                land_summary['release'][record['TOTAL_RELEASE']] += 1

    # Setting up the main menu.
    main_menu = ['View compilation of companies listed.','List of chemicals reported.',
                 'Range of reporting years','List of industries per NAICS code.','End program.']
    
    # Getting the wheel going so the menu will cycle through options until
    # prompted otherwise.
    option_go = True
    while option_go != False:
        print('')
        # Displaying menu.
        menu_wheel(main_menu)
        # Getting input from user for options.
        user_input = input('\nPlease select an option: ')
        # Option to list alphabetically the companies reported/reporting.
        if user_input == '1':
            print('\nCompanies listed: \n')
            comp_count = 0
            for comp in sorted(land_summary['company']):
                comp_count += 1
                print(comp_count,') ',comp,sep='')
        # Option compiling alphabetically the log of chemicals reported.
        elif user_input == '2':
            print('\nChemicals reported: \n')
            chem_count = 0        
            for chem in sorted(land_summary['chemical']):
                chem_count += 1
                print(chem_count,') ',chem,sep='')
        # Option to see the range from earliest reporting year to most recent.
        elif user_input == '3':
            print('\nRange of reporting years: \n')
            print('From',min(land_summary['year']),'to',max(land_summary['year']),sep='')
        # Listing the industry codes in order per NAICS. Currently without reference
        # so this will only be useful to thsoe already familiar with the code.
        elif user_input == '4':
            print('\nIndustry codes per NAICS: \n')
            ind_count = 0
            for ind in sorted(land_summary['industry_code']):
                ind_count += 1
                print(ind_count,') ',ind,sep='')
        # Ends the program.
        elif user_input == '5':
            option_go = False
            print('\nAll done!\n')
        # In event of invalid option.
        else:
            print('\nNot a valid option. Try again.\n')

            
if __name__ == "__main__":
   main()