# Week 4 Friday COMP-486
Last time: The Normal Equation for linear regression.

## Linear Regression (Gradient Descent)
Generic optimization algorithm capable of finding optimal solutions to a wide range of problems.
It will tweak parameters iteratively in order to minimize a cost function.

It start by filling $\theta$ with random values, and then iterates to find the best value for $\theta$.
The jumps between $\theta$'s is the learning rate, which is a hyperparameter.

Problems with this strategy include local minimums and plateaus.

### Gradient Descent (scaling)
Data without scaling will negatively affect the gradient descent.

### Batch Gradient Descent
Partial derivatives of each $\theta_j$.
The gradient is a combination of all the partial derivates.
- We wish to minimize the mean square error.
- Hyperparameters of learning rate and epoches.
- NOTE: Has to load all of the data into memory.

### Stochastic Gradient Descent
Stochastic gradient descent picks a random instance in the training set at every step and computes the gradients based only on that single instance.
- Hyperparameters of learning rate, epoches, which instance to pick, etc.



### Mini-Batch Gradient Descent
Computes gradient descent on small random sets of data.
- Hyperparameters of learning rate, epoches, which batches ot pick, etc.

## Polynomial Regression
If data is more complex than a straight line than use a polynomial regression.

Pipeline:
Data --> Polynomial Transform --> Linear Regression --> Predictions

## Learning Curve

### Bias/Variance Trade-Off
Bias:
This part of the generalization error is due to wrong assumptions.
High-bias model is most likely to underfit the training data.

Variance:
This part is due to the model’s excessive sensitivity to small variations in the training data.
High-variance model is most likely to overfit the training data.

## Summary
- Learned another way to train a linear regression
- Gradient Descent
- Important hyperparameters, such as learning rate
- Derivation of the error function
- 3 types of gradient descents: batch, stochastic, mini-batch
- Learning curve: relates to the value of error for training and validation set.
  - Combined with bias and variance.
