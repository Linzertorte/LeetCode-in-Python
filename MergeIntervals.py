# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals,key=lambda x:(x.start,x.end))
        if len(intervals)==0:
            return []
        a = reduce(lambda y,x:(y[0],y[1],max(y[2],x.end)) if x.start<=y[2] else (y[0]+[Interval(y[1],y[2])],x.start,x.end)   , intervals[1:],([],intervals[0].start,intervals[0].end))
        return a[0]+[Interval(a[1],a[2])]
