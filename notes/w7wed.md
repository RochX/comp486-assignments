# Week 7 Wednesday COMP-486
## Today: Ensemble Learning
Wisdom of the crowd

A group of predictors (models) is called an ensemble.
Ensemble learning is the process by which multiple models are strategically generated and combined to solve a particular computational intelligence problem.

### Voting Classifiers
"Voting Classifier" is a machine learning model that trains on an ensemble of numerous models and takes the option that the majority say.

The basis for this comes from the *law of large numbers*.
Running an experiment multiple times will get us closer to the average value.

Types:
- Hard voting: the predicted output class is a class with the highest majority of votes.
- Soft voting: the output class is the prediction based on the average probability given to that class.
  Each model gives their probabilities, which are then averaged on a per class basis.

## Ensemble Learning cont.
Ensemble methods work best when the predictors are as independent from one another as possible.

One way to get diverse classifiers is to train them using very different algorithms.
This increases the different types of errors.

To get a diverse set of classifiers:
- Use very different training algorithms
- Use the same training algorithm for every predictor but train them on different random subsets of the training set.

## Bagging and Pasting
To use the same training algorithm for every predictor but train them on different random subsets of the training set.
Bagging:
- Sampling is performed **with** replacement.
Pasting:
- Sampling is performed **without** replacement.

Once all predictors are trained, the ensemble can make a prediction for a new instance by:
- Aggregating the predictions of all predictors (like hard voting)
- Or the average for regression.

### Out-of-Bag Evaluation
Instances of training data that are not sampled.
On average its about 37% of data is not sampled.
The out-of-bag instances can then be used as its own validation set.

### Random Patches and Random Subspaces
A `BaggingClassifier` supports sampling the features as well.
Controlled by hyperparameters `max_features` and `bootstrap_features`.

Sampling both training instances and features is called the *random patches methods*.
Keeping all training instances while sampling features is called the *random subspaces method*.

## Summary
Ensemble learning
- Multiple models are trained for the same problem.
- We can either use diverse models
- Or use one model with subsets of the training instances
  - This can be done with bagging and pasting

We can sample instances *and* features.