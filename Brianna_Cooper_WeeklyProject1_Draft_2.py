# Display Name:
print('Brianna Cooper')
# Date Created:
print('May 31, 2024')
# Date Last Modified:
print('June 2, 2024')
# Class:
print('COSC 1336')
print('Weekly Project 1 Problem')

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Function to convert inches to centimeters
def inches_to_centimeters(inches):
    return inches * 2.54

# Collect data for day 1
print("\nEnter the data for day 1:")
day1 = input("Day of the week: ")
high_temp1 = float(input("High temperature (in degrees Fahrenheit): "))
low_temp1 = float(input("Low temperature (in degrees Fahrenheit): "))
rainfall1 = float(input("Amount of rainfall (in inches): "))

# Collect data for day 2
print("\nEnter the data for day 2:")
day2 = input("Day of the week: ")
high_temp2 = float(input("High temperature (in degrees Fahrenheit): "))
low_temp2 = float(input("Low temperature (in degrees Fahrenheit): "))
rainfall2 = float(input("Amount of rainfall (in inches): "))

# Collect data for day 3
print("\nEnter the data for day 3:")
day3 = input("Day of the week: ")
high_temp3 = float(input("High temperature (in degrees Fahrenheit): "))
low_temp3 = float(input("Low temperature (in degrees Fahrenheit): "))
rainfall3 = float(input("Amount of rainfall (in inches): "))

# Calculate averages and total in Fahrenheit and inches
avg_high_temp_f = (high_temp1 + high_temp2 + high_temp3) / 3
avg_low_temp_f = (low_temp1 + low_temp2 + low_temp3) / 3
total_rainfall_in = rainfall1 + rainfall2 + rainfall3

# Convert temperatures to Celsius
avg_high_temp_c = fahrenheit_to_celsius(avg_high_temp_f)
avg_low_temp_c = fahrenheit_to_celsius(avg_low_temp_f)

# Convert rainfall to centimeters
total_rainfall_cm = inches_to_centimeters(total_rainfall_in)

# Print the results in Fahrenheit and inches
print("\nWeather Summary for the Three-Day Span (in Fahrenheit and inches):")
print("Average High Temperature: {:.2f}°F".format(avg_high_temp_f))
print("Average Low Temperature: {:.2f}°F".format(avg_low_temp_f))
print("Total Rainfall: {:.2f} inches".format(total_rainfall_in))

# Print the results in Celsius and centimeters
print("\nWeather Summary for the Three-Day Span (in Celsius and centimeters):")
print("Average High Temperature: {:.2f}°C".format(avg_high_temp_c))
print("Average Low Temperature: {:.2f}°C".format(avg_low_temp_c))
print("Total Rainfall: {:.2f} cm".format(total_rainfall_cm))
