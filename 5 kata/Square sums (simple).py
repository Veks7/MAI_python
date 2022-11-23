'''
https://www.codewars.com/kata/5a6b24d4e626c59d5b000066/train/python
'''

from math import sqrt

def square_sums_row(n):
    counter = 1
    res = [1]
    unsuccess_res = set()
    while res[0] <= n and len(res) != n:
        # находим ближайшее число, которого еще нет
        while counter in res and counter <= n:
            counter += 1
        
        # флаг соответствующий тому, что был добавлен новый элемент в res
        added = False
        
        # пока не добавили число в res или не достигли n
        while counter <= n and not added:

            # если не выполняется условие для добавления числа в res
            if (int(sqrt(res[-1] + counter))) ** 2 != res[-1] + counter:
                # переходим к следующему
                counter += 1
            else:
                # если такого числа еще нет в res и не было такой ситуации
                if counter not in res and tuple(res + [counter]) not in unsuccess_res:
                    # добавляем counter в res
                    res.append(counter)
                    added = True
                else:
                    # иначе переходим к следующему числу
                    counter += 1
        
        # если counter не был добавлен
        if not added:
            # добавляем текущую ситуацию в список безуспешных вариантов развития событий
            unsuccess_res.add(tuple(res))
            counter = res.pop() + 1
            if not len(res):
                res.append(counter)
                counter = 1
        else:
            counter = 1
    
    return res if len(res) and res[0] <= n else False
