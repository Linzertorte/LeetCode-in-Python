class Solution(object):
    def inorderTraversal(self, root):
        st = [(root,0)]
        p = []
        if not root: return p
        while st:
            h,c = st.pop()
            if c==1 or (not h.left and not h.right): p.append(h.val)
            else:
                if h.right: st.append((h.right,0))
                st.append((h,1))
                if h.left: st.append((h.left,0))
        return p

'''
# Morris traversal
class Solution(object):
    def inorderTraversal(self, root):
        p = []
        cur = root
        while cur:
            if not cur.left:
                p.append(cur.val)
                cur= cur.right
            else:
                prev = cur.left
                while prev.right and prev.right!=cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    p.append(cur.val)
                    cur = cur.right
        return p
'''
