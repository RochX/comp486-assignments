# Week 4 Monday COMP-486
## Classifiers (cont.)
### Binary Classifiers
- SGDClassifier
- SVC

### Multiclass Classification
- Logistic Regression
- Random Forest Classifier

One way to create a multiclass classifier is to create many binary classifiers. 
(one-versus-the-rest aka OvR)
- For our digits we have 10 binary classifiers:
  Is the digit $x$ or not $x$? 
  Do this for each $x \in \{0, 1 \dots, 9\}$.
- When we make a prediction we get 10 values (how likely it is the given digit) and pick the highest one.

Another way is to train a classifier for every pair of digits. 
(one-versus-all aka OvA)

### Error Analysis on Multiclass Classification
Using a confusion matrix again.
This time the matrix is bigger.
In our example of digit classification, the confusion matrix is $10 \times 10$.

Errors normalized by rows or columns

## Continuing in class work on assignment 3...