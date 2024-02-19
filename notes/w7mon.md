# Week 7 Monday COMP-486
## Decision Trees
Can perform both classification and regression tasks, and even multioutput tasks.

Requires little data preparations.
Decision trees are intuitive and their decisions are easy to interpret (e.g. "White box model").

### Attributes of Decision Trees
- Condition: Tells us which path to follow.
- Gini: Impurity of the node (e.g. `gini = 0.667` means that 2/3 of the data is not of the specified class). Lower gini is better.
- Sample: Number of instances used to train the node.
- Value: How many instances in each class.
- Class: What class this node predicts.

### CART
Scikit-Learn uses the Classification and Regreesion Tree (CART) algorithm to train decision trees.
- Splitting the training set into two subsets using a single feature $k$ and a threshold $t_k$.
- CART algorithm is a greedy algorithm: It does not check whether or not the split will lead to the lowest possible impurity several levels down.
- This problem is NP-Compete, so we settle for a good-enough tree.

### Entropy
Entropy is used as an impurity measure.
A set’s entropy is zero when it contains instances of only one class.

## Quiz W7 Wed
On chapters 5 and 6.