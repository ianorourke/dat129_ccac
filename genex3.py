# -*- coding: utf-8 -*-
"""
Ian O'Rourke
DAT 129 - Python 2 - SP21
Mar 17, 2021
Generators Example
"""


def gener():
    answer_a = print('Alfa.')
    yield answer_a
    
    answer_b = print('Vita.')
    yield answer_b
    
    answer_c = print('Ghama')
    yield answer_c
    
def main():
    a = gener()
    input('What\'s the first letter in the Greek alphabet? ')
    next(a)
    input('What\'s the second letter in the Greek alphabet? ')
    next(a)
    input('What\'s the third letter in the Greek alphabet? ')
    next(a)
    #next(a)


if __name__ == '__main__':
    main()