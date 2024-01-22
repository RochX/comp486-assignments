# Week 3 Monday COMP-486
## Representative Test Set
Take a continuous numerical attribute and create a category attribute.
That is, placing continuous data within discrete bins.
Then create the representative test set by using the distribution of the bins.

|Category | Overall% | Stratified % | Random % | Strat. Error % | Rand. Error % |
|-|-|-|-|-|-|
|Category|How much of the data is in this category|Percent of stratified data in this category|Percent of random data in this category| error | error|

## Preparing the Data
Important:
- Put the test set aside
- Don't modify the original data; make copies

Visualize the data first if possible.

Look for correlations

What we may need for the training data:
- Clean the data
- Handle text and categorical attributes
- Feature scaling
- Transformations

Before that:
- Revert to a clean training set
- Separate predictors from the features

Clean the Data:
- Options to Fix Missing Data:
  - Get rid of the instances with little data
  - Get rid of the feature
  - Set the missing values to some value (imputation)

Handling Text and Categorical Entries
- Give each category a number
- One hot encoding (creates a sparse matrix)

### Feature Scaling and Transformation
Normalization and Stardardization

$x_{new} = \frac{x-x_{min}}{x_{max} - x_{min}}$ and $x_{new} = \frac{x- \mu}{\sigma}$