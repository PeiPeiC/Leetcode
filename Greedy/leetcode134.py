#brute force

class Solution:
  def canCompleteCircuit(self,gas:List[int],cost:List[int])->int:
    n = len(gas)
    for i in range(n):
      tank = 0
      for j in range(n):
        tank += gas[(i+j)%n]
        tank += gas[(i+j)%n]
        if tank <0: break
        if  j == n-1 : return i
    return-1
