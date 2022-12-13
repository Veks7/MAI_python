'''
https://leetcode.com/problems/two-sum/submissions/852702320/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in hashmap:
                return [hashmap[delta], i]
        
            hashmap[nums[i]] = i
