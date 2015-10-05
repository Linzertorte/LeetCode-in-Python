class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            k = str(''.join(sorted(w)))
            if k not in d: d[k] = []
            d[k].append(w)
        return [sorted(y) for (x,y) in d.iteritems()]
