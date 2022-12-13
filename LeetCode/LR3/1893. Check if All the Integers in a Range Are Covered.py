'''
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/submissions/852701217/
'''
# через set
# class Solution:
#     def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
#         s = set()
#         for el in ranges:
#             for x in range(max(el[0], left), min(el[1] + 1, right + 1)):
#                 s.add(x)
#         s1 = set(range(left, right + 1))
#         print(s1)
#         s1.difference_update(s)
#         if len(s1):
#             return False
#         else:
#             return True

# через dict
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        d = { x : 0 for x in range(left, right + 1) }
        for el in ranges:
            for x in range(max(el[0], left), min(el[1] + 1, right + 1)):
                if x in d:
                    d[x] += 1
        for x in d:
            if not d[x]:
                return False
        return True
