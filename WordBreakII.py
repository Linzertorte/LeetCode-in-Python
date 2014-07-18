class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dic):
        def dfs(i,s,dic,sentence,sentences):
            if i == len(s):
                sentences.append(sentence[1:])
                return
            for j in xrange(i+1,len(s)+1):
                if s[i:j] in dic:
                    #print s[i:j]
                    dfs(j,s,dic,sentence+" "+s[i:j],sentences)

        sentences = []
        s_cnt = [0]*128
        w_cnt = [0]*128
        for i in s:
            s_cnt[ord(i)] = 1
        for w in dic:
            for i in w:
                w_cnt[ord(i)] =1
        for i in xrange(128):
            if s_cnt[i]==1 and w_cnt[i]==0:
                return sentences
        if len(s)==0:
            return sentences
        dfs(0,s,dic,"",sentences)
        return sentences
