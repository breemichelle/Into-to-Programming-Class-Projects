# Name:
print('Brianna Cooper')
# Assignment:
print('Weekly Project 2')
# Date:
print('June 7, 2024')
# Class:
print('COSC 1336-79898')
#
# Purpose:
# The program calculates the shipping cost for packages based on user input.
# It takes into account the delivery service, package weight, shipping region,
# and delivery type. The program allows users to calculate costs for multiple
# packages and provides a total cost at the end.
#
# Inputs:
# - Delivery service: 1 (FedEx), 2 (UPS), 3 (USPS), 4 (DHL)
# - Package weight: 1 to 100 ounces (integer)
# - Shipping region: 1 (Central), 2 (Western), 3 (Eastern), 4 (International)
# - Delivery type: 1 (Overnight), 2 (Standard), 3 (Get it when you get it)
#
# Outputs:
# - Cost to ship each individual package
# - Total cost for shipping all packages

total_shipping_cost = 0
package_count = 0

while True:
    print("\nShipping Package #{}".format(package_count + 1))
    
    # Delivery service
    while True:
        try:
            delivery_service = int(input("Choose your delivery service (1-FedEx, 2-UPS, 3-USPS, 4-DHL): "))
            if delivery_service in [1, 2, 3, 4]:
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Package weight
    while True:
        try:
            weight = int(input("Enter the weight of your package in ounces (max 100 ounces): "))
            if 1 <= weight <= 100:
                break
            else:
                print("Weight must be between 1 and 100 ounces. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Shipping region
    while True:
        try:
            region = int(input("Choose your shipping region (1-Central, 2-Western, 3-Eastern, 4-International): "))
            if region in [1, 2, 3, 4]:
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Delivery type
    while True:
        try:
            delivery_type = int(input("Choose your delivery type (1-Overnight, 2-Standard, 3-Get it when you get it): "))
            if delivery_type in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Service fees
    FEDEX_FEE = 4
    UPS_FEE = 2
    USPS_FEE = 3
    DHL_FEE = 1

    if delivery_service == 1:
        service_fee = FEDEX_FEE
    elif delivery_service == 2:
        service_fee = UPS_FEE
    elif delivery_service == 3:
        service_fee = USPS_FEE
    else:
        service_fee = DHL_FEE

    # Weight fees
    if weight <= 8:
        weight_fee = 3.50
    elif 8 < weight <= 36:
        weight_fee = 4.75
    elif 36 < weight <= 72:
        weight_fee = 7.25
    else:
        weight_fee = 11

    # Region multipliers
    CENTRAL_MULTIPLIER = 1
    WESTERN_MULTIPLIER = 2
    EASTERN_MULTIPLIER = 3
    INTERNATIONAL_MULTIPLIER = 4

    if region == 1:
        weight_fee *= CENTRAL_MULTIPLIER
    elif region == 2:
        weight_fee *= WESTERN_MULTIPLIER
    elif region == 3:
        weight_fee *= EASTERN_MULTIPLIER
    else:
        weight_fee *= INTERNATIONAL_MULTIPLIER

    # Delivery fees
    OVERNIGHT_FEE = 17
    STANDARD_FEE = 7
    GET_IT_WHEN_YOU_GET_IT_FEE = 3

    if delivery_type == 1:
        delivery_fee = OVERNIGHT_FEE
    elif delivery_type == 2:
        delivery_fee = STANDARD_FEE
    else:
        delivery_fee = GET_IT_WHEN_YOU_GET_IT_FEE

    cost = service_fee + weight_fee + delivery_fee
    print("Cost to ship package #{}: ${:.2f}".format(package_count + 1, cost))

    total_shipping_cost += cost
    package_count += 1

    another_package = input("Do you have another package to ship? (yes/no): ").lower()
    if another_package != 'yes':
        break

print("\nTotal cost for shipping {} package(s): ${:.2f}".format(package_count, total_shipping_cost))
