# Week 3 Wednesday COMP-486
## Selecting and Training a Model
Predicting a number: use a regression

Predicting a category: use a classification
### Linear Regression
Using `make_pipeline(preprocessing, LinearRegression())` to process the data (feature scaling, filling in missing values, etc) before putting it into the linear regression.

Mean squared error:
- A measure of distance between predictions and true values.
- A mean squared error of `68000` means true values are plus or minus `68000` the predicted value.

Linear Regression score: `lin_reg.score(data, data_labels)` gives a precentage (think $r^2$ value).

### Decision Tree Regressor
Start with the main feature; choose the main feature by using a correlation.
Create a tree where one can go through all of the features in a tree and determine the predicted value.

#### Cross-Validation
Use: $k$-fold cross validation feature.
Randomly splits the training set into $k$-fold noneverlapping subsets.
Train and evaluate a model $k$ times, using $k-1$ folds for training and the remaining fold for validation.
The fold left out changes between each training.

### Random Forest Regressor
Random forests work by training many decision trees on random subsets of the features, then averaging out their predictions.
This model is call an *ensemble* since it is composed of many other models (in this case many decision trees).

### Fine-Tune Your Model
Compute the mean squared error on the test set.

## Project
Steps:
- Get the data
- Investigate the data
- Clean the data
- Split the data

## Quiz W4 Monday
Will go over chapters 1 and 2.
The quiz will be open book.