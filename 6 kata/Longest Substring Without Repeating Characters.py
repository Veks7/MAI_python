'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # словарь для отмечания позиций встреченных букв
        last_seen = {}
        # указатель на прошлую повторенную букву
        last = 0
        # максимальная длина неповторяющейся подстроки
        longest = 0
        for r in range(len(s)):
            # если символ уже был, то присваиваем указатель на в прошлый раз встреченный символ
            if s[r] in last_seen:
                last=max(last_seen[s[r]], last)
            
            # присваиваем очередному проверяемому символу указатель на текущую позицию (если символ первый раз встречается, то добавляется в словарь)
            last_seen[s[r]]=r+1
            # максимальная длина неповторяющихся символов будет равна разности текущего указателя и указателя l
            longest=max(longest, r - last + 1)
        return longest
