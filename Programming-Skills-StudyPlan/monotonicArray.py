'''An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.'''

class Solution:
    def isMonotonic(self,nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        increasing = False  
        decreasing = False  
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increasing = True 
            elif nums[i] < nums[i-1]:
                decreasing = True  
            if increasing and decreasing:  
                return False
        return True


