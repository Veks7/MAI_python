'''
https://www.codewars.com//kata/56b97b776ffcea598a0006f2
'''

def bubblesort_once(l):
    res = l.copy()
    for i in range(0, len(res)-1):
        if res[i] > res[i+1]:
            res[i], res[i+1] = res[i+1], res[i]
    return res

print(bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]), "==", [7, 5, 3, 1, 2, 4, 6, 8, 9])
