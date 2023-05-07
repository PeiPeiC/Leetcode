"""
62. Unique Paths
Medium

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[0 for i in range(n)] for j in range(m)]
        # set the base case values
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        # calculate the number of unique paths for each cell
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

# create an instance of the Solution class
sol = Solution()

# call the uniquePaths method with test inputs
m = 3
n = 7
result = sol.uniquePaths(m, n)

# print the result
print(result)
