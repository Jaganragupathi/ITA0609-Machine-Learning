vehicle = input("Enter Vehicle (Bike/Car): ")
hours = int(input("Enter Hours: "))

if vehicle == "Bike":
    fee = hours * 20
else:
    fee = hours * 50

print("Parking Fee =", fee)
