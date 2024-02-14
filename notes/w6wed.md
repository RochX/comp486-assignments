# Week 6 Wednesday COMP-486
## Nonlinear Support Vector Machine Model
Technique to tackle nonlinear problems:
– Polynomial Features
– Polynomial Kernel
Similarity Features
– Gaussian RBF Kernel

### Polynomial Kernel
Kernel trick allows us to get the same result as adding polynomial features *without* actually adding them!

### Similarity Features
Similarity features is to add features computed using a similarity function, which measures how much each instance resembles a particular landmark.

The function used for similarity is the Gaussian RBF function.

See [slide 19 in the slides](http://www.cs.kzoo.edu/cs486/slides/COMP486Chapter5.pdf) for an example on an one-feature dataset.

### SVM Regression
SVM can do a regression by fitting as many instances as possible on the street whiel limiting margin violations.