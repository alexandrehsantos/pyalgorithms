class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    
    data = None
    next_node = None
    
    def __init__(self,data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
        """ 
        Singly linked list
        """
        
        def __init__(self):
            self.head = None
        
        def __is_empty(self):
            return self.head == None
        
        def size(self):
            """
            Return size of the current list
            """
            current = self.head
            count = 0
            
            while current:
                count += 1
                current = current.next_node
            return count
        
        def add(self, data):
            """
            Adds new node containing data at head of the list
            """
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
        
        def search(self, key):
            """
            Search the first node containing data that matches the key 
            """
            current = self.head
            
            while current:
                if current.data == key:
                    return current
                else:
                    current = current.next_node
            return None
            
        def __insert__(self, data, index):
            """Insert node into some position"""
            if index == 0:
                self.add(data)
            if index > 0:
                new = Node(data)
                
                current = self.head
                position = index
                
                while position > 1:
                    current = current.next_node
                    position -=1
                
                prev_node = current
                next_node = current.next_node
                
                prev_node.next_node = new
                new.next_node = next_node
                    
        def remove(self, key):
            current = self.head
            previus = None
            found = False
            
            while current and not found:
                if current.data == key and current is self.head:
                    found = True
                    self.head = current.next_node
                elif current.data == key:
                    found = True
                    previus.next_node = current.next_node
                else:
                    """To evaluete the previus if any key matches, so it will be the previus node"""
                    previus = current
                    """To evaluete the next node for the while loop"""
                    current = current.next_node
            return current
        
        def __repr__(self):
            
            nodes=[]
            current = self.head
            
            while current:
                if current is self.head:
                    nodes.append("[Head: %s]" % current.data)
                elif current.next_node is None:
                    nodes.append("[Tail: %s]" % current.data)
                else:
                    nodes.append("[%s]" % current.data)
                
                current = current.next_node
            return '-> '.join(nodes)
        
        def __add__(self, data, index):
            if index == 0:
                self.add(data)
            if index > 0:
                new = Node(data)
                
                position = index
                current = self.head
                
                while position > 1:
                    current = current.next_node
                    position -= 1 
                
                prev = current
                next = current.next_node  

        def node_at_index(self, index):
            if index == 0:
                return self.head
            else:
               current = self.head
               position = 0
               
            while position < index:
                 current = current.next_node
                 position +=1
            return current
                
        
        
                 