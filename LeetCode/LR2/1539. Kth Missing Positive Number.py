'''
1539. Kth Missing Positive Number
'''
class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        left = 0
        right = len(a)
        while left < right:
            mid = (left + right) // 2
            if a[mid] - mid > k:
                right = mid
            else:
                left = mid + 1
        return right + k 
