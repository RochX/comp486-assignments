# Week 8 Monday COMP-486
## Ensemble Learning
### Last Time
Using multiple models at once to make predictions.

Bagging and pasting (with/without replacement)

Random patches: Selecting some features and some training instances

Random subspace: Selecting some features and all training instances

### Random Forests
A random forest is an ensemble of decision trees, generally trained via the bagging method (or sometimes pasting), typically with `max_samples` set to the size of the training set.

### Boosting
*Boosting* is any ensemble method that can combine several weak learners into a strong learner.
- The general idea of most boosting methods is to train predictors sequentially, each trying to correct its predecessor.
- Boosting methods:
  - AdaBoost
  - Gradient boosting

#### AdaBoost
One way for a new predictor model to correct its predecessor is to pay a bit more attention to the training instances that the predecessor underfit, which results in new predictors focusing more and more on the hard cases.

#### Gradient Boosting
Sequentially adds predictors to an ensemble, each one correcting its predecessor.

$y_n = y_{n-1} - \hat{y}_{n-1}$.
Then train with the new labels and same training data.