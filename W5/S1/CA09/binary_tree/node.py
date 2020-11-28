# Define a class for the tree node.
class Node:

    # Define your __init__() method.
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        pass

    def insert_at(self, value, node):
        pass

    def get_height(self, root):
        pass

    def print_given_level(self, root, level):
        pass
    
    # Traversals

    def print_inorder(self, root):
        pass
    
    def print_preorder(self, root):
        pass

    def print_postorder(self, root):
        pass

    # Sum Root to Leaf Numbers
    def sum_root_to_leaf(self, root):
        pass

    # Symmetric Trees
    def is_tree_symmetric(self, root):
        pass
    
    # Find Largest and Second Largest

    def find_largest(self, root):
        pass

    def find_second_largest(self, root):
        pass

# Instantiating a tree with the root node with value (10)
root = Node(10)

# Our tree looks like this now
#        10
#      /    \
#     None   None

# Adding the left child of the root to 34
root.left = Node(24)

# Setting the right child of the root to 89
root.right = Node(42)

# Our tree looks like this now
#          10
#        /    \
#      24      42
#     /    \  /    \
#  None  None None None