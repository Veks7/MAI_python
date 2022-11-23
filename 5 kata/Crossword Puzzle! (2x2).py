'''
https://www.codewars.com/kata/5c658c2dd1574532507da30b/train/python
'''

from itertools import combinations, permutations

def find_list_words(lx, ly, hx, hy, letter):
    res = []
    
    if lx != hx and ly != hy:
        if lx == ly:
            s = set()
            for w in words:
                if w[lx] == letter:
                    s.add(w)
            res = list(s)
        else:
            s1 = set()
            s2 = set()
            for w in words:
                if w[lx] == letter:
                    s1.add(w)
                if w[ly] == letter:
                    s2.add(w)
            res = [list(s1)] + [list(s2)]
    
    else:
        c1, c2 = (lx, ly) if lx == hx else (ly, lx)
        
        s1 = set()
        for w in words:
            if w[c1] == letter:
                s1.add(w)
        s2 = set()
        for w in words:
            for s in s1:
                if w[c2] == s[not c1]:
                    s2.add(w)
        res = [list(s1)] + [list(s2)]
            
    return res


def crossword_2x2(puzzle):
    letter = ''
    letter_x, letter_y, hashtag_x, hashtag_y = 0, 0, 0, 0
    res = []
    
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j].isalpha():
                letter_x, letter_y, letter = i, j, puzzle[i][j]
            elif puzzle[i][j] == '#':
                hashtag_x, hashtag_y = i, j
    
    need_words = find_list_words(letter_x, letter_y, hashtag_x, hashtag_y, letter)
    
    if letter_x != hashtag_x and letter_y != hashtag_y:
        if letter_x == letter_y:
            for x in list(permutations(need_words, 2)):
                summa = values[x[0][0]] + values[x[0][1]] + values[x[1][0]] + values[x[1][1]]
                res += [(x[0], x[1], summa)] if letter_y else [(x[1], x[0], summa)]
        else:
            for x in need_words[0]:
                for y in need_words[1]:
                    if x != y:
                        res += [(y, x, values[x[0]] + values[x[1]] + values[y[0]] + values[y[1]])]
    
    else:
        c1, c2 = (letter_x, letter_y) if letter_x == hashtag_x else (letter_y, letter_x)
        for x in need_words[0]:
            for y in need_words[1]:
                if x[not c1] == y[c2] and x != y:
                    summa = values[x[0]] + values[x[1]] + values[y[0]] + values[y[1]]
                    res += [(y, x, summa)] if letter_x == hashtag_x else [(x, y, summa)]
    
    res.sort(key=lambda x: x[1])
    res.sort(key=lambda x: x[0])
    res.sort(reverse=True, key=lambda x: x[2])
    
    return res
