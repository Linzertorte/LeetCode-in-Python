class Solution(object):
    def zigzagLevelOrder(self, root):
        def level(ns,c):
            if len(ns)==0: return []
            cur = map(lambda x:x.val,ns)
            if c==1: cur = cur[::-1]
            return [cur]+level([x for i in ns for x in [i.left,i.right] if x],1-c)
            
        if root is None: return []
        return level([root],0)
