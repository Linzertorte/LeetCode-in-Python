class Solution(Object):
  def minCostII(self,costs):
    if len(costs)==0:
      return 0
    n = len(costs)
    k = len(costs[0])
    m1,m2,x = 0,0,-1
    for i in xrange(0,n):
      nm1,nm2,nx = float('inf'),float('inf'),-1
      for j in xrange(0,k):
        total = m1+cost[i][j] if j != x else m2+cost[i][j]
        if total<=nm1:
          nm1,nm2,nx = total,nm1,j
        elif total<=nm2:
          nm2 = total
      m1,m2,x = nm1,nm2,nx
    
    return m1
