'''
https://www.codewars.com/kata/561f18d45df118e7c400000b/train/python
'''
from itertools import combinations

error_1 = "Error. Unexpected entries"
error_2 = "Error. Number of factors too high"
error_3 = "Error. Number of addens too high"


def factorial(a):
    return 1 if a == 0 else a * factorial(a - 1)


def find_combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def check_error(arr, num_fact, num_add, max_val):
    # проверка на первую ошибку
    for el in arr:
        if type(el) is not type(1):
            return error_1
    for el in [type(num_fact), type(num_add), type(max_val)]:
        if el is not type(1):
            return error_1
    if num_fact <= 0 or num_add <= 0 or max_val <= 0:
        return error_1
    
    # проверка на вторую ошибку
    if num_fact > len(arr):
        return error_2
    
    # проверка на третью ошибку
    if num_add > find_combinations(len(arr), num_fact):
        return error_3
    
    return ''


def eval_prod_sum(arr, num_fact, num_add, max_val):
    s_err = check_error(arr, num_fact, num_add, max_val) 
    if len(s_err):
        return s_err
    
    comb_prods = combinations(arr, num_fact)
    l = list(comb_prods)
    for i in range(len(l)):
        p = 1
        for el in l[i]:
            p *= el
        l[i] = p
    print(l)
    
    comb_adds = combinations(l, num_add)
    l_adds = list(comb_adds)
    
    smaller, equal, larger = 0, 0, 0
    
    for i in range(len(l_adds)):
        s = 0
        for el in l_adds[i]:
            s += el
        l_adds[i] = s
        if l_adds[i] < max_val: smaller += 1
        elif l_adds[i] == max_val: equal += 1
        else: larger += 1
    
    
    return [{f"Below than {max_val}" : smaller},
            {f"Equals to {max_val}"  : equal},
            {f"Higher than {max_val}": larger}]
