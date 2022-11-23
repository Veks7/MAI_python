'''
https://www.codewars.com/kata/5925138effaed0de490000cf/train/python
'''
def tiaosheng(failed_counter):
    time = 0
    jumps = 0
    
    while time < 60:
        jumps += 1
        if jumps in failed_counter:
            time += 3
        time += 1
    
    return jumps
