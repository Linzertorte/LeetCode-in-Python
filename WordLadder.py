
class Solution:
    # @param start, a string                                                                            
    # @param end, a string                                                                              
    # @param dict, a set of string                                                                      
    # @return an integer
    lowercase = map(chr, range(97, 123))
    def ladderLength(self, start, end, dic):
        def isNext(w1,w2):
            cnt = 0
            for i in xrange(len(w1)):
                if w1[i]!=w2[i]:
                    cnt += 1
                if cnt >= 2:
                    break
            return cnt == 1
        def nextWord(w,dic):
            for i in xrange(len(w)):
                for c in self.lowercase:
                    w1 = w[:i]+c+w[i+1:]
                    if c!=w[i] and w1 in dic:
                        yield w1
        
            
        dist = dict()
        dist[start] = 1
        queue = collections.deque()
        queue.append(start)
        while len(queue)!=0:
            head = queue.popleft()
            if isNext(head,end):
                return dist[head]+1
            for w in nextWord(head,dic):
                if w not in dist:
                    dist[w] = dist[head]+1
                    queue.append(w)
            
        return 0
        
        
