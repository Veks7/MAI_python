'''
852. Peak Index in a Mountain Array
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        temp = -1
        while left<=right:
            mid = (left+right)//2
            if arr[mid]>arr[mid+1]:
                temp = mid
                right = mid-1
            else:
                left = mid+1
        return temp
