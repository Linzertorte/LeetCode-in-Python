class Solution(object):
    def rightSideView(self, root):
        def right(level):
            if len(level)==0: return []
            return [level[-1].val]+right([x for i in level for x in [i.left,i.right] if x])
        if not root: return []
        return right([root])
