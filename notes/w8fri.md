# Week 8 Friday COMP-486
Last time: Artificial Neural Networks

## Multilayer Perceptron (MLP)
How is a MLP trained?
- Can use a gradient descent, but it is slow to just use gradient descent.
- Reverse-mode automatic differentiation.
  - Does forwards and backwards pass

### Backpropagation
In order for backprop to work properly, backpropagation algorithm replaced the step function with activation functions, such as:
– The sigmoid function: σ(z) = 1 / (1 + exp(–z)).
– The hyperbolic tangent function: tanh(z) = 2σ(2z) – 1.
– The rectified linear unit function: ReLU(z) = max(0, z)

Steps:
- Backpropagation makes predictions for a mini-batch (forward pass).
- Measures the error.
- Then goes through each layer in reverse to measure the error contribution from each parameter (reverse pass).
- Finally tweaks the connection weights and biases to reduce the error (gradient descent step).

Going over an example in class (see Intro to ANN slides).

### MLPs
MLPs can be used for
- Regression MLPs
- Classification MLPs

Hyperparameters
- hidden layers: Depends on problem, but typically 1 to 5
- neurons per hidden layer: Depends on problem, but typically 10 to 100
- output layer: one neuron per dimension
- Hidden activation: ReLU
- Output activation
- Loss function: MSE, or Huber if outliers