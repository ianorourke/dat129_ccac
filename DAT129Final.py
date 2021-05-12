# -*- coding: utf-8 -*-
"""
Ian O'Rourke
May 5, 2021
Python 2 - DAT 129 - SP21
Final Project
US National Weather Service API to .csv
"""

# Import modules as needed.
import requests, re, json, csv, statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define functions.
def menu_spinner(menu_list):
    '''Nicely displays a menu for information to access.'''
    counter = 0
    for option in menu_list:
        counter += 1
        print(counter,') ',option,sep='')


def input_scanner(user_input,ref_list):
    '''Readies user input for request by ensuring it as a valid state code.'''
    # Ensures user's input will be set to lowercase to access the list.
    lowered_input = user_input.lower()
    input_wheel = True
    while input_wheel != False:
        if lowered_input not in ref_list:
            new_input = input('Try a valid code. ')
            lowered_input = new_input.lower()
        else:
            input_wheel = False
            # Set result to all caps to properly make the API request.
            final_input = lowered_input.upper()
            return final_input
    
def alert_grabber(state_code):
    '''Makes the API request for alerts with the user-inputted state code.'''
    # Setting up User-Agent per instruction from https://api.weather.gov
    api_requester = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    # Variable set up for API endpoint.
    alert_endpoint = 'https://api.weather.gov/alerts/active/area/' + str(state_code)
    # Variable set for response from API endpoint as well as status_code test
    # to ensure status code 200. Left here for future testing purposes.
    response = requests.get(alert_endpoint)
    #print(response.status_code)
    # JSON-object dictionary generated from successful response.
    json_raw_ore = json.loads(response.text)
    return json_raw_ore

def list_comprehender(dictionary,sub_dict):
    '''Takes a variable holding nested data and makes a list comprehension.'''
    list_comp = [item[sub_dict] for item in dictionary]
    return list_comp

def list_toss(list_comp,empty_list,sub_list):
    '''Makes lists from the values using keys from the list comp dictionary.'''
    for item in list_comp:
        empty_list.append(sub_list)
        
def lambda_mat(list_comp,sub_list):
    '''Lambda function that digs further into a list comp to extract values.'''
    lambda_list = list(map(lambda lambda_list: lambda_list[sub_list], list_comp))
    return lambda_list

def tri_displayer(list_one,list_two,list_three):
    '''Displays nicely for the user three lists.'''
    zip_count = 0
    for(a,b,c) in zip(list_one,list_two,list_three):
        zip_count += 1
        print(zip_count,') ',a,':',b,':',c)

def individ_alerter(user_input,state_list):
    '''Pulls alerts for one state/territory and provides a brief report.'''
    # Verifies input matches a correct code.
    state_pick = input_scanner(user_input,state_list)
    # Sends code with API request.
    indiv_alerts = alert_grabber(state_pick)
    # Digging through the dictionary.
    indiv_specs = indiv_alerts['features']
    # Digging further through the dictionary for the relevant info.
    pot_o_gold = list_comprehender(indiv_specs,'properties')
    # Lists containing the relevant info.
    severities = lambda_mat(pot_o_gold,'severity')
    timedates = lambda_mat(pot_o_gold,'effective')
    headlines = lambda_mat(pot_o_gold,'headline')
    # Displays the alerts.
    tri_displayer(severities,timedates,headlines)

def yes_or_no(user_answer,state_list):
    '''User decides whether or not to pull new weather before analyzing current.'''
    # Ensures input will be lowercase to access the list of state codes.
    new_answer = user_answer.lower()
    wheel = True
    while wheel != False:
        if new_answer == 'y':
            print('\nLet\'s get the current alerts from each state and territory now!')
            print('This may take a moment...')
            weather_gather(state_list)
            wheel = False
            print('Done! A JSON containing current alerts is now available!')
        elif new_answer == 'n':
            wheel = False
            print('\nLet\'s look at the current data then.')
        else:
            new_answer = input('\nInvalid. Try again with \'y\' or \'n\': ')
           
def weather_gather(state_list):
    '''Pulls weather data and places it in as JSON.'''
    # Preparing list for dump into JSON.
    state_data_list = []
    # Loop to run through each state for alert data.
    for state in state_list:
        new_state = state.upper()
        alerter = alert_grabber(new_state)
        alert_specs = alerter['features']
        grab_bag = list_comprehender(alert_specs,'properties')
        state_data_list.append(grab_bag)
    # Writes the completed data from into a JSON. Originally appended
    # but due to issues with the JSON containing multiple objects, a
    # new list is written to file rather than appended as per suggestion
    # during office hours.
    with open('state_weather_data.json','w') as filer:
        json.dump(state_data_list,filer)

