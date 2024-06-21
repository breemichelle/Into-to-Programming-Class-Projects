#Enter name
print('Brianna Cooper')
#Enter date
print('June 5, 2024')
#Enter class
print('COSC 1336')
#Enter prompt
print('Day 6 Start Up')

#Initial variables
total = 0
largest = 0
smallest = float('inf') #set smallest to float infinity initially

#prompt user for 5 positive integers while updating total, largest, and smallest
print("Enter 5 positive integers:")
num1 = int(input())
if num1 < 0:
    print("Invalid input. Please enter a positive integer.")
else:
    total += num1
    if num1 > largest:
        largest = num1
    if num1 < smallest:
        smallest = num1

num2 = int(input())
if num2 < 0:
    print("Invalid input. Please enter a positive integer.")
else:
    total += num1
    if num2 > largest:
        largest = num2
    if num2 < smallest:
        smallest = num2

num3 = int(input())
if num3 < 0:
    print("Invalid input. Please enter a positive integer.")
else:
    total += num3
    if num3 > largest:
        largest = num3
    if num3 < smallest:
        smallest = num3

num4 = int(input())
if num4 < 0:
    print("Invalid input. Please enter a positive integer.")
else:
    total += num4
    if num4 > largest:
        largest = num4
    if num4 < smallest:
        smallest = num4

num5 = int(input())
if num5 < 0:
    print("Invalid input. Please enter a positive integer.")
else:
    total += num5
    if num5 > largest:
        largest = num5
    if num5 < smallest:
        smallest = num5

#Calculate the average
average = total / 5.0

print("The average is:", average)
print("The largest number entered is:", largest)
print("The smallest number entered is:", smallest)

      
