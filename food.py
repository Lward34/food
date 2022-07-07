"""
AFTER
Summary: This script will ask the user for their name and favorite food then print it. 
Author: Sharif A. Rahman
Date: February 1, 2021
"""

validname = False
validfood = False

while not validname:
    name = input('Good day , shall we start by you giving me your name? : ')
    if name.isalpha() and len(name) >= 2:
        validname = True
    else:
        print("\nWhat you entered isn't a real name\n")
while not validfood:
    fav_food = input(f'\nHello {name}, it\'s nice to meet you. \n'
f'Since we\'re getting to know each other, \n'
f'how bout you tell me your favorite food: ')
    if fav_food.isalpha() and len(fav_food) >= 2:
       validfood = True
       print(f'\nMhhhmm..... {fav_food}!, that sounds amazing right about now!! \n'
f'Got any {fav_food} on you?  I\'m starving!!')
    else:
        print("\nWhat you entered isn't a real food\n")