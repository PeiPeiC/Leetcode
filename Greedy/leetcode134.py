"""
1.Brute force : 
Time compleity o(n^2)
iterating through all gas stations.
"""

class Solution:
  def canCompleteCircuit(self,gas:List[int],cost:List[int])->int:
    n = len(gas)
    for start in range(n):
      tank = 0
      for path in range(n):
        tank += gas[(start+path)%n]
        tank -= cost[(start+path)%n]
        if tank <0: 
          break
        if  path == n-1 : 
          return start
    return-1

"""
The (start+path)%n index calculation is used to ensure that we are iterating over the stations in a circular manner, 
i.e., if we reach the end of the gas and cost arrays, we continue from the beginning of the arrays again.

For example, consider the case where n=5 (i.e., there are 5 gas stations), and start=3 (i.e., we start at the 4th station):

When path=0, the index we need to access in the gas and cost arrays is (3+0)%5=3.
When path=1, the index we need to access in the gas and cost arrays is (3+1)%5=4.
When path=2, the index we need to access in the gas and cost arrays is (3+2)%5=0.
When path=3, the index we need to access in the gas and cost arrays is (3+3)%5=1.
When path=4, the index we need to access in the gas and cost arrays is (3+4)%5=2.
So, by using (start+path)%n as the index, we can ensure that we iterate over all stations in a circular manner, 
and avoid accessing elements outside the bounds of the gas and cost arrays.

"""

"""
2.Greedy

"""
class Solution:
  def canCompleteCircuit(self,gas:List[int],cost:List[int])->int:
    total = 0
    currTank = 0
    start = 0
    for i in range(len(gas)):
        currTank += gas[i]-cost[i]
        if currTank < 0:
            start = i+1
            currTank = 0
        total += gas[i]-cost[i]
    if total < 0:
        return -1
    return start
          
