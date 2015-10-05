class Solution(object):
    def findRepeatedDnaSequences(self, s):
        ti = {'A':0,'C':1,'G':2,'T':3}
        n = len(s)
        if n<10: return []
        h = 0
        for i in xrange(10):
            h = h*4 + ti[s[i]]
        dp = {h:0}
        answer = []
        for i in xrange(10,n):
            h = 4*(h-ti[s[i-10]]*262144)+ti[s[i]]
            if h not in dp: dp[h] = 0
            elif dp[h] ==0:
                answer.append(s[i-10+1:i+1])
                dp[h] = 1
        return answer
