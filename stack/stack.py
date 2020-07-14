"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import array as array
import context

from singly_linked_list.singly_linked_list import Node, LinkedList

# 1. Use array to implement stack
# class Stack:
#     """
#     Array as storage structure
#     Note array is easier to append so we refere index [-1] as the top of stack
#     """
#     def __init__(self):
#         self.size = 0
#         self.storage = array.array('f',[])

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.size ==0:
#             print('Stack is empty, nothing to pop.')
#             return None
#         self.size -= 1
#         print(self.storage)
#         item_to_pop = self.storage[-1]
#         self.storage.remove(item_to_pop)
#         return item_to_pop

# # 2. Use linked list to implement stack
class Stack: 
    """
    Linked list as storage structure
    Linked list is easier to augment/remove from the head, 
    so we refere its head as the top of stack
    """
    def __init__(self):
        self.storage = LinkedList()
        return None
        
    def __len__(self):        
        # case: no node
        if self.storage.head == None:
            size = 0
            return size
        # case: 1 node
        size = 1 
        current_node = self.storage.head
        while current_node.get_next() != None:
            # loop until the last current is tail
            current_node = current_node.get_next()
            size += 1
        return size

    def push(self, value):        
        # push by adding to head
        if self.storage.head == None:
            self.storage.head = Node(value)
        else:
            new_node = Node(value, self.storage.head)
            self.storage.head = new_node
        print(self.storage.head.value)    

    def pop(self):
        if len(self) == 0:
            return None
        value = self.storage.head.get_value()   
        self.storage.remove_head()
        return value

 # 3. The difference of using different data structure to implement stacks:
 #    Array implemented stack must have same data type for all element; 
 #        linked-list implemented stack can have mixed data type. 
 #    Comparing method runtime: 
 #        array implemented stack: pop ~O(1), push ~O(1), len ~O(n); 
 #        linked list implemented stack: pop ~O(n), push ~O(n), len~O(n).   
    
