import math

X = [1, 2, 3, 4, 5]
Y = [0, 0, 1, 1, 1]

w = 0
b = 0
lr = 0.1
epochs = 1000

for epoch in range(epochs):

    dw = 0
    db = 0

    for i in range(len(X)):
        z = w * X[i] + b
        yhat = 1 / (1 + math.exp(-z))

        dw += (yhat - Y[i]) * X[i]
        db += yhat - Y[i]

    w = w - lr * dw / len(X)
    b = b - lr * db / len(X)

correct = 0

for i in range(len(X)):

    z = w * X[i] + b
    yhat = 1 / (1 + math.exp(-z))

    if yhat >= 0.5:
        prediction = 1
    else:
        prediction = 0

    print(X[i], round(yhat, 3), prediction)

    if prediction == Y[i]:
        correct += 1

accuracy = correct / len(Y) * 100

print("Weight:", w)
print("Bias:", b)
print("Accuracy:", accuracy, "%")
