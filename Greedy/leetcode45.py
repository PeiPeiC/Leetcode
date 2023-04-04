"""
45. Jump Game II
import List from typing
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        step,curCover,nextCover = 0,0,0
        for i in range(len(nums)-1):
            nextCover = max(nextCover,i+nums[i])
            if i >= curCover:
                step += 1                
                if nextCover >= len(nums):
                    break
                curCover = nextCover
        return step

"""
test:

s=Solution()
nums = [2,3,0,1,4]
print(s.jump(nums))

"""
