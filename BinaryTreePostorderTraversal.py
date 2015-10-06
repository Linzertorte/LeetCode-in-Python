class Solution(object):
    def postorderTraversal(self, root):
        st = [(root,0)]
        p = []
        if not root: return p
        while st:
            h,c = st.pop()
            if c==1 or (not h.left and not h.right): p.append(h.val)
            else:
                st.append((h,1))
                if h.right: st.append((h.right,0))
                if h.left: st.append((h.left,0))
        return p
