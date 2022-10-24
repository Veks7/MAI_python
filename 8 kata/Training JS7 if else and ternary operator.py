'''
https://www.codewars.com//kata/57202aefe8d6c514300001fd
'''
def sale_hotdogs(n):
    if n < 5:       return n * 100
    elif n >= 10: return n * 90
    else:           return n * 95

print(sale_hotdogs(0))
print(sale_hotdogs(1))
print(sale_hotdogs(2))
print(sale_hotdogs(3))
print(sale_hotdogs(4))
print(sale_hotdogs(5))
print(sale_hotdogs(9))
print(sale_hotdogs(10))
print(sale_hotdogs(11))
print(sale_hotdogs(100))
