'''
https://www.codewars.com//kata/580dda86c40fa6c45f00028a
'''
def cube_odd(arr):
    res = 0
    for i in arr:
        if type(i) != int:
            return None
        elif i%2 == 1:
            res+=i**3
    return res

print(cube_odd([1, 2, 3, 4]), "==", 28)
print(cube_odd([-3,-2,2,3]), "==", 0)
print(cube_odd(["a",12,9,"z",42]), "==", None)
