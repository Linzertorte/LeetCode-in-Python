
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        P=dict()
        for word in strs:
            w="".join(sorted(word))
            if w not in P:
                P[w]=[]
            P[w].append(word)
        ans=[]
        for key in P:
            if len(P[key])>1:
                for word in P[key]:
                    ans.append(word)
        return ans
