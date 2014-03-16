# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    def getAngle(self,p,q):
        x=p.x-q.x
        y=p.y-q.y
        g=self.gcd(x,y)
        if x==0 and y==0: return (0,0)
        if x==0: return (0,1)
        if y==0: return (1,0)
        if y>0: return (x/g,y/g)
        else: return (-x/g,-y/g)
        
    def maxPoints(self, points):
        best = 0
        for p in points:
            angle_cnt=dict()
            same = 0
            lm = 0
            for q in points:
                angle=self.getAngle(p,q)
                if angle ==(0,0):
                    same += 1
                else:
                    angle_cnt[angle] = angle_cnt[angle]+1 if angle in angle_cnt else 1
                    lm=max(lm,angle_cnt[angle])
            best=max(best,same+lm)
        return best
