'''
https://www.codewars.com//kata/56a946cd7bd95ccab2000055
'''

def lowercase_count(strng):
    res = 0
    for symbol in strng:
        if symbol.islower():
            res += 1
    return res

print(lowercase_count("abc"), "==", 3)
print(lowercase_count("abcABC123"), "==", 3)
print(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), "==", 3)
print(lowercase_count(""), "==", 0)
print(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), "==", 0)
print(lowercase_count("abcdefghijklmnopqrstuvwxyz"), "==", 26)
