'''
https://www.codewars.com/kata/58a2a561f749ed763c00000b/train/python
'''
def cowboys_dollars(boots):    
    return f"This Rhinestone Cowboy has {boots[1][:77].count('[(1)]')} dollar bills in his right boot and {boots[0][:77].count('[(1)]')} in the left"
