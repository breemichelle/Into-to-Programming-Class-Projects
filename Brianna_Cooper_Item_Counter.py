#Name
print('Brianna Cooper')
#Date
print('June 14, 2024')
#Class
print('COSC 1336')
#Solving for
print('Weekly Project 3 Part 3')

def count_names_in_file(filename):
    # Open the file.
    with open(filename, 'r') as file:
        # Initialize a counter for the names in the file.
        name_count = 0

        # Iterate through each line in the file.
        for line in file:
            # Increment the counter for each line read.
            name_count += 1

    # The file is automatically closed when the 'with' block is exited.
    return name_count

# Specify the filename
filename = 'names.txt'

# Call the function and print the result
number_of_names = count_names_in_file(filename)
print(f"There are {number_of_names} names in the file '{filename}'.")
    
    
