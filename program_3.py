# Author: Lucia Floan
# Date: Mar 21, 2025
# Title: Capital Quiz

# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random

states = {
    "Florida": "Tallahassee",
    "Hawaii": "Honolulu",
    "Texas": "Austin",
    "New Jersey": "Trenton",
    "South Carolina": "Columbia",
    "Michigan": "Lansing",
    "Ohio": "Columbus",
    "Colorado": "Denver",
    "Illinois": "Springfield",
    "Georgia": "Atlanta",
    "Nevada": "Carson City",
    "Kansas": "Topeka",
    "Tennessee": "Nashville",
    "California": "Sacramento",
    "Utah": "Salt Lake City",
    "Indiana": "Indianapolis",
    "Louisiana": "Baton Rouge",
    "Rhode Island": "Providence",
    "Alabama": "Montgomery",
    "North Carolina": "Raleigh",
    "Wyoming": "Cheyenne",
    "Oregon": "Salem",
    "Kentucky": "Frankfort",
    "Alaska": "Juneau",
    "South Dakota": "Pierre",
    "New York": "Albany",
    "West Virginia": "Charleston",
    "Arizona": "Phoenix",
    "New Mexico": "Santa Fe",
    "North Dakota": "Bismarck",
    "Montana": "Helena",
    "Washington": "Olympia",
    "Maryland": "Annapolis",
    "Mississippi": "Jackson",
    "Vermont": "Montpelier",
    "Iowa": "Des Moines",
    "Delaware": "Dover",
    "Missouri": "Jefferson City",
    "Minnesota": "Saint Paul",
    "Maine": "Augusta",
    "Arkansas": "Little Rock",
    "Connecticut": "Hartford",
    "Wisconsin": "Madison",
    "Idaho": "Boise",
    "Pennsylvania": "Harrisburg",
    "Virginia": "Richmond",
    "Nebraska": "Lincoln",
    "Montana": "Helena",
    "Wyoming": "Cheyenne",
    "Oklahoma": "Oklahoma City",
    "California": "Sacramento",
    "Massachusetts": "Boston",
    "New Hampshire": "Concord",
    "Kentucky": "Frankfort"
}

correct = 0
wrong = 0

shuffled_states = list(states.keys())
random.shuffle(shuffled_states)

for state in shuffled_states[:5]:
 answer = input(f'what is the capital of {state}? ').strip()
 if answer.lower() == states[state].lower():
   print ('correct')
   correct += 1
 else:
   print ('wrong')
   wrong += 1

print('quiz complete!')
print(f'number correct: {correct}')
print(f'number wrong: {wrong}')




