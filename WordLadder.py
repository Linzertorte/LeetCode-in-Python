class Solution(object):
    def ladderLength(self, start, end, words):
        lowercase = map(chr, range(97, 123))
        words.add(end)
        words.add(start)
        def next_word(w):
            return [w[:i]+c+w[i+1:] for i in xrange(len(w)) for c in lowercase if c!=w[i] and w[:i]+c+w[i+1:] in words]
        queue, dist = collections.deque(), {}
        dist[start] = 1
        words.remove(start)
        queue.append(start)
        while queue:
            head = queue.popleft()
            if head==end:
                return dist[head]
            for w in next_word(head):
                if w not in dist:
                    dist[w] = dist[head]+1
                    words.remove(w)
                    queue.append(w)
        return 0
