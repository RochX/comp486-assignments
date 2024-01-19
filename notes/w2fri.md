# Week 2 Friday COMP-486
## The Main Challenges of Machine Learning (cont)
### Irrelevant Features
In our example: Country Name

### Overfitting the Training Data
The model performs well on the training data, but it does not generalize well.

**Solutions:**
- Simplify the model
- Gather more data
- Ignore outliers

#### Regularization of a Linear Regression
Tweaking the parameters of $\overline{y} = \theta_1 + \theta_2x$.

### Underfitting the Training Data
The model is too simple for the training data.

**Solutions:**
- Select a more powerful model
- Feature Engineering

## Testing and Validating
The only way to know how well a model will generalize to new cases is to actually try it out on new cases.
Set aside some (about 20%) of the training data to test the model.

*Test Set:*
- A subset of the data not used to train the model.
- It is used to evaluate whether the final model works.

*Validation Set:*
- Part of the training data is split into this set, which is used to see if the model is good.
- It is used to evaluate the models in order to perform model selection.

### Error
If we get a 5% error when selecting a model but then get 15% error on the testing data, we know that the model has overfit the validation set.

## End-To-End Machine Learning Project
California housing census
### Frame the Problem
- Objectives?
  - Predict median housing price
- Data?
- Current solution?
- Model?
  - A regression model

### Select a Performance Measure
A typical performance measure for regression problems is the root mean square error (RMSE).
$$\text{RMSE}(\mathbf{X}, h) = \sqrt{\frac{1}{m}\sum_{i=1}^m (h(\mathbf{x}^{(i)}) - y^{(i)})}$$
If there are many outlier districts, in that case, you may consider using the mean absolute error (MAE)
$$\text{MAE}(\mathbf{X}, h) = \sum_{i=1}^m \left|h(\mathbf{x}^{(i)}) - y^{(i)}\right|$$

### Downloading the Data
Some data is public, but other data requires permission in order to download.

### Looking at `02_end_to_end_machine_learning_project.ipynb`

#### Creating a Test Set
Solutions:
- Set the random generator seed. Use `test_train_split` function.
- Use each instance's identifier to decide whether or not it should go in the test set (row index as the ID).

*Satratified Sampling:* the population is divided into homogeneous subgroups call *strata*, and the right number of instances are sampled from each stratum to guarantee that the test set is representative of the overall population.