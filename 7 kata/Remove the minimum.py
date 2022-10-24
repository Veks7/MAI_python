'''
https://www.codewars.com//kata/563cf89eb4747c5fb100001b
'''
def remove_smallest(numbers):
    if len(numbers) == 0:
        return numbers
    else:
        numbers_copy = list(numbers)
        numbers_copy.remove(min(numbers))
        return  numbers_copy

print(remove_smallest([1, 2, 3, 4, 5]), "==", [2, 3, 4, 5], "Result for [1, 2, 3, 4, 5]")
print(remove_smallest([5, 3, 2, 1, 4]), "==", [5, 3, 2, 4], "Result for [5, 3, 2, 1, 4]")
print(remove_smallest([1, 2, 3, 1, 1]), "==", [2, 3, 1, 1], "Result for [1, 2, 3, 1, 1]")
print(remove_smallest([]), [], "Result for []")
