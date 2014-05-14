# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        best = 0
        for p in points:
            angle_cnt=dict()
            same = 0
            lm = 0
            for q in points:
                angle=math.atan2(p.y-q.y,p.x-q.x)
                if p.x==q.x and p.y==q.y:
                    same += 1
                else:
                    angle_cnt[angle] = angle_cnt[angle]+1 if angle in angle_cnt else 1
                    lm=max(lm,angle_cnt[angle])
            best=max(best,same+lm)
        return best
