'''
Given an integer array nums and an integer k, return true if 
there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}

        for i,val in enumerate(nums):
            if val in seen and i-seen[val] <=k :
                return True
            else:
                seen[val] = i

        return False