def json_opener():
    '''Returns from a json an object that can be analyzed.'''
    with open('state_weather_data.json') as weather:
        weather_data = json.load(weather)
        return weather_data 

def key_refinery(pre_refined,empty_list,particular_key):
    '''Sorts lists from data extracted from the JSON.'''
    for item in pre_refined:
        refined = item[particular_key]
        empty_list.append(refined)   

# Following two functions were created when .readlines() was used to
# attempt to parse through the JSON.
def json_arranger(json_ore,empty_list,sought_str):
    '''Arranges info from the json and sorts them into relevant lists.'''
    for json_metal in json_ore:
        if sought_str in json_metal:
            empty_list.append(json_metal)
            
def list_stripper(old_list,empty_list,extra_bits):
    '''Removes extraneous characters from strings in a list.'''
    for item in old_list:
        new_item = item.replace(extra_bits,'')
        clean_item = new_item.replace('"','')
        empty_list.append(clean_item)
        
def graph_maker(dictionary):
    '''Makes a matplotlib graph from values set in a dictionary.'''
    # Splitting keys and values for graph axes.
    ratings = list(dictionary.keys())
    counts = list(dictionary.values())
    avg_wrath = np.mean(counts)
    fig, ax = plt.subplots()
    ax.barh(ratings,counts)
    labels = ax.get_xticklabels()
    plt.show()
    

def date_counter(date_list):
    '''Arranges a list of dates with counts. Made specifically for alert dates.'''
    # Preparing counts for display.
    four_count = 0
    five_count = 0
    six_count = 0
    seven_count = 0
    eight_count = 0
    nine_count = 0
    ten_count = 0
    elev_count = 0
    twel_count = 0
    other_count = 0
    
    # Currently an arbitrary date range intended for demonstration.
    # Future versions may include drawing from saved datetimes instead.
    for item in date_list:
        if '05-04' in item:
            four_count += 1
        elif '05-05' in item:
            five_count += 1
        elif '05-06' in item:
            six_count += 1
        elif '05-07' in item:
            seven_count += 1
        elif '05-08' in item:
            eight_count += 1
        elif '05-09' in item:
            nine_count += 1
        elif '05-10' in item:
            ten_count += 1
        elif '05-11' in item:
            elev_count += 1
        elif '05-12' in item:
            twel_count += 1
        else:
            other_count += 1
            
    print('May 4:',four_count)
    print('May 5:',five_count)
    print('May 6:',six_count)
    print('May 7:',seven_count)
    print('May 8:',eight_count)
    print('May 9:',nine_count)
    print('May 10:',ten_count)
    print('May 11:',elev_count)
    print('May 12:',twel_count)
    
def type_counter(type_list):
    '''Sorts a list into types. Made specifically for weather severities.'''
    # Preparing counts for the alerts of each severity type.
    min_count = 0
    mod_count = 0
    sev_count = 0
    unk_count = 0
    ex_count = 0
    other_count = 0
    
    for item in type_list:
        if item == 'Minor':
            min_count += 1
        elif item == 'Moderate':
            mod_count += 1
        elif item == 'Severe':
            sev_count += 1
        elif item == 'Extreme':
            ex_count += 1
        elif item == 'Unknown':
            unk_count += 1
        else:
            other_count += 1
    
    # Readying visualization as per:
    # https://matplotlib.org/stable/tutorials/introductory/lifecycle.html
    
    plot_dict = {'Minor':min_count,
                 'Moderate':mod_count,
                 'Severe':sev_count,
                 'Unknown':unk_count,
                 'Extreme':ex_count,
                 'Other':other_count}
    
    # Displays graph of the alert types last pulled.
    graph_maker(plot_dict)
    # Readying counts for potential stats analysis. Longer workarounds used
    # when .describe() and other more convenient functions did not appear to
    # provide any results.
    total_counts = [min_count,mod_count,sev_count,unk_count,ex_count,other_count]
    stats_grabber(total_counts)
    
    
