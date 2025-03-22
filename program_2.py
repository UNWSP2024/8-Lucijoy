# Author: Lucia Floan
# Date: Mar 21, 2025
# Title: Word Separator

# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = sentence[0].upper()  # Capitalize the first letter of the sentence
    for character in sentence[1:]:
        if character.isupper():
            new_sentence += " " + character.lower()  # Add a space and lowercase the uppercase character
        else:
            new_sentence += character  # Keep the rest of the characters as they are

    return new_sentence


# Input from the user
sentence = input('Enter your sentence with all first characters capitalized and words run together: ')

# Process the sentence
new_sentence = word_separator(sentence)

# Output the result
print(new_sentence)
