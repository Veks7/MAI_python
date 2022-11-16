'''
35. Search Insert Position
'''
class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
 
