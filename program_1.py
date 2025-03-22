# Author: Lucia Floan
# Date: Mar 21, 2025
# Title: Initials

# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

def initials_generator(personsName):

    personsInitials = ""
    part_of_name = personsName.split()
    for part in part_of_name:
        personsInitials += part[0].upper() + "."
        personsInitials.strip()

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name')

initials = initials_generator(personsName)

print(initials)
