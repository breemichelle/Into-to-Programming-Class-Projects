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
    shipping_cost += USPS_fee
else:
    if carrier == "2":
        shipping_cost += UPS_fee
    else:
        shipping_cost += FedEx_fee
            
print("Shipping cost:",shipping_cost)

weight = float(input("how much does the package weight in ounces? Max of 48 is allowed)"))
if weight < 10:
    shipping_cost+= 1
elif weight > 10 and weight <22:
    shipping_cost += 2
elif weight >= 22 and weight <= 48:
    shipping_cost =+ 3
else:
    print("your parcel exceeds weight allowed")
