'''
https://www.codewars.com/kata/588f3e0dfa74475a2600002a/train/python
'''
def possibilities(param):
    l = [param] * (2 ** param.count('?'))
    for i in range(len(l)):
        bin_str = bin(i)[2:].rjust(param.count('?'), '0')
        idx = 0
        l_str_i = list(l[i])
        for j in range(len(l_str_i)):
            if l_str_i[j] == '?':
                l_str_i[j] = bin_str[idx]
                idx += 1
        l[i] = ''.join(l_str_i)
    
    return l
