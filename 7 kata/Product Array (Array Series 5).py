'''
https://www.codewars.com//kata/5a905c2157c562994900009d
'''
import math
def product_array(numbers):
    productArray = [];
    for i in numbers:
        productArray.append(int(math.prod(numbers)/i))
    return productArray
print(product_array([12,20]), "==", [20,12])
print(product_array([3,27,4,2]), "==",[216,24,162,324])
print(product_array([13,10,5,2,9]), "==",[900,1170,2340,5850,1300])
print(product_array([16,17,4,3,5,2]), "==",[2040,1920,8160,10880,6528,16320])
