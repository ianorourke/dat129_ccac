# -*- coding: utf-8 -*-
"""
Ian O'Rourke
Apr 13, 2021
Python 2 - DAT 129 - SP21
Web-scraping Assignment
Recommendations List From Goodreads.com
"""

# Importing modules as needed per https://docs.python.org/3/howto/urllib2.html:

import urllib.request
from bs4 import BeautifulSoup
import requests, re, random

# Defining functions.

def request_getter(author,author_list):
    '''Makes the request to Goodreads for an author's titles.'''
    # Setting a counter/limit of how much will be pulled from the search results.
    piece_parse = 100
    for piece in range(1,25):
        piece_parse += 1
        # Making request and sorting via BeautifulSoup as per in-class exercises.
        requester = requests.get(author)
        author_soup = BeautifulSoup(requester.text,'html.parser')
        # Pulling specific titles from the HTML code.
        title_soup = author_soup.find_all('a', class_="bookTitle")
        for title in title_soup:
            title_collect = {}
            title_collect['book'] = title['href']
            if title_collect['book'] not in author_list:
                author_list.append(title_collect['book'])
                
def list_stripper(messy_list):
    '''Strips unwanted characters from a list.'''
    # Setting up empty list for first cleaning of entries.
    stripped_list = []
    for title in messy_list:
        nu_title = title.replace('/book/show/','')
        stripped_list.append(nu_title)
    # Stripped numbers from the list entries via lambda function
    # as provided by https://www.geeksforgeeks.org/python-remove-all-digits-from-a-list-of-strings/
    num_list = '[0-9]'
    no_num_list = [re.sub(num_list,'',i) for i in stripped_list]
    # Taking same principle to remove unwanted punctuation.
    unwanted_punct = '[-._]'
    clean_list = [re.sub(unwanted_punct,' ',i) for i in no_num_list]
    # Setting up second empty list for next wave of cleaning for entries.
    cleaner_list = []
    for item in clean_list:
        if item[0] == ' ':
            new_item = item.strip(' ')
            cleaner_list.append(new_item)
        else:
            cleaner_list.append(item)
    return cleaner_list
                
def title_roulette(book_list):
    '''Selects a random title from a list'''
    roulette_result = random.randint(0,len(book_list))
    return roulette_result

# Defining main():

def main():
    '''Pulling together the recommendations.'''
    # Greeting the user.
    print('''\nWelcome! Let\'s go to Goodreads and pull some titles from the
stranger (and arguably more interesting) parts of science fiction.''')
    
    # Setting up empty lists for each author.
    b_list = []
    l_list = []
    d_list = []
    #r_list = []
    #t_list = []
    #p_list = []
    
    # Establishing variables for each author.    
    ballard = 'https://www.goodreads.com/author/list/7010931.J_G_Ballard'
    lem = 'https://www.goodreads.com/author/show/10991.Stanis_aw_Lem'
    p_k_dick = 'https://www.goodreads.com/author/show/4764.Philip_K_Dick'
    
    # Other potential authors though an issue on how to bring in characters with
    # diacritics and non-Latin letters still needs to be resolved in order for
    # the titles to display nicely for the user.
    #delany = 'https://www.goodreads.com/author/show/49111.Samuel_R_Delany'
    #tokarczuk = 'https://www.goodreads.com/author/show/296560.Olga_Tokarczuk'
    #pelevin = 'https://www.goodreads.com/author/show/4594585.Victor_Pelevin'

    # Making the requests and filling the empty lists with titles.
    request_getter(ballard,b_list)
    request_getter(lem,l_list)
    request_getter(p_k_dick,d_list)
    #request_getter(delany,r_list)
    #request_getter(tokarczuk,t_list)
    #request_getter(pelevin,p_list)
    
    # Cleaning up the list of titles.
    b_list = list_stripper(b_list)
    l_list = list_stripper(l_list)
    d_list = list_stripper(d_list)
    
    # Drawing random titles from each of the lists.
    random_b = title_roulette(b_list)
    random_l = title_roulette(l_list)
    random_d = title_roulette(d_list)
    print('\nAnd the recommended titles are:\n')
    # Print the resulting titles.
    print('J.G. Ballard: '+ b_list[random_b].title())
    print('Philip K. Dick: '+ d_list[random_d].title())
    print('Stanislaw Lem: '+ l_list[random_l].title())
    
    
# Main incantation.
if __name__ == "__main__":
   main()