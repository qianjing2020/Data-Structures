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

import sys
import os
cwd = os.getcwd()
parent = os.path.dirname(cwd)
sys.path.insert(0, os.path.abspath(parent))
# from stack.stack import Stack
from queue.queue import Queue


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
                # Note we basically shifted root for the insert method from self to self.left
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
        if self.right is None:
            return self.value
        max_val = self.right.get_max()
        return max_val
        
    def for_each(self, fn):
        """Call the function `fn` on the value of each node
        """
        # first apply fn to root
        fn(self.value)
        # traverse to left
        if self.left is not None:
            self.left.for_each(fn)        
        if self.right is not None:
            self.right.for_each(fn)
        """ Another approach: Depth first traversal: from the smallest to the biggest number in the tree"""
        # # first apply fn to far left node
        # if self.left is not None:
        #     self.left.for_each(fn) 
        # # then local root       
        # fn(self.value)
        # # then left
        # if self.right is not None:
        #     self.right.for_each(fn)

    # Part 2 -----------------------
    def get_node(self, node):
        """traverse the tree to find the node that match the input node
        and return subtree rooted at that node"""
        # use recursive algorithm to get the node
        # if self is None:
        #     return None
        # case 0: value match
        # extreme case:
        if self is None:
            return None
        # base case:    
        if self.value == node.value:
            return self
        # case 1: go search left part
        if node.value < self.value:
            if self.left is None:
                # no matching node
                return None
            else:
                return self.left.get_node(node)
        # case 2: go search right part
        if node.value > self.value:
            if self.right is None:
                # no matching node
                return None
            else:
                return self.right.get_node(node)
        else:
            print('Input node does NOT exist in the tree, or tree is None!')
    
    def in_order_print_tree(self):
        """print entire tree, use recursive, depth first traversal"""
        # extreme case:
        if self is None:
            return None
        # base case: 
        if self.left:
            self.left.in_order_print_tree()
        print(self.value) 
        if self.right:
            self.right.in_order_print_tree()

    def in_order_print(self, node):
        """ Print all the values in order from low to high, starting with the given node
        Hint:  Use a recursive, depth first traversal
        """
        newroot = self.get_node(node)
        newroot.in_order_print_tree()

    # def in_order_print(self, node):
    #     """ Print all the values in order from low to high, starting with the given node use a recursive, depth first traversal.
    #     Note that instead of two function, this can be achieved in only one
    #     """
    #     if self is None:
    #         return None
        
    #     # base case: node is self:
    #     if self.value == node.value:          
    #         # print the smallest first
    #         if self.left:
    #             print(self.left.value)
    #         # print the smallest parent node
    #         print(self.value)
    #         # print the bigger sibling
    #         if self.right:
    #             print(self.right.value)
    #     # nonbase case 1: node value smaller than self, go left 
    #     elif node.value < self.value:
    #         self.left.in_order_print(node)
    #     # nonbase case 2: node value bigger than self, go right 
    #     elif node.value > self.value:
    #         self.right.in_order_print(node)

    def bft_print_tree(self):
        """breadth first traversal method to print a tree """
        if self is None:
            return None
        # make a queue, add thehfirst node 
        current = self
        lst = Queue()
        lst.enqueue(current.value)
        # while queue is not empty
        while len(lst) > 0:
            # remove the current, and print it
            print(lst.dequeue())
            # add all children of the current
            if current.left:
                current = current.left
                lst.enqueue(current.value)
            if current.right:
                current = current.right
                lst.enqueue(current.value)
        
    def bft_print(self, node):
        """Print the value of every node, starting with the given node,
            in an breadth first traversal search.
        """
        # first find the node:
        newroot = self.get_node(node)
        # print the tree from the node:
        newroot.bft_print_tree()


    # def bft_print(self, node):
    #     """Print the value of every node, starting with the given node,
    #         in an iterative breadth first traversal, aka, Breadth first traversal.
    #     """
    #     # Use a queue obj to store traversed nodes, start with input node
    #     pass
        # while length of queue > 0
            # dequeue item
            # print item

            # place current item's left in queue is not None
            # place current item's right in queue if not None


        # base case: self is the node
        # 
        #lst = Queue()
        # if newroot.value == node.value:
        #     print.push(self.value)
        #     if self.left:
        #         lst.push(self.left.value)
        #     if self.right:
        #         lst.push(self.right.value)
            
        # # nonbase case 1: node value smaller than self, go left 
        # elif node.value < self.value:
        #     self.left.bft_print(node)
        # # nonbase case 2: node value greater than self, go right
        # else:
        #     self.right.bft_print(node)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # if self is the node, print self, go left until bottom then right
        # create a stack obj to store the value in order: right, self, left
        pass
        """lst = Stack()
        if self.value == node.value:
            if self.right:
                lst.push(self.right.value)
            lst.push(self.value)
            if self.left:
                lst.push(self.left)
        # apply recursion algorithm is self is not node
        elif node.value < self.value:
            self.left.dft_print(node)
        else:
            self.right.dft_print(node)  
        print(lst)    
                """




        # if self is not the node, recursion to locate self and do dft_print

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


root = BSTNode(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
root.insert(12)
print(dir(root))
print(root.value)
print(root.left.value)
print(root.right.value)
print(root.contains(7))
print(root.contains(22))
print(root.get_max())
# test fn
from math import sqrt
#test_fn = lambda x: print(f'sqrt of current node is {sqrt(x):.2f}')
test_fn = lambda x: print(f'/ {x} / ')
root.for_each(test_fn)

my_node = BSTNode(5)
#print(f'my_node is {my_node.value}')

x = root.get_node(my_node)
print('***********')
root.in_order_print_tree()
print('***********')
root.in_order_print(x)
print('*********')
root.bft_print_tree()
