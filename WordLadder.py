class Solution:
    lowercase = map(chr, range(97, 123))
    def ladderLength(self, start, end, dic):
        def nextWord(w,dic):
            for i in xrange(len(w)):
                for c in self.lowercase:
                    w1 = w[:i]+c+w[i+1:]
                    if c!=w[i] and w1 in dic:
                        yield w1
        dic.add(end)
        dist = dict()
        dist[start] = 1
        queue = collections.deque()
        queue.append(start)
        while len(queue)!=0:
            head = queue.popleft()
            if head == end:
                return dist[head]
            for w in nextWord(head,dic):
                if w not in dist:
                    dist[w] = dist[head]+1
                    queue.append(w)
        return 0