def stats_grabber(data_list):
    '''Used as a workaround if pd.Series() isn't working.'''
    #Doing this the longway since pd.Series() was not working.
    # Assistance from https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
    # https://www.geeksforgeeks.org/python-statistics-stdev/
    #Count
    sev_sum = sum(data_list)
    print('\nSum/Count: ',sev_sum)
    #Mean
    n = len(data_list)
    sev_mean = sev_sum / n
    print('Mean: ',sev_mean)
    #Min
    sev_min = min(data_list)
    print('Min: ',sev_min)
    #Q1
    first_q = np.percentile(data_list,25,interpolation = 'midpoint')
    print('Q1/25%: ',first_q)
    #Median
    print('Median: % s ' % (statistics.median(data_list)))
    #Q3
    third_q = np.percentile(data_list,75,interpolation = 'midpoint')
    print('Q3/75%: ',third_q)
    #Max
    sev_max = max(data_list)
    print('Max: ',sev_max)
    #IQR
    iqr = third_q - first_q
    print('IQR: ',iqr)
    #Standard Deviation
    print('StDev: % s ' % (statistics.stdev(data_list)))
    

# Define main.
def main():
    '''The big to-do.'''
    main_menu = ['See individual weather alerts by state/territory',
                 'Create JSON containing current alerts for the day',
                 'Access currently stored JSON',
                 'Analyze current data',
                 'Save current data to .csv',
                 'End program']
    
    
    # Establishing state and region code lists for ease of access.
    state_codes = ['ak','al','am','an','ar','as','az','ca','co','ct',
                   'dc','de','fl','ga','gm','gu','hi','ia','id','il',
                   'in','ks','ky','la','lc','le','lh','lm','lo','ls',
                   'ma','md','me','mi','mo','mn','ms','nc','nd','ne',
                   'nh','nj','nm','nv','ny','oh','ok','or','pa','ph',
                   'pk','pm','pr','ps','pz','ri','sc','sd','tn','tx',
                   'ut','va','vi','wa','wi','wv','wy']

    
    print('''\nGreetings! This programs allows access to daily alerts as
provided by the API Web Service of the National Weather Service.''')
    print('')
    big_wheel = True
    while big_wheel != False:
        print('\nHere are the current available options:')
        print('')
        menu_spinner(main_menu)
        selection = input('\nEnter your selection here: ')
        if selection == '1':
            user_entry = input('\nEnter the state or territory code to see the current alerts: ')
            checked_entry = input_scanner(user_entry,state_codes)
            individ_alerter(checked_entry,state_codes)
        elif selection == '2':
            print('\nWould you like to access all current active alerts?')
            u_answer = input('\nEnter \'y\' or \'n\': ')
            yes_or_no(u_answer,state_codes)
        elif selection == '3':
            print('\nLet\'s look at the current data we have so far.')
            weather_report = json_opener()
            peeled_report = weather_report[2]
            fresh_sever = []
            fresh_times = []
            fresh_headlines = []
            key_refinery(peeled_report,fresh_sever,'severity')
            key_refinery(peeled_report,fresh_times,'effective')
            key_refinery(peeled_report,fresh_headlines,'headline')
            print('\nCurrent alerts:')
            tri_displayer(fresh_sever,fresh_times,fresh_headlines)
        elif selection == '4':
            print('\nLet\'s get some general information from the current data.')
            print('')
            print('\nLevels of severity:')
            weather_report = json_opener()
            peeled_report = weather_report[2]
            fresh_sever = []
            fresh_times = []
            fresh_headlines = []
            key_refinery(peeled_report,fresh_sever,'severity')
            key_refinery(peeled_report,fresh_times,'effective')
            key_refinery(peeled_report,fresh_headlines,'headline')
            type_counter(fresh_sever)
            print('\nRange of dates: ')
            date_counter(fresh_times)
        elif selection == '5':
            print('\nNow let\'s prepare some of the current data for .csv.')
            weather_report = json_opener()
            peeled_report = weather_report[2]
            areadesc = []
            fresh_sever = []
            fresh_times = []
            fresh_headlines = []
            key_refinery(peeled_report,fresh_times,'effective')
            key_refinery(peeled_report,areadesc,'areaDesc')
            key_refinery(peeled_report,fresh_sever,'severity')
            key_refinery(peeled_report,fresh_headlines,'headline')
            # Preparing data for .csv as per:
            # https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/
            dict_for_csv = {'Alert Date':fresh_times,
                            'Severity':fresh_sever,
                            'Area':areadesc,
                            'Headline':fresh_headlines}
            df = pd.DataFrame(dict_for_csv)
            df.to_csv('current_alerts.csv')
            print('\nSaved to .csv!')
        elif selection == '6':
            print('\nThank you for your interest in this program!')
            big_wheel = False
        else:
            print('\nNot a valid option. Try again.')
    
# Main incantation.
if __name__ == "__main__":
   main()


