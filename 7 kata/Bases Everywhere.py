'''
https://www.codewars.com//kata/5f47e79e18330d001a195b55
'''
def base_finder(seq):
    max = 0
    if len(seq) == 1:
        return max + int(seq[0])
    else:
        for num in seq:
            for i in num:
                res = int(i)
                if max < res:
                    max = res
        return max + 1
print(base_finder(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']), "==", 10)
print(base_finder(['1', '2', '3', '4', '5', '6', '10', '11', '12', '13']), "==", 7)
