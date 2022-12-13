'''
https://leetcode.com/problems/valid-anagram/description/
'''
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        c = {}     
        
        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in c:
                c[char] = 1
            else:
                c[char] += 1
        
        for char in t:
            if char in c:
                c[char] -= 1
            else:
                return False
            
        for val in c.values():
            if val != 0:
                return False
        
        return True
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = dict()
        
        for c in s:
            if c in ds:
                ds[c] += 1
            else:
                ds[c] = 1
        
        for c in t:
            if c in ds and ds[c] > 0:
                ds[c] -= 1
            else:
                return False
        
        return not sum(ds.values())
