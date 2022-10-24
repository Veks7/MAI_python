'''
https://www.codewars.com//kata/52829c5fe08baf7edc00122b
'''
def number_of_occurrences(element, sample):
    res = sample.count(element)
    return(res)
sample = [0, 1, 2, 2, 3]
print(number_of_occurrences(0, sample), "==", 1)
print(number_of_occurrences(4, sample), "==", 0)
print(number_of_occurrences(2, sample), "==", 2)
print(number_of_occurrences(3, sample), "==", 1)
