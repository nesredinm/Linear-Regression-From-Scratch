# Linear Regression from scratch (no external libraries)
# Demo dataset: study hours vs exam result (out of 10) for 3 students

study_hour = [1, 2, 3] # feature
result = [3, 5, 7] # target

# Initialize slope (m) and y-intercept (b)
m = 0
b = 0

n = len(study_hour)        # number of data points
iteration = 1000           # number of training steps
learning_rate = 0.01       # step size for gradient descent

for _ in range(iteration):
    db = 0
    dm = 0
    
    # Compute gradients over all data points
    for i in range(n):
        y_pred = m * study_hour[i] + b
        db += y_pred - result[i]
        dm += study_hour[i] * (y_pred - result[i])

    # Update parameters using batch gradient descent
    b = b - learning_rate * (2 / n) * db
    m = m - learning_rate * (2 / n) * dm

print(f"\nParameters: \nslope(m): {m}\ny-intercept(b): {b}\n")