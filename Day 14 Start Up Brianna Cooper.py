#Name
print('Brianna Cooper')
#Date
print('June 20, 2024')
#Class
print('COSC 1336')
#Solving for
print('Day 14 Start Up Problem')

# This program collects a person's first name, last name, age, height in inches, and weight in pounds.
# It stores these values in a list and prints out the age and the last name.

# Initialize an empty list to store the person's details
person_details = []

# Collecting all the required info from the user and appending it to the list
first_name = input("Enter your first name: ")
person_details.append(first_name)

last_name = input("Enter your last name: ")
person_details.append(last_name)

age = input("Enter your age: ")
person_details.append(age)

height_in_inches = input("Enter your height in inches: ")
person_details.append(height_in_inches)

weight_in_pounds = input("Enter your weight in pounds: ")
person_details.append(weight_in_pounds)

# Printing out the age and the last name
print("Age:", person_details[2])  # age is the third element in the list
print("Last Name:", person_details[1])  # last name is the second element in the list

