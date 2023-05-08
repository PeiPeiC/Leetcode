"""
63. Unique Paths II
Medium

"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]== 1:
            return 0
        #print(f'obstacleGrid:{obstacleGrid}')

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        

        dp= [[0 for _ in range(cols)]for _ in range(rows)]

        for i in range(cols):
            if obstacleGrid[0][i]== 1:
                break
            dp[0][i] = 1
        for j in range(rows):
            if obstacleGrid[j][0]== 1:
                break
            dp[j][0] = 1
        #print(f'dp:{dp}')
        for i in range(1,rows):
            for j in range(1,cols):
                if obstacleGrid[i][j] == 0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

#test
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
solution = Solution()
result = solution.uniquePathsWithObstacles(obstacleGrid)
print(result)
