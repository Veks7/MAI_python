'''
https://www.codewars.com/kata/5a59e029145c46eaac000062/train/python
'''
def two_by_n(n, k):
    mass1 = [0, 0, 0]
    mass2 = [1, 0, 0]
    for _ in range(n):
        mass3 = [0, 0, 0]

        mass3[1] = mass2[0] * k + mass2[1] * (k-1) + mass2[2] * (k-2)
        mass3[2] = mass1[0] * k * (k-1)
        mass3[2] += mass1[1] * (k-1) * (k-2)
        mass3[2] += mass1[2] * (k-1)
        mass3[2] += mass1[2] * (k-2) * (k-2)

        mass3 = [x % 12345787 for x in mass3]
        mass1 = mass2
        mass2 = mass3

    return sum(mass2) % 12345787
