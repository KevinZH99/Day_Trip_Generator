

destination_options = ['Denver', 'Dallas', 'Tampa']
restaurant_options = ['Olive Garden', 'Texas Roadhouse', 'Yard House']
transportation_options = ['Bus', 'Rental Car', 'Uber']
entertainment_options = ['Comedy Club', 'Concert', 'Football Game']

import random

random_destination = random.choice(destination_options)
print(random_destination)
random_restaurant = random.choice(restaurant_options)
print(random_restaurant)
random_transportation = random.choice(transportation_options)
print(random_transportation)
random_entertainment = random.choice(entertainment_options)
print(random_entertainment)

ask_user = input("Does your day trip look complete? Yes or No?: ").upper()
if ask_user.upper() == 'YES':
    print(f'Awesome! City: {random_destination}. Restaurant: {random_restaurant}. Transportation: {random_transportation}. Entertainemnt: {random_entertainment}.')
else:
    print
    change_options: input('What options do you want to change?: ')
    if change_options == (f'{random_entertainment}'):
        print('awesome')
