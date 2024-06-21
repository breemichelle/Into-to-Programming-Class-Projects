count = 0
total = 0

getData = open('data.txt', 'r')

number = getData.readline()   #initialization

while number != '':    #condition
    number = int(number)   #recast the string value as a number
    count = count + 1
    total = total + number
    print('Here')
    print(number, ' ', count, ' ', total)
    number = getData.readline()   #update

getData.close()

average = total/count
print('The average of the numbers read in is ', average)

putData = open('report.txt', 'w')
putData.write('The average of the numbers read in is ' + str(average))
putData.close()
