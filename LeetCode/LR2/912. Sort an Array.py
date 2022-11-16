"""
912. Sort an Array
"""

#Сортировка слиянием
def MergeSort(data):
    if len(data) <= 1:
        return data
    m = len(data) // 2
    part1 = MergeSort(data[:m])
    part2 = MergeSort(data[m:])
    mass = []
    i = 0
    j = 0
    while i < len(part1) and j < len(part2):
        if part1[i] < part2[j]:
            mass.append(part1[i])
            i += 1
        else:
            mass.append(part2[j])
            j += 1
    while i < len(part1):
        mass.append(part1[i])
        i += 1
    while j < len(part2):
        mass.append(part2[j])
        j += 1
    return p

#Разбиение быстрой сортировки
def QuickPart(data, mid):
    left = []
    m = []
    right = []
    for i in data:
        if i < data[mid]:
            left.append(i)
        elif i > data[mid]:
            right.append(i)
        else:
            m.append(i)

    return QuickSort(left), m, QuickSort(right)

#Сортировка подсчетом
def CountingSort(self, data):
    max_k = max(data)
    min_k = min(data)
    l = [0] * (max_k - min_k + 1)
    for i in data:
        l[i - min_k] += 1
    result = []
    for i in range(len(l)):
        if l[i] > 0:
            result += [i + min_k] * l[i]

    return result

#Быстрая сортировка
def QuickSort(data):
    if len(data) <= 1:
        return data
    elif len(data) == 2 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]
        return data

    mid = len(data) // 2

    left, middle, right = QuickPart(data, mid)

    return left + middle + right

class Solution:
    def sortArray(self, nums):
        # return MergeSort(nums)
        # return CountingSort(nums)
        # return QuickSort(nums)
        pass
