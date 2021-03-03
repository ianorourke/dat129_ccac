## Icon Making Program
Using a series of prompts for the user to enter ten lines of ten digits of 1 and 0, this program can put those entries 
into a 10 x 10 image that can be inverted, scaled, or reversed.

First, a dictionary is established to store each line that will be used to generate the image.
```
icon_dict = { first_row : first_ten,
                 ...
                 tenth_row : tenth_ten
                 }
```

Then, the user in prompted for each line. A function is in place to ensure that ten digits are entered and that they are 
0s and 1s (and any mistaken entry is treated as 1).
```
first_input = input('Let\'s start with the first row of 10.: ')
    wheeler(first_input,first_ten)
    ...
    tenth_input = input('And now the final ten.: ')
    wheeler(tenth_input,tenth_ten)
```

Once entered, the results were display:
![Example of Generated Icon](/dat129_ccac/icon_example.png)

Then a menu will appear with a list of options in which the generated icon can be adjusted.
```
icon_maker(icon_dict)
    ...
    menu_list = ['See Original','Reverse','Invert','Scale','End Program']
    print('\nAre they any transformations you would like to use?')
    ...
    option_wheel = True
    while option_wheel != False:
        ...
        menu_displayer(menu_list)
        option_input = input('\nPlease select an option. ')
```
These options include 'Reverse' which swaps 0s with 1s and 1s with 0s to produce a negative-like image.
![Example of Reverse Option](/dat129_ccac/reverse_example.png)

'Invert' which inverts the order of entries to show a mirror-like image.
![Example of Invert Option](/dat129_ccac/invert_example.png)

And 'Scale' which can scale the icon from 1-9x.
![Example of Scale Option](/dat129_ccac/scale_example.png)
