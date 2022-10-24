'''
https://www.codewars.com//kata/5b73fe9fb3d9776fbf00009e
'''
def sum_of_differences(arr):
    if len(arr) == 0:
        return 0
    else:
        return max(arr) - min(arr)
print(sum_of_differences([1, 2, 10]),"==", 9)
print(sum_of_differences([-3, -2, -1]), "==",2)
print(sum_of_differences([1, 1, 1, 1, 1]), "==",0)
print(sum_of_differences([-17, 17]), "==",34)      
print(sum_of_differences([]), "==",0)
print(sum_of_differences([0]), "==",0)
print(sum_of_differences([-1]), "==",0)
print(sum_of_differences([1]), "==",0)
