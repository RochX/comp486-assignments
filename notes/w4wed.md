# Week 4 Wednesday COMP-486
Will eventually gain an understanding of what is happening behind the scenes of machine learning and training.

## Linear Regression
A linear model makes a prediction by simply computing a weighted sum of the input features, plus a constant called the bias term (also called the intercept term).

### Linear Regression Training
Training a model means setting its parameters so that the model best fits the training set.
- We need measures of how well the model fits the training data.
- Most common performance measure of a regression model is the root mean square error.

### The Normal Equation
The equation $\theta = (X^TX)^{-1}X^Ty$ gives us the best values for $\theta$.

Each column of $X$ corresponds to a $\theta_i$ where $\hat{y} = \theta_0 + \theta_1x_1 + \dots + \theta_nx_n$.

Problems:
- The normal equation is only for linear regression.
- Slow when number of features is large (>10,000)

## Next time: Gradient Descent...