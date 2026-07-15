temp = []

for i in range(7):
    t = int(input("Enter Temperature: "))
    temp.append(t)

print("Maximum =", max(temp))
print("Minimum =", min(temp))
print("Average =", sum(temp) / 7)
