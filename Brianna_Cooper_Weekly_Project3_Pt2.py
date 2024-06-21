#Name
print('Brianna Cooper')
#Date
print('June 13, 2024')
#Class
print('COSC 1336')
#Solving for
print('Weekly Project 3 Part 2')

#Dice Rolling Program

#This program simulates rolling a 6-sided die 12 times and calculates various statistics based on the rolls.

import math
import random

# Function to roll the dice 12 times and return the statistics directly
def roll_dice():
    min_roll = float('inf')  # Initializing the minimum roll as positive infinity
    max_roll = float('-inf')  # Initializing the maximum roll as negative infinity
    sum_rolls = 0  # Initializing the sum of rolls
    for _ in range(12):  # Rolling the dice 12 times
        roll = random.randint(1, 6)  # Generating a random number between 1 and 6 (inclusive)
        print("Roll:", roll)  
        min_roll = min(min_roll, roll)  
        max_roll = max(max_roll, roll)  
        sum_rolls += roll  
    average_roll = sum_rolls / 12  # Calculating the average roll
    return min_roll, max_roll, average_roll  # Returning the statistics directly

# Function to process the results by calculating square roots and exponentials
def process_results(min_roll, max_roll, average_roll):
    min_sqrt = math.sqrt(min_roll)  # Calculating the square root of the minimum roll
    max_sqrt = math.sqrt(max_roll)  # Calculating the square root of the maximum roll
    avg_sqrt = math.sqrt(average_roll)  # Calculating the square root of the average roll
    min_exp = math.exp(min_roll)  # Calculating the exponential of the minimum roll
    max_exp = math.exp(max_roll)  # Calculating the exponential of the maximum roll
    avg_exp = math.exp(average_roll)  # Calculating the exponential of the average roll
    return min_sqrt, max_sqrt, avg_sqrt, min_exp, max_exp, avg_exp
# Returning the square roots and exponentials as a tuple

# Main function
def main():
    print("Welcome to the dice rolling program!")  
    print("You will roll a 6-sided die 12 times.")
    input("Press enter to continue.")
    print("Here are the results of each roll:")
    min_roll, max_roll, average_roll = roll_dice()  # Function call to roll the dice and calculate statistics
    min_sqrt, max_sqrt, avg_sqrt, min_exp, max_exp, avg_exp = process_results(min_roll, max_roll, average_roll)
    input("Press enter to continue.")
    # Function call to process results
    print("Here are some statistics based on your rolls:")  
    print("Minimum roll:", min_roll)  
    print("Maximum roll:", max_roll)  
    print("Average roll:", f"{average_roll:.2f}")  
    print("Square root of the minimum roll:", f"{min_sqrt:.2f}")  
    print("Square root of the maximum roll:", f"{max_sqrt:.2f}")  
    print("Square root of the average roll:", f"{avg_sqrt:.2f}")  
    print("Exponential of the minimum roll:", f"{min_exp:.2f}")  
    print("Exponential of the maximum roll:", f"{max_exp:.2f}")  
    print("Exponential of the average roll:", f"{avg_exp:.2f}")  

# Main function call
main()
