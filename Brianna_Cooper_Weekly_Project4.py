# Name:
print('Brianna Cooper')
# Assignment Title:
print('Weekly Project 4')
# Date Submitted:
print('June 21, 2024')
# Class Information:
print('COSC 1336')

# This program reads player statistics from a file named 'Stats.txt'
# It calculates and prints the average HR value, the highest RBI value,
# and the lowest RBI value among the players.

def main():
    # Read the file contents into a list
    try:
        with open('Stats.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("The file 'Stats.txt' was not found.")
        return

    # Initialize variables
    hr_values = []
    rbi_values = []

   # Skip the header line and process each subsequent line in the file
    for line in lines[1:]:
        # Split the line into components
        parts = line.strip().split()
        if len(parts) < 7:
            # Skip lines that do not have at least seven components
            continue

        try:
            # Extract HR and RBI values (5th and 6th columns respectively)
            hr = int(parts[5])
            rbi = int(parts[6])

            # Append values to the lists
            hr_values.append(hr)
            rbi_values.append(rbi)
        except ValueError:
            # Skip lines with invalid integer values
            continue

    if not hr_values or not rbi_values:
        print("No valid data found in the file.")
        return

    # Calculate the average HR value
    average_hr = sum(hr_values) / len(hr_values)

    # Find the highest and lowest RBI values
    highest_rbi = max(rbi_values)
    lowest_rbi = min(rbi_values)

    # Print the results
    print(f"The average HR value for the players is: {average_hr:.2f}")
    print(f"The highest RBI value in the list is: {highest_rbi}")
    print(f"The lowest RBI value in the list is: {lowest_rbi}")

# Run the main function
if __name__ == "__main__":
    main()
