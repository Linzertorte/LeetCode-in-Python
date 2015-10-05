class Solution(object):
    def minWindow(self, s, t):
        n = len(s)
        hist,wh = [0]*128,[0]*128
        for c in t:
            hist[ord(c)] += 1
        def lack():
            return len(filter(lambda i:wh[i]<hist[i], range(128)))!=0
        i,j=0,0
        while lack() and j<n:
            wh[ord(s[j])] +=1
            j+=1
        if j==n and lack(): return ''
        while wh[ord(s[i])]>hist[ord(s[i])]:
            wh[ord(s[i])] -= 1
            i+=1
        ai,aj = i,j
        while j<n:
            wh[ord(s[j])] +=1
            while wh[ord(s[i])]>hist[ord(s[i])]:
                wh[ord(s[i])] -= 1
                i+=1
            j+=1
            if j-i<aj-ai: ai,aj = i,j
        return s[ai:aj]
