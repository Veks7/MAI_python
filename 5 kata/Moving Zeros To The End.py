'''
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
'''
def move_zeros(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == 0:
            lst.append(lst.pop(i))
    
    return lst
