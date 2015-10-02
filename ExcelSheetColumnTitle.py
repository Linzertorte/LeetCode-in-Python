class Solution(object):
    def convertToTitle(self, n):
        def tc(x):
            return chr(ord('A')+x-1)
        ls = []
        while n!=0:
            x = n%26
            n /= 26
            if x == 0:
                x += 26
                n -= 1
            ls = [x] + ls
        return ''.join(map(tc,ls))
