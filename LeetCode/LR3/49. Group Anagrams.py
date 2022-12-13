'''
https://leetcode.com/problems/group-anagrams/submissions/852713299/
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        htable = {}
        for word in strs:
            hcode = 1
            for char in word:
                hcode *= hash(char)
            if hcode in htable:
                htable[hcode].append(word)
            else:
                htable[hcode] = [word]
        # putting each list of anagrams into a string
        results = []
        for key in htable:
            results.append(htable[key])
        return results
