#Name
print('Brianna Cooper')
#Date
print('June 14, 2024')
#Class
print('COSC 1336')
#Solving for
print('Weekly Project 3 Part 3')

def main():
    #Open the numbers.txt file.
    display_numbers_from_file = open('numbers.txt', 'r')

    #Read the first line from the file.
    numbers = display_numbers_from_file.readline()

    #Read the rest of the file.
    while numbers != '':
        #Display the contents in the file.
        print(numbers.strip())

        #Read the next line in the file
        numbers = display_numbers_from_file.readline()
    
    #Close the file
    display_numbers_from_file.close()

main()
        
        

    
        

    
