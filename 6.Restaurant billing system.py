amount = float(input("Enter food bill amount: "))
gst = amount * 0.05
service = amount * 0.10
total = amount + gst + service
print("Food Bill =", amount)
print("GST =", gst)
print("Service Charge =", service)
print("Total Bill =", total)
