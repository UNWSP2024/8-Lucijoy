# Author: Lucia Floan
# Date: Mar 21, 2025
# Title: Course Info

# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

courses = {}
amount_courses = int(input('Number of courses: '))

for _ in range(amount_courses):
  id = input('Enter the ID: ').strip()
  name = input('enter the name: ').strip()
  courses[id] = name

subject = input('Enter subject to search for: ').strip()

print(f'\nThecourses with that subject are: ')
for id, name in courses.items():
  if id.startswith(subject):
    print(f'{id}: {name}')
