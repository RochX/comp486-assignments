# Week 2 Wednesday COMP-486
Today:
- Types of Machine Learning Systems
- Main Challenges
- Data and validation
## Types of Machine Learning Systems Categorization
- How they are *supervised* during training.
- Whether or not they can learn incrementally on the fly
- Instance-based or model-based learning

Independent choices for these three choices.

We will primarily cover supervised learning, batch learning.

### Supervised Learning
Keyword: **labeled data**

Typical supervised learning task:
- Classification: place data points into a category
- Regression: give data points a number

Predicted $y$ is denoted as: $\overline{y}$.
We will have that $\overline{y}$ depends on the features $x_i$.

Types of classifications we will cover: 
- Binary: only two categories
- Multi-classification: more than two categories

***This is the recommended type of learning to use for the group project!***

### Unsupervised Learning
The data has no labels.

- Clustering: groups data together without labeling
- Association Rule Learning: finding a relationship between

### Semi-Supervised Learning
Data has some labeled, but mostly unlabeled.
It will attempt to label all of the remaining unlabeled.

### Self-supervised Learning
The data is labeled but is damaged/incomplete in some way.
The unlabeled data is given labels.

### Batch/Offline Learning
All of the data is used at once to train the model.

### Online/Learning
The system is training incrementally by feeding it data instances sequentially.

### Dimensionality Reduction
The goal of dimensionality reduction is to reduce the number of features without losing the meaning of the data.
This is useful in order to visualize the data.

### Instance-based vs Model-based Learning
Instance-Based: Making a prediction by finding existing data that is already closest to it, then taking an average for computing $\overline{y}$.
- $k$-nearest neighbors classification: pick the closest $k$ data points and then place the new data in a group based upon these closest points.

Model-Based: Making predictions by finding the best function that works with the existing data.
- Using a clustering to group data, then placing new data within a group.

## Example: Model-based Learning
Does money make people happier?

Features: country and GDP per capita

Predicting life satisfaction

Supervised-learning

We will use a linear regression.
Training a model to find the best coefficients to a prediction function.

## Main Challenges of Machine Learning
- Insuficient Quantity of Training Data
- Poor-quality data
- Irrelevant features
- Over and under fitting data

### Nonrepresentative Training Data
Data that does not represent all of the possible features
- Can fix by either getting more data or acknowledging the limitations

### Poor-Quality Data
Data has numerous outliers, errors, missing points.

Continued in W2 Fri...