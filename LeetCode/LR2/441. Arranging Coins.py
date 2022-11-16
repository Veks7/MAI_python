'''
441. Arranging Coins
'''
class Solution:
   def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            temp = (mid*(mid+1))//2
            if temp == n:
                return mid
            elif (temp < n):
                left = mid + 1
            else:
                right = mid - 1
        return right
