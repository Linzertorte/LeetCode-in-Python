class Solution:
    lowercase = map(chr, range(97, 123))
    def findLadders(self, start, end, dic):
        def nextWord(w,word_id):
            for i in xrange(len(w)):
                for c in self.lowercase:
                    w1 = w[:i]+c+w[i+1:]
                    if c!=w[i] and w1 in word_id:
                        yield word_id[w1]

        def dfs(i,e,next_word,words,path,paths):
            path.append(words[i])
            if i==e:
                paths.append(path[:])
                del path[-1]
                return
            for j in next_word[i]:
                if dist[j] == dist[i]+1:
                    dfs(j,e,next_word,words,path,paths)
            del path[-1]


        dic.add(end)
        dic.add(start)
        words = list(dic)
        n = len(words)
        word_id = dict()
        for i in xrange(len(words)):
            word_id[words[i]] = i
        s,e = word_id[start], word_id[end]
        next_word = [[] for i in xrange(n)]
        for i in xrange(n):
            for j in nextWord(words[i],word_id):
                next_word[i].append(j)

        dist = [-1]*n
        queue = collections.deque()
        dist[s] = 1
        queue.append(s)

        while len(queue)!=0:
            head = queue.popleft()
            for i in next_word[head]:
                if dist[i]==-1:
                    dist[i] = dist[head]+1
                    queue.append(i)
        if dist[e]==-1:
            return []
        #print dist
        path = []
        paths = []
        dfs(s,e,next_word,words,path,paths)
        return paths
