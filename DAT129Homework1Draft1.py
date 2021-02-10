# -*- coding: utf-8 -*-
"""
Ian O'Rourke
Created on Sun Feb  7 17:57:23 2021
Python 2 - DAT 129 - SP21
Homework Week 1
Icon Creator
"""

def wheeler(ten_set,this_list):
    '''Ensure the user inputs 10 characters.'''
    # Setting up while loop so the user can be prompted again if more
    # or less than 10 characters are provided for the input prompts in
    # main().
    wheel = True
    while wheel != False:
        if len(ten_set) != 10:
            print('Try again.')
            ten_set = input('Enter ten.: ')
        else:
            this_list.append(ten_set)
            wheel = False
            return('Onto the next one!')


def main():
    # Greeting and instructing the user.
    print('''Welcome! Using just a simply entry of 0s and 1s, this program
will generate a 10 x 10 image that can serve as an icon for you.
Simply type a sequence using only 0 and 1 (anything else will count as a 1) 
for each row until all 10 are complete! Let's begin!''')
    
    # Establishing keys and values for primary dictionary.
    first_row = 'Row 1'
    second_row = 'Row 2'
    third_row = 'Row 3'
    fourth_row = 'Row 4'
    fifth_row = 'Row 5'
    sixth_row = 'Row 6'
    seventh_row = 'Row 7'
    eighth_row = 'Row 8'
    ninth_row = 'Row 9'
    tenth_row = 'Row 10'
    
    first_ten = []
    second_ten = []
    third_ten = []
    fourth_ten = []
    fifth_ten = []
    sixth_ten = []
    seventh_ten = []
    eighth_ten = []
    ninth_ten = []
    tenth_ten = []
    
    icon_dict = { first_row : first_ten,
                 second_row : second_ten,
                 third_row : third_ten,
                 fourth_row: fourth_ten,
                 fifth_row : fifth_ten,
                 sixth_row : sixth_ten,
                 seventh_row : seventh_ten,
                 eighth_row : eighth_ten,
                 ninth_row : ninth_ten,
                 tenth_row : tenth_ten
                 }
    
    # Collecting 100 0s and 1s from the user. Divided into 10 input
    # commands to help make it convenient for the user to enter all 100.
    first_input = input('Let\'s start with the first row of 10.: ')
    wheeler(first_input,first_ten)
    second_input = input('Now let\'s do the second.: ')
    wheeler(second_input,second_ten)
    third_input = input('And the now the third: ')
    wheeler(third_input,third_ten)
    fourth_input = input('And the fourth.: ')
    wheeler(fourth_input,fourth_ten)
    fifth_input = input('Now the fifth.: ')
    wheeler(fifth_input,fifth_ten)
    sixth_input = input('And the sixth.: ')
    wheeler(sixth_input,sixth_ten)
    seventh_input = input('The seventh: ')
    wheeler(seventh_input,seventh_ten)
    eighth_input = input('The eighth.: ')
    wheeler(eighth_input,eighth_ten)
    ninth_input = input('Now the ninth.: ')
    wheeler(ninth_input,ninth_ten)
    tenth_input = input('And now the final ten.: ')
    wheeler(tenth_input,tenth_ten)
    
    # Letting the user know that the input is complete.
    print('Let\'s see what we\'ve got!')
    print('')
    
    # Replaces the 0s with blank spaces and the 1s with Xs to display
    # the icon made from the inputted characters. Currently part of
    # main() due to trouble getting this to work through a function.
    for key in icon_dict:
        for item in icon_dict[key]:
            for digit in item:
               if '0' in digit:
                    item = item.replace(digit,' ')
               else:
                    item = item.replace(digit,'X')
        print(item)
    

if __name__ == "__main__":
    main()

