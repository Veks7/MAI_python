'''
https://www.codewars.com/kata/595120ac5afb2e5c1d000001/train/python
'''
def count_domains(domains, min_hits=0):
    d = {}
    l = domains.split('\n')
    for el in l:
        el = el.split('\t')
        if '.co.' not in el[0] and '.com.' not in el[0]:
            el[0] = '.'.join((el[0].split('.'))[-2::1])
        else:
            el[0] = '.'.join((el[0].split('.'))[-3::1])
        
        if el[0] not in d:
            d.update({el[0] : int(el[1])})
        else:
            d[el[0]] += int(el[1])
    
    res = []
    for el in d:
        if d[el] >= min_hits:
            res.append([el, d[el]])
    res.sort(key=lambda k: k[0])
    res.sort(reverse=True, key=lambda k: k[1])
    for el in res:
        el[1] = '(' + str(el[1]) + ')'
    
    return '\n'.join([' '.join(el) for el in res])
