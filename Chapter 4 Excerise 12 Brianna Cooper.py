#Enter Name
print('Brianna Cooper')
#Enter Date
print('June 5, 2024')
#Enter Class
print('COSC 1336')
#Enter Prompt
print('Chapter 4 Excerise 12')

# Get input from the user
user_input = input("Enter a nonnegative integer: ")

# Ensure the user input is a valid integer
try:
    number = int(user_input)
    if number < 0:
        print("Please enter a nonnegative integer.")
    else:
        factorial = 1
        for i in range(1, number + 1):
            print(f"Multiplying {factorial} by {i}")
            factorial *= i
        print(f"The factorial of {number} is {factorial}.")
except ValueError:
    print("Invalid input. Please enter a valid nonnegative integer.")
