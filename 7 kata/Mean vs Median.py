'''
https://www.codewars.com//kata/5806445c3f1f9c2f72000031
'''

import statistics
def mean_vs_median(numbers):
    if statistics.mean(numbers) > statistics.median(numbers):
        return 'mean'
    elif statistics.mean(numbers) < statistics.median(numbers):
        return 'median'
    else:
        return 'same'



print("[1, 1, 1]")
print(mean_vs_median([1, 1, 1]), "==", "same")

print("[1, 2, 37]")
print(mean_vs_median([1, 2, 37]), "==", "mean")

print("[7, 14, -70]")
print(mean_vs_median([7, 14, -70]), "==", "median")

print("[-10, 20, 5]")
print(mean_vs_median([-10, 20, 5]), "==", 'same')
