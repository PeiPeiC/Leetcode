"""
1005. Maximize Sum Of Array After K Negations

import List from typing
"""

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums,key=lambda x:abs(x),reverse=True)
        i=0
        while i< len(nums) and k>0:
            if nums[i] < 0:
                nums[i]= (-nums[i])
                k-=1
            i+=1
        if (k%2 == 1):
            nums[-1] = -nums[-1]
        return sum(nums)

"""
test:
s = Solution()
nums =[4,2,3]
print(s.largestSumAfterKNegations(nums,k=1)

"""
        

        

        
        
        
