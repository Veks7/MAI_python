'''
https://www.codewars.com/kata/58febc23627d2f48de000060/train/python
'''

import heapq

def closure_gen(*s):
    if 1 in s:
        yield 1
        s = [v for v in s if v != 1]
    if not s:
        return
    
    s = set(s)
    h = list(s)
    heapq.heapify(h)
    
    last = 1
    while True:
        cur = heapq.heappop(h)
        if cur == last: continue
        yield cur
        last = cur
        for v in s:
            heapq.heappush(h, cur * v)
