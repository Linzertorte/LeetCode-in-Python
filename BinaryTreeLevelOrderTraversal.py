class Solution(object):
    def levelOrder(self, root):
        def level(xs):
            if len(xs)==0: return []
            cur = map(lambda x:x.val, xs)
            return [cur] + level([j for i in xs for j in [i.left,i.right] if j])
        if root is None: return []
        return level([root])
