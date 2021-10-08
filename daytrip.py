import random


destination_options = ['Denver', 'Dallas', 'Tampa']
restaurant_options = ['Olive Garden', 'Texas Roadhouse', 'Yard House']
transportation_options = ['Bus', 'Rental Car', 'Uber']
entertainment_options = ['Comedy Club', 'Concert', 'Football Game']


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
while ask_user.upper() == "NO":
    print ('Press 1 to change destination. Press 2 to change restaurant. Press 3 to change transportation. Press 4 to change entertainment.')
    change_options = input('What options do you want to change?: ')
    if change_options == '1':
        random_destination = random.choice(destination_options)
        print(f'{random_destination}')
    elif change_options == '2':
        random_restaurant = random.choice(restaurant_options)
        print(f'{random_restaurant}')
    elif change_options == '3': 
        random_transportation = random.choice(transportation_options)
        print(f'{random_transportation}')
    elif change_options == '4':
        random_entertainment = random.choice(entertainment_options)
        print(f'{random_entertainment}')
    ask_user = input("Does your day trip look complete? Yes or No?: ").upper()
    if ask_user.upper() == "YES":
        print(f'Awesome! City: {random_destination}. Restaurant: {random_restaurant}. Transportation: {random_transportation}. Entertainemnt: {random_entertainment}.')
        quit()
