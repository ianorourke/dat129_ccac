# -*- coding: utf-8 -*-
"""
Ian O'Rourke
Apr 13, 2021
Python 2 - DAT 129 - SP21
Web-scraping Assignment
Recommendations List From Goodreads.com
"""

# Per https://docs.python.org/3/howto/urllib2.html:
import urllib.request
import re
from bs4 import BeautifulSoup
import requests

the_list = []

piece_parse = 100
for piece in range(1,25):
    piece_parse += 1
    requester = requests.get('https://www.goodreads.com/author/list/7010931.J_G_Ballard')
    starting_soup = BeautifulSoup(requester.text,'html.parser')
    #print(starting_soup)
    spanner = starting_soup.find_all('a', class_="bookTitle")
    #print(spanner)
    for a in spanner:
        a_collect = {}
        #print(a['href'])
        a_collect['book'] = a['href']
        if a_collect['book'] not in the_list:
            the_list.append(a_collect['book'])
            
print(the_list)
        
        
        

#def url_draw(htmlpiece):
#    return 'https://www.python.org/search/?q=generators&submit=' % (htmlpiece,)