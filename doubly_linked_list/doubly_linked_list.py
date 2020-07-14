"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        self.prev = None
        self.next = None
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def __repr__(self):
        # string representation of DLL instance
        # print out all links in the DLL
        output = ''
        current = self.head
        while current != None:
            output += f"{current.value} <=> "
            current = current.next
        return output

    def add_to_head(self, value):
        """
        Wraps the given value in a ListNode and inserts it 
        as the new head of the list. 
        """    
        if self.length ==0: 
            # DLL is empty 
            self.head = ListNode(value, prev=None, next=None)
            self.tail = self.head
            self.length += 1
        else:
            # DLL is not empty
            new_head = ListNode(value, prev=None, next=self.head)
            self.head.prev = new_head
            self.head = new_head
            self.length += 1
        
    def remove_from_head(self):
        """
        Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        """
        if self.length == 0:
            # DLL empty
            return None
        
        # DLL not empty
        value = self.head.value
        if self.length == 1:
            # one-item DLL
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else: 
            # DLL has at least 2 items
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            self.length -= 1
        return value
            
    def add_to_tail(self, value):
        """
        Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly.
        """
        new_tail = ListNode(value)
        if self.length ==0:
            # empty DLL
            self.tail = new_tail
            self.head = self.tail
            self.length +=1
        else:
            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail
            self.length += 1
       
    def remove_from_tail(self):
        """
        Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """
        if self.length == 0:
            # DLL is empty
            return None
       
        value = self.tail.value    
        if self.length == 1:
            # DLL has one item
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        else:
            # DLL has at least 2 items
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return value                

    def move_to_front(self, node):       
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        """       
        if self.length == 0:
            return None

        if self.length ==1:
            return self
              
        current = self.head
        # loop through the chain until current = node
        while current != node:
            current = current.next
        
        # now current == node
        if current == self.tail:
            # if node is the tail
            self.remove_from_tail()            
            self.add_to_head(current.value)            

        else: 
            # if node has not None prev and next  
            # first relink prev and next (bypass node)  
            current.prev.next = current.next
            current.next.prev = current.prev
            # segment current
            current.prev = None
            current.next = None
            self.length -= 1
            # add node to head
            self.add_to_head(current.value)                         
        
    
    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        """
        if self.length == 0:
            # empty DLL
            return None
        if self.length == 1:
            # one-item DLL
            return self        
        # loop through the chain to find matching node       
        current = self.head
        while current != node:
            current = current.next
        assert(current == node)

        if current == self.head:
            # head is the node, move head to tail
            self.remove_from_head()
            self.add_to_tail(current.value)
        else:
            # node somewhere in the middle
            # by pass node and double link and segement node
            current.prev.next = current.next
            current.next.prev = current.prev
            current.prev = None
            current.next = None
            self.length -= 1
            # add node to tail            
            self.add_to_tail(current.value)
            
    def delete(self, node):
        """
        Deletes the input node from the List, preserving the 
        order of the other elements of the List.
        """
        if self.length == 0:
            return None
        
        current = self.head
        # loop through the chain to find node
        while current != node:
            current = current.next

        if current == self.head:
            self.remove_from_head()

        else: 
            # node somewhere in the middle
            # by pass node and double link and segement node
            current.prev.next = current.next
            current.next.prev = current.prev
            current.prev = None
            current.next = None 
            self.length -= 1      
    
    def get_max(self):
        """
        Finds and returns the maximum value of all the nodes 
        in the List.
        """
        if self.length ==0:
            return None
        if self.length ==1: 
            return self.head.value
        else:
            current = self.head
            while current.next != None:
                max = current.value
                if max <= current.next.value:
                    max = current.next.value
                current = current.next
            return max




    
# x = DoublyLinkedList()
# x.add_to_head(0)
# x.add_to_head(1)
# x.add_to_head(2)
# x.add_to_head(3)
# print(x)
# x.remove_from_head()
# print(x)
# x.add_to_tail(99)
# print(x)
# x.remove_from_tail()
# print(x)
# x.move_to_front(ListNode(1))
# print(x)
