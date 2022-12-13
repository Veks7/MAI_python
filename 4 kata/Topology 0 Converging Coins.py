'''
https://www.codewars.com/kata/5f5bef3534d5ad00232c0fa8/train/python
'''
def fingerprint(s):
    # Finger print for a set of locations
    return sum(2 << x for x in s)

def converge(r, u1, u2, u3):
    if u1 == u2 == u3:
        return 0

    locations = [{u1}, {u2}, {u3}]
    seen = set()
    moves = 0
    while True:
        moves += 1
        new_locations = [
            {n for node in node_set for n in r[node]}
            for node_set in locations
        ]
        
        if new_locations[0].intersection(new_locations[1].intersection(new_locations[2])):
            # Solved
            return moves
        
        key = tuple(map(fingerprint, new_locations))
        if key in seen:
            # No solution possible, we've been in this position before
            return None

        # Set up for next cycle
        seen.add(key)
        locations = new_locations
    
    return None
