'''
https://www.codewars.com/kata/55a243393fb3e87021000198/train/python
'''
def remember(str_):
    d = {}
    res = []
    for el in str_:
        if el not in d:
            d.update( { el : 0 } )
        elif el not in res:
            res.append(el)
    
    return res
