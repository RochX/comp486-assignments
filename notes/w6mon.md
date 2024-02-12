# Week 6 Monday COMP-486
Last time: logistic/softmax regressions

## Support Vector Machines
- Linear SVM Classification
- Nonlinear SVM Classification

SVMs shine with small to medium-szed nonlinear datasets.

### Linear SVM Classifier
A linear Support Vector Classifier (SVC) tries to find a line/hyperplane that separates the True labels from the False labels.
The output of training is a decision funtion that tells us how close to the line we are.
Positive decision values mean True and Negative decision values mean False.

Can be thought of as a *large margin* classification.

Hard margin classification:
  If we strictly impose that all instances must be off the street and on the correct side.
  There are two main issues with hard margin classification:
  - It only works if the linearly separable.
  - It is senstitive to outliers

## SVM Regression