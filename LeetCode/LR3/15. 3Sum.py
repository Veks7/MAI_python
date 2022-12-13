'''
https://leetcode.com/problems/3sum/submissions/852703019/
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        history = set()
        triplet = set()
        target = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                delta = target - nums[i] - nums[j]
                if delta in history:
                    triplet.add((delta, nums[i], nums[j]))
                
            history.add(nums[i])
        return triplet
