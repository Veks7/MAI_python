'''
https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/python
'''
def rev_rot(strng, sz):
    # если на входе невалидные данные
    if sz <= 1 or len(strng) == 0 or sz > len(strng):
        return ''
    
    s = strng[:(len(strng) // sz) * sz]
    l = []
    
    for i in range(0, len(s), sz):
        slice = list(s[i: i + sz])
        summ = 0
        for c in slice:
            summ += int(c)
        # если сумма цифр нечетная, перемещаем элементы слайса влево
        if summ % 2:
            for j in range(len(slice) - 1):
                slice[j - 1], slice[j] = slice[j], slice[j - 1]
        # иначе - переворачиваем слайс
        else:
            for j in range(len(slice) // 2):
                slice[j], slice[len(slice) - 1 - j] = slice[len(slice) - 1 - j], slice[j]
        
        l += slice
    
    return ''.join(l)

s = "733049910872815764"
print(rev_rot(s, 5), "330479108928157")
