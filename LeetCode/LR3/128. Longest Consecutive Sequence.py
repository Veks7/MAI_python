'''
https://leetcode.com/problems/longest-consecutive-sequence/submissions/852717966/
'''

def getNewLength(self, item, hashed) -> int:
    answer = 1
    while item + 1 in hashed:
        item += 1
        answer += 1
    return answer
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        setNums = set(nums)
        for item in setNums:
            if item - 1 not in setNums:
                answer = max(answer, getNewLength(self, item, setNums))
        return answer
