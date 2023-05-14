"""
704. Binary Search
Easy

"""
#Iterative solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0, len(nums)-1
        while left <=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1

#Recursive solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        return self.binarySearch(nums,target,0,len(nums)-1)
    def binarySearch(self,nums: List[int], target: int,left,right) -> int:      
        if left > right:
            return -1
        mid = (left+right)//2    
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid+1,right)
        else:
            return self.binarySearch(nums, target, left,mid-1)

