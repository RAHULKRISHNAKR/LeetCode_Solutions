'''
You are given a 0-indexed integer array nums and two integers key and k. 
A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.
Return a list of all k-distant indices sorted in increasing order.
'''

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        index = [i for i,num in enumerate(nums) if num == key]

        for i in index:
            for j in range(len(nums)):
                if abs(i-j)<=k:
                    res.append(j)
        
        return sorted(list(set(res)))