'''
https://www.codewars.com/kata/5ac62974348c2203a90000c0/train/python
'''
def check_line_on_digits(s):
    for el in s:
        if el.isdigit(): return True
    return False

def check_line_on_two_digits(s):
    for el in s:
        if el.isdigit() and len(el) == 2: return True
    return False

def check_was_two_digits(s, amount):
    for el in s:
        if el.isdigit() and int(el) - amount >= 10: return True
    return False

def check_was_one_digit(s, amount):
    for el in s:
        if el.isdigit() and int(el) - amount < 10: return True
    return False

def transpose(amount, tab):
    res = list(map(list, zip(*tab)))
    
    for i in range(2, len(res)):
        for j in range(len(res[i])):
            if res[i][j].isdigit():
                number = res[i][j]
                if res[i + 1][j].isdigit():
                    number += res[i + 1][j]
                    res[i + 1][j] = '-'
                number = int(number) + amount
                if number < 0 or number > 22: return 'Out of frets!'
                res[i][j] = str(number)
    
    for i in range(2, len(res) * 2, 1):
        if i < len(res):
            if check_line_on_digits(res[i]):
                if check_line_on_two_digits(res[i]):
                    if check_was_one_digit(res[i], amount) and not check_was_two_digits(res[i], amount):
                        res.insert(i + 1, ['-', '-', '-', '-', '-', '-'])
                    for j in range(len(res[i])):
                        if len(res[i][j]) == 2:
                            res[i + 1][j] = res[i][j][1]
                            res[i][j] = res[i][j][0]
                else:
                    if check_was_two_digits(res[i], amount) and not check_was_one_digit(res[i], amount):
                        res.pop(i + 1)
        else:
            break
    
    return list(map(''.join, zip(*res)))
