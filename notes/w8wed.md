# Week 8 Wednesday COMP-486
## Introduction to Neural Networks
An Artificial neural network (ANN) is a computational model that consists of several processing elements that receive inputs and deliver outputs based on their predefined activation functions.

ANNs are comprised of node layers, containing an input layer, one or more hidden layers, and an output layer.

Each node, orartificial neruon, connects to another and has an associated weight and threshold.
- If the output of any individual node is above the specified threshold value, that node is activated, sending its data through the network.

ANNs are at the very core of deep learning.

### Types of Neural Networks
Feedforward Neural Networks
- data flows in the forward direction
- no backpropagation

Multi-Layer Perceptron

Convolutional Neural Networks (CNNs)
- Used in image processing

Recurrent Neural Networks (RNNs)
- Commonly used in sequential data

### The Perceptron
Inputs are multiplied by various weights.
Use a linear function to sum the inputs, then activate if the sum is positive.
Send the data to the next layer if positive.

Threshold logic unit (TLU), or sometimes linear threshold unit (LTU).

Inputs --> Weights --> Linear function --> Step function --> Output

The step function is often the Heaviside step function or the sign function.

A perceptron is composed of one or more TLUs organized in a single layer.

Scikit-Learn provides a Perceptron that can be used for classification.

Perceptrons are incapable of solving some trivial problems.
Solution: Add more layers.