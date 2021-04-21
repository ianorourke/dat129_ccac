# Web-Scraping Assignment

## Root URL
[Goodreads](https://www.goodreads.com/)

## Sources
[Python.org](https://docs.python.org/3/howto/urllib2.html)
[Geeks For Geeks](https://www.geeksforgeeks.org/python-remove-all-digits-from-a-list-of-strings/)


Put simply, for this assignment, this brief program puts together a recommendation list of titles selected from a handful of particular science-fiction writers
using the BeautifulSoup module to help sort through the HTML and return titles in a user-friendly format.

To start, a number of modules were required as recommended from [Python.org](https://docs.python.org/3/howto/urllib2.html):

```
import urllib.request
from bs4 import BeautifulSoup
import requests, re, random

```

From Goodreads, pages from each of the selected authors have been set to variables along with empty lists to contain the titles.

```
b_list = []
l_list = []
d_list = []
...
# Establishing variables for each author.
ballard = 'https://www.goodreads.com/author/list/7010931.J_G_Ballard'
lem = 'https://www.goodreads.com/author/show/10991.Stanis_aw_Lem'
p_k_dick = 'https://www.goodreads.com/author/show/4764.Philip_K_Dick'

```

A function, request_getter, is then called to make the requests to Goodreads and to begin compiling the lists of titles. For
convenience, these are limited to 25 titles.

```
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
```

From there, another function, list_stripper, runs each of the compiled lists to remove the unwanted characters and
produce cleaner results that can display nicely for the user. Rather than make additional functions or import string
to use string.punctuation to check for punctuation, lambda functions have been implemented to conveniently remove 
the unwanted the characters without the need of calling other functions within this function.

```
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
```

Then, another function, title_roulette, draws a random number using random.randint from the lists that is set to
a variable to help draw the random title for the user.

```
def title_roulette(book_list):
    '''Selects a random title from a list'''
    roulette_result = random.randint(0,len(book_list))
    return roulette_result
```

Resulting in:

![Recommended List of Titles](https://github.com/ianorourke/dat129_ccac/blob/main/webscrape2.png)

## Issues for Future Work

Reliably accessing the author search bar from Goodreads proved to be a significant issue as the titles pulled could not
be guaranteed to match exactly. Another issue came with characters with diacritics and letters in other languages, particularly
with letters from non-Latin alphabets. Letters outside the 26 used in English would often result as _ or '', making the results
appear poorly.
