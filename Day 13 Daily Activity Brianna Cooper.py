#Name
print('Brianna Cooper')
#Date
print('June 17, 2024')
#Class
print('COSC 1336')
#Solving for
print('Day 13 Daily Activity')
input()

# This program demonstrates several string testing methods.

def main():
    # Get a string from the user.
    user_string = input('Enter a string: ')
    print('This is what I found about that string:')

    # Test the string.
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase.')
    
    # Print the string in uppercase.
    print('The letters in the string are now all uppercase:', user_string.upper())
    input()
    
    # Get a file name from the user.
    filename = input('Enter the filename: ')
    print('This is what I found about that file:')

    # Test the file.
    if filename.endswith('.txt'):
        print('That is the name of a text file.')
    elif filename.endswith('.py'):
        print('That is the name of a Python source file.')
    elif filename.endswith('.doc'):
        print('That is the name of a word processing document.')
    else:
        print('Unknown file type.')
    input()
    
    # This demonstrates how the find method is used for a substring.
    string = 'I have four fur babies'
    print('string:', string)
    position = string.find('four')
    if position != -1:
        print(f'The word "four" was found at index {position}.')
    else:
        print('The word "four" was not found.')
        input()

    #Demonstrate the split method.
    words = string.split()
    print('The string split into words:', words)

# Call the main function.
if __name__ == '__main__':
    main()
