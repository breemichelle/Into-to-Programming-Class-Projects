#Selling product need to ship via carrier
#Carrier 1 USPS
#Carrier 2 UPS
#Carrier 3 FedEX

shipping_cost = 0
carrier = input("Choose carrier selection. Enter 1 for USPS, 2 for UPS, 3 for FedEx. ")
USPS_fee = "1"
UPS_fee = "2"
FedEx_fee = "3"

if carrier == "1":
    shipping_cost =+ USPS_fee
else:
    if carrier == "2":
        shipping_cost =+ UPS_fee
    if  carrier == "3":
        shipping_cost =+ FedEx_fee
            
print("Shipping cost" , shipping_cost)

weight = input("how much does the package weight in oz? ")
if weight < "10 oz" "+ 1.00 to shipping_cost)":
    elif weight > "10 oz ^ < 22 oz" "+ 2.00 to shipping_cos)":
if weight > "22 oz ^ < 48 oz" "+ 3.00 to shipping_cost)":
