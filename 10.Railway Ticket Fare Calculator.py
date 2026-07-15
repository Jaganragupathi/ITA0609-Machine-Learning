fare = float(input("Enter Base Fare: "))
age = int(input("Enter Age: "))
cls = input("Class (First/Second): ")

if cls == "First":
    fare = fare + 200

if age < 12:
    fare = fare * 0.5
elif age >= 60:
    fare = fare * 0.7

print("Ticket Fare =", fare)
