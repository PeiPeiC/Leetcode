"""
70. Climbing Stairs
Easy

● Step 1 : Clarify the definition of dp[] array and index i
There are dp [i] distinct ways to climb to the i th stair

● Step 2 : Find a formula to calculate dp[i]

The methods to reach the (i-1)th and (i-2)th stairs are independent sets:
This is because the last step in the method to reach the (i-1)th stair is different from the last step in the method to reach the (i-2)th stair. 
Since each step can only climb up one or two stairs, the last step in the method to reach the (i-1)th stair and the last step in the method to 
reach the (n-2)th stair cannot be the same. 
Therefore, each method to reach the (n-1)th stair cannot contain a method to reach the (n-2)th stair at the same time.

The methods to reach the i th stair = {The methods to reach the i-1 th stair} + {The methods to reach the i-2 th stair}
-> dp[i] = dp [i-1]+ dp[i-2]

● Step 3 : Initialize dp array

dp = [1] * (n+1)

● Step 4 : Make sure the traverse order
forward traverse in this case 
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        else:
            dp = [1] * (n+1)
            dp[1]=1
            dp[2]=2
            for i in range(3,n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]
"""
Time complexity: O(n)
Space complexity: O(n)
