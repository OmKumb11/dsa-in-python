import numpy as np 

x = np.array([1,2,3,4])
y = np.array([2,4,6,8])

w = 0.0
b = 0.0

learning_rate = 0.01
iterations = 100

print(f"Start: w={w}, b={b}")

for i in range(iterations):
    n = len(x)
    y_pred = w*x + b
    dw = -(2/n) * sum(x * (y - y_pred))
    db = -(2/n) * sum(y - y_pred)

    w = w - learning_rate*dw
    b = b - learning_rate*db 

    if i % 10 == 0:
        cost = sum((y - y_pred)**2) / n # Mean Squared Error
        print(f"Iter {i}: w={w:.3f}, b={b:.3f}, Cost={cost:.3f}")

print(f"Final: w={w:.3f}, b={b:.3f}")
print("Expected: w=2.000, b=0.000")