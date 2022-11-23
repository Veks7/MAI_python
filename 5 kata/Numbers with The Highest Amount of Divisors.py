'''
https://www.codewars.com/kata/55ef57064cb8418a3f000061/train/python
'''
def find_divisors(number):
    if number == 1:
        return 1
    res = [1]
    
    for i in range(2, number // 2 + 1):
        if not (number % i):
            res.append(i)
    
    return len(res) + 1


def proc_arrInt(listNum):
    d = {}
    res = [len(listNum), 0, [0, []]]
    max_divisors = 0
    
    for el in listNum:
        quantity_divs = find_divisors(el)
        max_divisors = max(max_divisors, quantity_divs)
        d.update({ el : quantity_divs })
        if quantity_divs == 2:
            res[1] += 1
    
    res[2][0] = max_divisors
    
    for el in d:
        if d[el] == max_divisors:
            res[2][1].append(el)
    res[2][1].sort()
    
    return res
