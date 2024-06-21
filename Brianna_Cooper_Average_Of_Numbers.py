#Name
print('Brianna Cooper')
#Date
print('June 14, 2024')
#Class
print('COSC 1336')
#Solving for
print('Weekly Project 3 Part 3')

def calculate_average_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if line:  # Check if the line is not empty
                    try:
                        number = int(line)
                        total += number
                        count += 1
                    except ValueError as ve:
                        print(f"Skipping line due to ValueError: {line} ({ve})")
            if count > 0:
                average = total / count
                print(f"The average of the numbers is: {average}")
            else:
                print("No valid numbers found to calculate the average.")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
calculate_average_from_file('numbers.txt')
