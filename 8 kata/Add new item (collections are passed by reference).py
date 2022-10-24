'''
https://www.codewars.com//kata/566dc05f855b36a031000048
'''
def add_extra(list_of_numbers):
    return list_of_numbers + [7]

print(len(add_extra([1,2])), "==", 3)
print(len(add_extra([])), "==", 1)
