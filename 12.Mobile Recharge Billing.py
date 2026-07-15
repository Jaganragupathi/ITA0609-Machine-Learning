amount = float(input("Enter Recharge Amount: "))

if amount >= 500:
    discount = amount * 0.10
else:
    discount = amount * 0.05

total = amount - discount

print("Final Amount =", total)
