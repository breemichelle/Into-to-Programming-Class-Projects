#input 5 integers, find the max, min, and ave, and display the results

#import Stats
from StatsEx import FindMax, FindMin, FindAve

def main():
    #input

    num1 = int(input('Enter an integer data value 1: '))
    num2 = int(input('Enter an integer data value 2: '))
    num3 = int(input('Enter an integer data value 3: '))
    num4 = int(input('Enter an integer data value 4: '))
    num5 = int(input('Enter an integer data value 5: '))

    #should we conduct input validation?

    #calculate

    maxValue = FindMax(num1, num2, num3, num4, num5)
    minValue = FindMin(num1, num2, num3, num4, num5)
    aveValue = FindAve(num1, num2, num3, num4, num5)

    #display

    print('The max value is ', maxValue)
    print('The min value is ', minValue)
    print('The average value is ', aveValue)

main()

