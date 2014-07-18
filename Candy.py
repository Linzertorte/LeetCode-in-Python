class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n = len(ratings)
        heap = sorted(zip(ratings,range(n)))
        
        candies = [0]*n
        for (rating,i) in heap:
            m = 1
            if i!=0 and ratings[i-1]<rating:
                m = max(m,candies[i-1]+1)
            if i!=n-1 and ratings[i+1]<rating:
                m = max(m,candies[i+1]+1)
            candies[i]=m
        return sum(candies)
