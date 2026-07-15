distance = float(input("Enter Distance: "))
mileage = float(input("Enter Mileage: "))
price = float(input("Enter Fuel Price: "))

fuel = distance / mileage
cost = fuel * price

print("Fuel Cost =", cost)
