class Solution(object):
    def deleteNode(self, node):
        def delete(h): #return (val,node)
            if h.next is None:
                return h.val,None
            val = h.val
            h.val,h.next = delete(h.next)
            return val,h
        node.val, node.next = delete(node.next)
