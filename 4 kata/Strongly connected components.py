'''
https://www.codewars.com/kata/5f74a3b1acfbb20033e5b7d9/train/python
'''
from itertools import groupby
from collections import defaultdict

def strongly_connected_components(graph):
    def dfs(cur_node, stack, low, disc, in_stack):
        
        nonlocal level
        
        stack.append(cur_node)
        checked.add(cur_node)
        in_stack[cur_node] = 1
        disc[cur_node] = low[cur_node] = (level := level + 1)
        
        for el in graph[cur_node]:    
            if el not in checked:
                dfs(el, stack, low, disc, in_stack)
            if in_stack[el]:
                low[cur_node] = min(low[cur_node], low[el])

        if disc[cur_node] == low[cur_node]:
            while True:
                in_stack[(el := stack.pop())] = 0
                low[el] = low[cur_node]
                if el == cur_node:
                    break
    
    low, disc, level, checked = dict(), dict(), -1, set()
    
    for i in range(len(graph)):
        if i not in checked:
            dfs(i, list(), low, disc, defaultdict(int))

    return [set(j) for _, j in groupby(sorted(low, key=lambda x: low[x]), key=lambda x: low[x])]
