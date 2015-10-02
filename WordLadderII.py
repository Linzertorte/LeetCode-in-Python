class Solution:
    def findLadders(self, start, end, words):
        lowercase = map(chr, range(97, 123))
        words.add(end)
        words.add(start)
        next_word = {}
        for w in words:
            next_word[w] = [w[:i]+c+w[i+1:] for i in xrange(len(w)) for c in lowercase if c!=w[i] and w[:i]+c+w[i+1:] in words]
        queue, dist = collections.deque(), {}
        dist[start] = 1
        queue.append(start)
        while queue:
            head = queue.popleft()
            for w in next_word[head]:
                if w not in dist:
                    dist[w] = dist[head]+1
                    queue.append(w)
        def dfs(i):
            return [[end]] if i==end else [[i]+path for j in next_word[i] if dist[j]==dist[i]+1 for path in dfs(j)]
        return dfs(start)
