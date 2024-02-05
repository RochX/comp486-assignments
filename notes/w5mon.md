# Week 5 Monday COMP-486

## Last Time
Gradient Descent (batch, stochastic, mini-batch)

Bias == underfitting

Variance == overfitting

## Today: Regularized Linear Models
The slide examples use stochastic gradient descent.
### Ridge Regression
A regularization term is added to the mean square error.
The hyperparameter $\alpha$ controls how much you want to regularize the model.
The $m$ represents the number of instances while $n$ represents the number of features.

It uses a $\ell_2$ norm.

### Lasso Regression
Least absolute shrinkage and selection operator (LASSO).
Adds regularization term to the mean square error that uses $\ell_1$ norm.

### Elastic Net Regression
Middle ground between ridge and lasso regression.
Uses a mix ratio of $r$.

### Using these regressions
Ridge is a good default.

If only a few features are useful one should prefer lasso or elastic net.

Dr. Tasnim prefers starting with elastic net with $\ell_1$ ratio $r = 0.5$.
## Early Stop
Can stop the training early, which may be useful because we might reach the best model early in training.
Further training could risk overfitting the training data.

We want to save the best model we have so far within training.

## On Wednesday
Midterm Take-Home Exam on Wednesday!

No class on Wednesday because of exam.