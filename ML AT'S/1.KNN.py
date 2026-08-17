import math

X = [[1,1], [2,2], [3,3], [6,6], [7,7]]
Y = [0,0,0,1,1]

test = [5,5]

k = int(input("Enter K: "))

distance = []

for i in range(len(X)):
    d = math.sqrt((X[i][0]-test[0])**2 + (X[i][1]-test[1])**2)
    distance.append((d,Y[i]))

distance.sort()

nearest = distance[:k]

print("Nearest Neighbours:", nearest)

classes = [x[1] for x in nearest]

prediction = max(set(classes), key=classes.count)

print("Predicted Class:", prediction)

correct = 0

for i in range(len(X)):
    if Y[i] == prediction:
        correct += 1

accuracy = correct / len(Y) * 100

print("Accuracy:", accuracy, "%")
