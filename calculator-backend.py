import requests
headers = {"Authorization": "Bearer keywAt8RcXG9dAxFG"}
url = "https://api.airtable.com/v0/app5QUe3opWl9lRLa/Table%201"

#FUNCTIONS
#categorises your stats to see which plants you can keep
def lightcategory(parvalue):
    if parvalue < 30:
        return 'low'
    elif parvalue < 50:
        return 'mid'
    else:
        return 'high'

#the higher the light, the more plants are output
def outputplants(lightreq):
    if lightreq == 'low':
        url = "https://api.airtable.com/v0/apppNh9VpaH1N9fET/Tasks?fields%5B%5D=Plant&filterByFormula=%7Blightrequirement%7D+%3D+1"
    elif lightreq == 'mid':
        url = "https://api.airtable.com/v0/apppNh9VpaH1N9fET/Tasks?fields%5B%5D=Plant&filterByFormula=%7Blightrequirement%7D+%3C%3D+2"
    elif lightreq == 'high':
        url = "https://api.airtable.com/v0/apppNh9VpaH1N9fET/Tasks?fields%5B%5D=Plant&filterByFormula=%7Blightrequirement%7D+%3C%3D+3"
    else:
        print('Error')
    plants = requests.get(url, headers=headers).json()['records']
    for plant in plants:
        name = plant['fields']['Plant']
        print(name)

        

lights = requests.get(url, headers=headers).json()['records']
print('Available lights are: ')
for light in lights:
    print(light['fields']['Name'])
lightinput = input('\nEnter light model: ')
height = int(input('Enter aquarium height in inches: '))
#finds light that matches name
global par
for light in lights:
    if light['fields']['Name'] == lightinput:
        #different heights
        if height == 9:
            par = int((light['fields']['9"']))
        elif height == 12:
            par = int((light['fields']['12"']))
        elif height == 15:
            par = int((light['fields']['15"']))
        elif height == 18:
            par = int((light['fields']['18"']))
        elif height == 21:
            par = int((light['fields']['21"']))
        elif height == 24:
            par = int((light['fields']['24"']))
        else:
            print('Height unsupported')

print('Based on light model and height, your light category is', lightcategory(par))
print('\nYou can keep the following plants: ')
#plugs in output of lightcategory function and shows low/mid/high light plants
outputplants(lightcategory(par))
