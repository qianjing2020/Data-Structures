"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import context
from array import array
from singly_linked_list.singly_linked_list import LinkedList, Node
# # 1. Use array as storage
# class Queue:
#     def __init__(self):        
#         self.size = 0
#         self.storage = array('f', [])
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         # use the array [-1] as the top of stack
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         # remove array at [0]
#         print(self.storage)
#         if self.size == 0:
#             return None
        
#         value_dequeue = self.storage[0]
#         self.storage.remove(value_dequeue)
#         self.size -= 1
#         return value_dequeue

# # 2. Use linked list as storage
class Queue:
    def __init__(self):
        self.storage = LinkedList()
        self.size = 0

    def __len__(self):
        if self.storage.head == None:
            self.size = 0
        self.size = 1    
        current_node = self.storage.head
        while current_node is not self.storage.tail: 
            current_node = current_node.get_next()
            self.size += 1
        return self.size

    def enqueue(self, value):
        # use linked list head to enqueue

        new_head = Node(value, self.storage.head)
        self.storage.head = new_head
              
        
    def dequeue(self):
        # use linked list end to dequeue
        if not self.storage.head:
            # empty queue
            value_dequeue = None

        # one item queue
        elif self.storage.head is self.storage.tail:
            value_dequeue = self.storage.head.get_value()
            print(value_dequeue)
            self.storage.head = None
            self.storage.tail = None
            return value_dequeue

        else: # more than 1 item in queue
            value_dequeue = self.storage.tail.get_value()
            self.storage.remove_tail()
            
        return value_dequeue
                
        # self.storage.remove_tail()        
