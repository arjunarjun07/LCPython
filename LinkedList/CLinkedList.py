class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.link = None
    
    def __repr__(self) -> str:
        return "[{0}]->({1})".format(self.data, self.link)


class CLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        
    def __repr__(self) -> str:
        
        res = []
        
        p = self.head
        while p:
            res.append(p.data)
            p = p.link

        return " -> ".join(res)
    
    def insert_begin(self, data):
        
        n = Node(data)
        
        if self.head is None:
            self.head = n
        else:
            n.link = self.head
            self.head = n
            
    def insert_end(self, data):
        
        n = Node(data)
        
        if self.head is None:
            self.head = n
        else:
            
            t = self.head
            
            while t:
                prev = t
                t = t.link
                
            prev.link = n
            
    def insert_after(self, data_to_search, data_to_insert):
        
        t = self.head
        while t:
            if t.data == data_to_search:
                break            
            t = t.link
        
        if t:
            n = Node(data_to_insert)
            n.link = t.link
            t.link = n
            
    def remove(self, data_to_del) -> bool:
        
        if self.head is None:
            return True

        if self.head.data == data_to_del:
            t = self.head
            self.head = self.head.link

            t.link = None
            del t
            return True
    
        t = self.head
        
        #if we try to remove the head node. We have to point head again properly
        prev = self.head
        
        while t and t.data != data_to_del:
            prev = t
            t = t.link
        
        #pointing prev node to t.link 
        prev.link = t.link
        
        #del node
        t.link = None
        del t
        return True
        
            
        
        
cl = CLinkedList()

cl.insert_begin("5")
cl.insert_end("6")
cl.insert_end("7")
cl.insert_end("8")

cl.remove("5")

print(repr(cl))