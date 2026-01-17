# Linear Regression From Scratch (Python)

This project demonstrates how linear regression works internally by implementing it from scratch in pure Python, without using libraries like NumPy, Pandas, or scikit-learn.

The goal is to understand the core idea behind gradient descent and how a model learns the best-fit line.

## Dataset

A small demo dataset representing:
- Study hours
- Exam results (out of 10)

Study Hours -> Result
1 -> 3
2 -> 5
3 -> 7

## Model

The model follows the linear equation:

y = m * x + b

Where:
- m is the slope
- b is the y-intercept

Both parameters are learned using batch gradient descent.

## Training Approach

- Initialize m and b to 0
- Compute prediction errors
- Calculate gradients
- Update parameters iteratively

After training, the model converges close to:

m ≈ 2  
b ≈ 1