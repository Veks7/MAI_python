'''
https://www.codewars.com/kata/59eb1e4a0863c7ff7e000008/train/python
'''
import functools
def solve(s,ops):
    print(solver(s, ops, 't'))
    return solver(s, ops, 't')

d = {'t&' : [('t', 't')], 'f&' : [('t', 'f'), ('f', 't'), ('f', 'f')], 't|':[('t', 't'), ('t', 'f'), ('f', 't')], 'f|': [('f', 'f')],
    't^':[('t', 'f'), ('f', 't')], 'f^':[('t', 't'), ('f', 'f')]}

@functools.cache
def solver(s, ops, ev):
    if ops == "" and s==ev:
        return 1
    elif ops == "" and s!=ev:
        return 0
    else:
        sum1 = 0
        for i in range(len(ops)):
            opr = ev+ops[i]
            for j in d[opr]:
                sum1 += solver(s[:1+i], ops[:i], j[0]) * solver(s[i+1:], ops[i+1:], j[1])
        return sum1
