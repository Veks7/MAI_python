'''
https://www.codewars.com/kata/58e6d83e19af2cb8840000b5/train/python
'''
def attack(start, dest, obstacles):
    all_points = (start, dest) + obstacles
    min_x = min(p[0] for p in all_points) - 3
    min_y = min(p[1] for p in all_points) - 3
    max_x = max(p[0] for p in all_points) + 3
    max_y = max(p[1] for p in all_points) + 3
    n = (sum(start) + sum(dest)) % 2
    start = {start}
    dest = {dest}
    dest_path = set(), dest
    if n:
        start_path = start, set()
        start = moves(start).difference(obstacles)
        start_path[1].update(start)
    else:
        start_path = set(), start
    pi = 0
    while not start.intersection(dest):
        if not start or not dest: return None
        start = set((x,y) for (x,y) in moves(start) if x>min_x and x<max_x and y>min_y and y<max_y)
        start.difference_update(obstacles)
        start.difference_update(start_path[pi])
        start_path[pi].update(start)
        dest = set((x,y) for (x,y) in moves(dest) if x>min_x and x<max_x and y>min_y and y<max_y)
        dest.difference_update(obstacles)
        dest.difference_update(dest_path[pi])
        dest_path[pi].update(dest)
        n += 2
        pi ^= 1
    return n

def moves(start=((0,0),)):
    m = set()
    for x, y in start:
        m.update({(x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1),(x+1,y+2),(x-1,y+2),(x+1,y-2),(x-1,y-2)})
    return m
