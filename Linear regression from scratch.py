study_hour = [1,2,3] # feature
result = [3,5,7] # target

m = 0
b = 0

n = len(study_hour)
iteration = 1000 
learning_rate = 0.01


for _ in range(iteration):
    db = 0
    dm = 0
    
    for i in range(n):
        y_pred = m * study_hour[i] + b
        db += y_pred - result[i]
        dm += study_hour[i] * (y_pred - result[i])

    b = b - learning_rate * 2/n * db 
    m = m - learning_rate * 2/n * dm 


print (m, b)