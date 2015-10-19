class BSTIterator(object):
    def __init__(self, root):
        self.path,p = [],root
        while p:
            self.path.append(p)
            p=p.left
    def hasNext(self):
        return len(self.path)>0

    def next(self):
        x = self.path[-1]
        self.path.pop()
        p = x.right
        while p:
            self.path.append(p)
            p = p.left
        return x.val
