# CA09 P10 - Binary Trees

For this problem we will implement a simple [Binary Tree](http://cslibrary.stanford.edu/110/BinaryTrees.html) data structure.

## Reading Resources

* https://en.wikipedia.org/wiki/Binary_tree
* http://cslibrary.stanford.edu/110/BinaryTrees.html 


## Problems

### 1. Tree Data

  * `get_height(self, root)` -- Returns the depth of tree represented as the longest path from the root to the edge.
  * `print_given_level(self, root, level)` -- Prints the nodes to certain level of the tree.

### 2. Traversals

A binary tree is a non-linear data structure and therefore there is more than one way to traverse (run) through the tree data.

A binary tree supports multiple methods of traversal, and we will be implementing the follwoing:
    * `print_inorder(self, root)` -- Prints the tree with **inorder traversal**.
    * `print_preorder(self, root)` -- Prints the tree with **preorder traversal**.
    * `print_postorder(self, root)` -- Prints the tree with **postorder traversal**.

For our sample tree, it looks like this.

```python
# Our tree look like this now
#          10
#        /    \
#      24      42
#     /  \    / \
#   20  44   88  22

# Inorder Traversal: 20 24 44 10 88 42 22 (LPR)
# Preorder Traversal: 10 24 20 44 42 88 22 (PLR)
# Postorder Traversal: 20 44 24 88 22 42 10 (LRP)
```

### 3. Sum Root to Leaf Numbers

Solve the problem [here](https://leetcode.com/problems/sum-root-to-leaf-numbers/) using Python.

### 4. Symmetric Trees

Solve the problem [here](https://leetcode.com/problems/symmetric-tree/) using Python.

### 5. Find Largest and Second Largest

  * `find_largest(self, root)` -- Retruns the value of the largest node.
  * `find_second_largest(self, root)` -- Retruns the value of the second largest node.








