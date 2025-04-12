pet = {
    'name': None,
    'species': None,
    'age': 0,
    'health': 100,
    'happiness': 100,
    'is_alive': True
}


pet['species'] = input('Welcome to the pet shop. What species of pet would you like? ')
print(pet)

pet['name'] = input('What would you like to name your pet? ')
print(pet)


while pet['is_alive'] == True:
    print(pet)
    # fake code, we need actual time logic for this to work
    # if time_passed == '30 seconds':
    #     pet['age'] += 1
    # if time_passed == '5 seconds':
    #     pet['health'] -= 5
    #     pet['happiness'] -= 5

    if pet['age'] > 100:
        pet['is_alive'] = False
        break

    action = input('What would you like to do this turn? 1. Feed the pet 2. Punch the pet 3. Do nothing')

    if action == 'Feed':
        pet['happiness'] += 10
        pet['health'] += 5
    
    if action == 'Punch':
        pet['happiness'] -= 10
        pet['health'] -= 10
    
    if action == 'Do nothing':
        pet['happiness'] -= 2
        pet['health'] -= 0.5
    
    if pet['health'] <= 0:
        pet['is_alive'] = False
    
    if pet['is_alive'] == False:
        print('Your pet has died, game over!')
        break
