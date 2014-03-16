class Node:
    def __init__(self,k,x):
        self.key=k
        self.val=x
        self.prev=None
        self.next=None

class DoubleLinkedList:
    def __init__(self):
        self.tail=None
        self.head=None
        
    def isEmpty():
        return not self.tail
    def removeLast(self):
        self.remove(self.tail)
        
    def remove(self,node):
        if self.head==self.tail:
            self.head,self.tail=None,None
            return
        if node == self.head:
            node.next.prev=None
            self.head=node.next
            return
        if node ==self.tail:
            node.prev.next=None
            self.tail=node.prev
            return
        node.prev.next=node.next
        node.next.prev=node.prev
        
    def addFirst(self,node):
        if not self.head:
            self.head=self.tail=node
            node.prev=node.next=None
            return
        node.next=self.head
        self.head.prev=node
        self.head=node
        node.prev=None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity=capacity
        self.size=0
        self.P=dict()
        self.cache=DoubleLinkedList()
    # @return an integer
    def get(self, key):
        if (key in self.P) and self.P[key]:
            self.cache.remove(self.P[key])
            self.cache.addFirst(self.P[key])
            return self.P[key].val
        else: return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.P:
            self.cache.remove(self.P[key])
            self.cache.addFirst(self.P[key])
            self.P[key].val=value
        else:
            node=Node(key,value)
            self.P[key]=node
            self.cache.addFirst(node)
            self.size +=1
            if self.size > self.capacity:
                self.size -=1
                del self.P[self.cache.tail.key]
                self.cache.removeLast()
