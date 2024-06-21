weight = float(input('Enter the weight of the package in ounces. Maximum Weight is 32 ounces: '))

if weight <= 8:
    weight_fee = 2.50
elif weight > 8 and weight <= 16:
    weight_fee = 4.50
elif weight > 16 and weight <= 32:
    weight_fee = 7.50
else:
    weight_fee = 12.00
    print("Weight is above maximum allowed.")

total_weight = weight + weight_fee
print('Total weight:', total_weight)

