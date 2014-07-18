class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        def same(strs,cnt):
            a = set(map(lambda s:s[cnt] if cnt<len(s) else -1, strs))
            return len(a)==1 and -1 not in a
        if len(strs)==0:
            return ''
        cnt = 0
        while same(strs,cnt):
            cnt += 1
        return strs[0][:cnt]
