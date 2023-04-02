class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = 1
        preD = 0
        curD = 0
        for i in range(len(nums)-1):
            preD = nums[i+1]-nums[i]
            if preD*curD <= 0 and preD != 0:
                res += 1
                curD = preD
        return res
