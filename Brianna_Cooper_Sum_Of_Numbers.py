#Name
print('Brianna Cooper')
#Date
print('June 14, 2024')
#Class
print('COSC 1336')
#Solving for
print('Weekly Project 3 Part 3')

def calculate_total_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            total = 0  #Initializing
            for line in file: #Iterate through each line in the file
                line = line.strip()
                if line:  # Check if the line is not empty
                    try:
                        number = int(line)
                        total += number #Increment the total for each number in file
                    except ValueError as ve:
                        print(f"Skipping line due to ValueError: {line} ({ve})")
            print(f"The total of the numbers is: {total}") #Display
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
calculate_total_from_file('numbers.txt')
