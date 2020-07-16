"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        # the self value will be the root of the tree
        self.value = value
        self.left = None
        self.right = None        

    def insert(self, value):        
        """Insert the given value into the tree"""
        ## compare value to node value 
        if value < self.value:
            # insert value to left node
            if self.left == None:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)            
        if value >= self.value:
            # insert to the right, if the insert value equal current node value, insert to the right (Just to play along with the test)
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # else:    
        # # value already in BST, no insert
        #     return None  

    
    def contains(self, target):
        """Return True if the tree contains the value, and False if it does not"""
        #if target match the root node, return true        
        found = False
        if target == self.value:
            found = True
        # if target < node, go to node.left  and compare
        if target < self.value:
            if self.left is None:
                found = False
            else:
                found = self.left.contains(target)
        # if target > node, go to node.right and compare
        if target > self.value:
            if self.right is None:
                found = False
            else:
                found = self.right.contains(target)
        return found

    def get_max(self):
        """Return the maximum value found in the tree"""
        # Note that we should always compare to the right side of node until there is no right
        if self.right == None:
            max_val = self.value
        else:
            max_val = self.right.get_max()
        return max_val
        
    def for_each(self, fn):
        """Call the function `fn` on the value of each node"""
        # # simple case of recursion is the leaf node
        # # for_each would be for one
        # if (self.left is None) & (self.right is None):
        #     fn(self.value)
        # elif self.left is not None:
        #     self.left.for_each(fn)
        # elif self.right is not None:
        #     self.right.for_each(fn)
        #map(fn, self.value)
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
       

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# x = BSTNode(10)
# x.insert(5)
# x.insert(15)
# x.insert(3)
# x.insert(7)
# x.insert(12)
# print(dir(x))
# print(x.value)
# print(x.left.value)
# print(x.right.value)
# print(x.contains(7))
# print(x.contains(22))
# print(x.get_max())

# from math import sqrt
# print(x.for_each(sqrt))