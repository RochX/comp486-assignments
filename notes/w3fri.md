# Week 3 Friday COMP-486
## Classification
Supervised learning

We will using the MNIST dataset: 
Set of images of handwritten digits

Covert images to numbers by getting pixel data

Running `03_classification.ipynb` from the textbook GitHub

### Training a Binary Classifier
`SGDClassifier`

Predicting which number are 5 and are not 5.

### Performance Measures
#### Cross-Validation
Folds idea

#### Confusion Matrices
Measures correct vs incorrect predictions.
Takes in the training data labels and the predicted labels.
In the case of a binary classifier it tells us false positives and false negatives.

#### Precision and Recall
precision = $\frac{TP}{TP+FP}$ and recall = $\frac{TP}{TP+FN}$ where $TP$ is true positives, $FP$ is false positives, and $FN$ is false negative.

Precision measures how well the model differentiates between 5 and numbers that are not 5.

Recall measures how well the model predicts 5 when the true value is a 5.

It is often convenient to combine these two metrics into one score called the F1 score.

#### The Precision/Recall Trade-off
For each instance, the classifier computes a score based on a decision function.
- If that score is greater than a threshold, it assigns the instance tothe positive class (e.g. is a 5)
- Otherwise, it assigns it to the negative class (e.g. is not a 5)

#### Receiver Operating Characteristic
Classifiers that give curves closer to the top-left corner indicate better performance

## On W4 Mon
Quiz!

Working in the class on assignment 3.