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
        
def menu_displayer(ready_menu):
    '''Displays a list as a menu for the user for potential options.'''
    counter = 0
    for entry in ready_menu:
        counter = counter + 1
        print(counter,') ',entry,sep='')
        
def icon_maker(dictionary):
    '''Makes an icon switches 0s to spaces and 1s to Xs.'''
    for key in dictionary:
        for item in dictionary[key]:
            for digit in item:
               if '0' in digit:
                    item = item.replace(digit,' ')
               else:
                    item = item.replace(digit,'X')
        print(item)
        
def icon_negative(dictionary):
    '''Swaps 0s for Xs and 1s for spaces.'''
    for key in dictionary:
        for item in dictionary[key]:
            for digit in item:
               if '0' in digit:
                    item = item.replace(digit,'X')
               else:
                    item = item.replace(digit,' ')
        print(item)

def inverter(dictionary):
    '''Makes the icon from the end of the given inputs.'''
    for key in dictionary:
        for item in dictionary[key]:
            for digit in item:
               if '0' in digit:
                    item = item.replace(digit,' ')
               else:
                    item = item.replace(digit,'X')
        print(item[::-1])
        
def scale_check(scale_input):
    '''Ensures user input is within 1-9.'''
    while int(scale_input) > 0 and int(scale_input) < 9:
                if scale_input > 0 and scale_input < 9:
                    ready_input = scale_input
                    return ready_input
                else:
                    int(input('\nInvalid option. Try again. Pick a number between 1-9.'))
    
        
def scaler(dictionary,scale):
    '''Scales the icon by 1-9x depending on user selection011.'''
    for key in dictionary:
        for vert in range(0,scale):
            for item in dictionary[key]:
                for digit in item:
                    if '0' in digit:
                        item = item.replace(digit,' ' * scale)
                    else:
                        item = item.replace(digit,'X' * scale)
            print(item)

def main():
    # Greeting and instructing the user.
    print('''Welcome! Using just a simply entry of 0s and 1s, this program
will generate a 10 x 10 image that can serve as an icon for you.
Simply type a sequence using 0 and 1 (if anything else is typed, it will 
count as a 1) for each row until all 10 are complete! Let's begin!''')
    
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
    print('\nLet\'s see what we\'ve got!')
    print('')
    # Showing the results.
    icon_maker(icon_dict)
    # Setting up the menu for the user to make transformations.
    menu_list = ['See Original','Reverse','Invert','Scale','End Program']
    print('\nAre they any transformations you would like to use?')
    print('')
    # Getting the menu to run.
    option_wheel = True
    while option_wheel != False:
        # Displaying the menu.
        menu_displayer(menu_list)
        option_input = input('\nPlease select an option. ')
        # Option for viewing the original creation.
        if option_input == '1':
            print('\nHere\'s the original icon.')
            icon_maker(icon_dict)
            print('\nAny other transformations you would like to see?')
            print('')
        # Option for viewing the icon reversed like a negative.
        elif option_input == '2':
            print('\nLet\'s how this looks reversed!')
            icon_negative(icon_dict)
            print('\nAny other transformations you would like to see?')
            print('')
        # Option for viewing the icon inverted.
        elif option_input == '3':
            print('\nLet\'s see how this looks inverted!')
            inverter(icon_dict)
            print('\nAny other transformations you would like to see?')
            print('')
        # Option for viewing the icon scaled.
        elif option_input == '4':
            print('\nHow much would you like this icon scaled?')
            user_scale = int(input('\nSelect a number between 1-9. '))
            clean_scale = scale_check(user_scale)
            print('\nNow let\'s see how this looks scaled at',user_scale,'x!')
            print('')
            scaler(icon_dict,clean_scale)
            print('\nAny other transformations you would like to see?')
            print('')
        # Ends the program.
        elif option_input == '5':
            print('\nAll right! Thanks for using this program!')
            option_wheel = False
        # For all other options that are not 1-6.
        else:
            print('\nNot a valid option. Try again.')
            print('')
    

if __name__ == "__main__":
    main()

