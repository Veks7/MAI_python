'''
https://www.codewars.com/kata/5904be220881cb68be00007d/train/python
'''
def fish(shoal):
    l = [int(el) for el in shoal]
    l.sort()
    size = 1
    idx = 0
    capacity = 4
    cur = 0
    
    for el in l:
        if el <= size:
            cur += el
            if cur >= capacity:
                size += 1
                cur %= capacity
                idx += 1
                capacity += 4
        else:
            break
    
    print(l)
    
    return size
