# Create a double linked list class, i.e., a list where each element 
#has an attribute previous and an attribute next, and of course previous 
#and next are also instances of the same class.  
class Node: 
    
    def __init__(self, data, to_head = None, to_tail = None):  
        
        self.data = data
        self.to_tail = to_tail
        self.to_head = to_head
        
    def __repr__(self):
        
        aprint = '('
        if self.to_head:            
            aprint += ' < '
        else:
            aprint += ' x '
        aprint += str(self.data) 
        if self.to_tail:            
            aprint += ' > '
        else:
            aprint += ' x '
        aprint += ')' 
        if self.to_tail:
            aprint += self.to_tail.__repr__()
        
        return aprint
        
        
class LinkedList:
    
    def __init__(self):
        
        self.root = None
        self.size = 0
        
    def add(self, data):
        
        new_node = Node(data, to_head = None, to_tail = self.root)
        if self.root:
            self.root.to_head = new_node
        self.root = new_node
        self.size += 1
        
        
    def __repr__(self):
        
        if self.root == None:
            return 'Empty'
        return self.root.__repr__()
    

    def remove(self, node_value):
        
        this_node = self.root.to_tail
 
        while this_node is not None:
            if this_node.data == node_value:
                if this_node.to_tail is not None:
                    this_node.to_tail.to_head = this_node.to_head
                    this_node.to_head.to_tail = this_node.to_tail
                else:                  
                    self.to_head = this_node.to_head
                    this_node.to_head.to_tail = None
 
            this_node = this_node.to_head

            
        
my_list = LinkedList()
my_list.add(5)
my_list.add(9)
my_list.add(1)
print(my_list)
print(my_list.remove(5))
print(my_list)
print(my_list.remove(5))