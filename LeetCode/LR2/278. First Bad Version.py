'''
278. First Bad Version
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
                               
        return left 
