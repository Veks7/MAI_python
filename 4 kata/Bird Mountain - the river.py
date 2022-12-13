'''
https://www.codewars.com//kata/5c2fd9188e358f301f5f7a7b
'''
def peak_height(mountain):
    counter = 0
    peaks = 0
    
    next = []
    if len(mountain):
        next = mountain.copy()
        for i in range(len(next)):
            next[i] = list(next[i])
        
        prev = [0] * len(next)
        for i in range(len(prev)):
            prev[i] = next[i].copy()
        
        while counter < min(len(mountain), len(mountain[0])):
            counter += 1
            for i in range(counter - 1, len(prev) - counter + 1):
                for j in range(counter - 1, len(prev[i]) - counter + 1):
                    if prev[i][j] == '^':
                        peaks = counter
                        if i == counter - 1 or i == len(prev) - counter:
                            next[i][j] = str(counter)
                        elif j == counter - 1 or j == len(prev[i]) - counter:
                            next[i][j] = str(counter)
                        else:
                            if prev[i - 1][j] in ' -' or prev[i][j - 1] in ' -' or prev[i + 1][j] in ' -' or prev[i][j + 1] in ' -':
                                next[i][j] = str(counter)
                            elif prev[i - 1][j].isdigit() or prev[i][j - 1].isdigit() or prev[i + 1][j].isdigit() or prev[i][j + 1].isdigit():
                                next[i][j] = str(counter)
            
            for i in range(len(prev)):
                prev[i] = next[i].copy()
            for i in range(len(next)):
                next[i] = prev[i].copy()
    
    return next


def wet_ground(terrain, day):
    counter = 0
    
    next = []
    if len(terrain):
        next = terrain.copy()
        for i in range(len(next)):
            next[i] = list(next[i])
        
        while counter < len(terrain) * len(terrain[0]):
            counter += 1
            for i in range(len(next)):
                for j in range(len(next[i])):
                    if next[i][j] in day:
                        if i == 0:
                            if next[i + 1][j] == '-': next[i][j] = '-'
                            if j > 0 and next[i][j - 1] == '-':                  next[i][j] = '-'
                            elif j < len(next[i]) - 1 and next[i][j + 1] == '-': next[i][j] = '-'
                        elif j == 0:
                            if next[i][j + 1] == '-': next[i][j] = '-'
                            if i > 0 and next[i - 1][j] == '-':                  next[i][j] = '-'
                            elif i < len(next) - 1 and next[i + 1][j] == '-':    next[i][j] = '-'
                        elif i == len(next) - 1:
                            if next[i - 1][j] == '-': next[i][j] = '-'
                            if j > 0 and next[i][j - 1] == '-':                  next[i][j] = '-'
                            elif j < len(next[i]) - 1 and next[i][j + 1] == '-': next[i][j] = '-'
                        elif j == len(next[i]) - 1:
                            if next[i][j - 1] == '-': next[i][j] = '-'
                            if i > 0 and next[i - 1][j] == '-':                  next[i][j] = '-'
                            elif i < len(next) - 1 and next[i + 1][j] == '-':    next[i][j] = '-'
                        else:
                            if next[i - 1][j] in '-' or next[i][j - 1] in '-' or next[i + 1][j] in '-' or next[i][j + 1] in '-':
                                next[i][j] = '-'
    return next


def execute_day(with_water, day):
    # day 1
    count_minus = 0
    with_water = wet_ground(with_water, day)
    for i in range(len(with_water)):
        count_minus += with_water[i].count('-')
    return len(with_water) * len(with_water[0]) - count_minus


def dry_ground(terrain):
    day_0, day_1, day_2, day_3 = 0, 0, 0, 0
    if len(terrain):
        with_water = peak_height(list(terrain))
        count_minus = 0
        
        for i in range(len(with_water)):
            count_minus += with_water[i].count('-')
        
        day_0 = len(terrain) * len(terrain[0]) - count_minus
        day_1 = execute_day(with_water, ' ')
        day_2 = execute_day(with_water, ' 1')
        day_3 = execute_day(with_water, ' 12')
    
    return day_0, day_1, day_2, day_3


def launch_test(mountain):
    print(dry_ground(mountain))


if __name__ == '__main__':
    launch_test([
          "  ^^^^^^             ",
            "^^^^^^^^       ^^^   ",
            "^^^^^^^  ^^^         ",
            "^^^^^^^  ^^^         ",
            "^^^^^^^  ^^^         ",
            "---------------------",
            "^^^^^                ",
            "   ^^^^^^^^  ^^^^^^^ ",
            "^^^^^^^^     ^     ^ ",
            "^^^^^        ^^^^^^^ "
                ])
    # launch_test([])
