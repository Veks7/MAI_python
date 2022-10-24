'''
https://www.codewars.com//kata/56bf3287b5106eb10f000899
'''
def move_vowels(input): 
    left_arr =[]
    right_arr = []
    for i in input:
        if i in 'aeiou':
            right_arr.append(i)
        else:
            left_arr.append(i)
    return "".join(left_arr + right_arr)
print(move_vowels('day'), "==", 'dya')
print(move_vowels('apple'), "==", 'pplae')
print(move_vowels('peace'), "==", 'pceae')
print(move_vowels('maker'), "==", 'mkrae')
print(move_vowels('programming'), "==", 'prgrmmngoai')
print(move_vowels('javascript'), "==", 'jvscrptaai')
print(move_vowels('python'), "==", 'pythno')
print(move_vowels('ruby'), "==", 'rbyu')
print(move_vowels('haskell'), "==", 'hskllae')
print(move_vowels('clojure'), "==", 'cljroue')
print(move_vowels('csharp'), "==", 'cshrpa')
