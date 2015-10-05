class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        w = max(A,E)
        e = min(C,G)
        n = min(D,H)
        s = max(B,F)
        area = (C-A)*(D-B)+(G-E)*(H-F)
        if w<e and s<n: area -= (e-w)*(n-s)
        return area
