'''
https://www.codewars.com/kata/56121f3312baa28c8500005b/train/python
'''
# нахождение НОК
def calculate_lcm(x, y):
    if x > y: greater = x
    else:     greater = y
    flag = False
    while not flag:
        if (greater % x == 0) and (greater % y == 0):
            NOK = greater
            flag = True
        else: greater += 1
    return NOK

def biggest(nums):
    for i in range(len(nums)):
        nums[i] = str(nums[i])

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            min_length = calculate_lcm(len(nums[i]), len(nums[j]))

            if nums[i] * (min_length // len(nums[i])) < nums[j] * (min_length // len(nums[j])):
                nums[i], nums[j] = nums[j], nums[i]

    return str(int(''.join(nums)))
