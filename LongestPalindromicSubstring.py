#import math
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        """
        This solution used Suffix Array and Range Minimum/Maximum Query
        You can find better solution from Google. I write this just to practice Suffix Array
        """
        def makesa(s,sa,height,rank):
            n = len(s)
            x,y = None,None
            cnt = [0]*2100
            ma= [0]*2100
            mb=[0]*2100

            x,y = ma,mb
            na = max(n,256)
            for i in xrange(n):
                x[i]=ord(s[i])
                cnt[x[i]]+=1
            for i in xrange(1,na):
                cnt[i] += cnt[i-1]
            for i in xrange(n-1,-1,-1):
                cnt[x[i]] -= 1
                sa[cnt[x[i]]] = i
            #print sa[:n]
            p,j=1,1
            while p<n:
                p ,i= 0,n-j
                while i<n:
                    y[p]=i
                    p+=1
                    i+=1
                for i in xrange(n):
                    if sa[i]>=j:
                        y[p]=sa[i]-j
                        p+=1
                for i in xrange(2100):
                    cnt[i] = 0
                for i in xrange(n):
                    cnt[x[y[i]]]+=1
                for i in xrange(1,na):
                    cnt[i] += cnt[i-1]
                for i in xrange(n-1,-1,-1):
                    cnt[x[y[i]]]-=1
                    sa[cnt[x[y[i]]]]=y[i]
                x,y=y,x
                x[sa[0]] = 0
                p = 1
                for i in xrange(1,n):
                    if (y[sa[i]]==y[sa[i-1]] and y[sa[i]+j]==y[sa[i-1]+j]):
                        x[sa[i]] = p-1
                    else:
                        x[sa[i]] = p
                        p+=1
                j*=2
                #print sa[:n]

            for i in xrange(n):
                rank[sa[i]] = i
            k = 0
            for i in xrange(n):
                if k!=0:
                    k-=1
                j = sa[rank[i]-1]
                while s[i+k]==s[j+k]:
                    k+=1
                height[rank[i]] = k



        def rmq_init(M,A,N):
            for i in xrange(N):
                M[i][0]= i
            j = 1
            while (1<<j)<=N:
                i = 0
                while i+(1<<j)-1<N:
                    if(A[M[i][j-1]]<A[M[i+(1<<(j-1))][j-1]]):
                        M[i][j] = M[i][j-1]
                    else:
                        M[i][j] = M[i+(1<<(j-1))][j-1]

                    i+=1

                j+=1



        def rmq(M,a,b,h):
            if a>b:
                a,b=b,a
            a+=1
            if a==b:
                return h[b]
            k = int(math.floor(math.log(b-a+1.0)/math.log(2.0)))
            return min(h[M[a][k]],h[M[b-(1<<k)+1][k]])


        n = len(s)
        s = s+'#'+s[::-1]+chr(0)
        sa = [0]*2100  #suffix array
        height = [0]*2100
        rank = [0]*2100
        makesa(s,sa,height,rank)

        M = [[0]*20 for i in xrange(2100)]
        rmq_init(M,height,2*n+2)
        m = 0
        l,r = 0,0

        for i in xrange(n):
            temp = rmq(M,rank[i],rank[2*n+1-i],height)
            if 2*temp>m:
                m = 2*temp
                l = i-temp
                r= i+temp-1
                #print m,l,r
            temp = rmq(M,rank[i],rank[2*n-i],height)
            if 2*temp-1>m:
                m = 2*temp -1
                l = i-temp+1
                r = i+temp-1

                #print m,l,r
        #print l,r
        return s[l:r+1]
