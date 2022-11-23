'''
https://www.codewars.com/kata/5aa67541373c2e69a20000c9/train/python
'''
def check_winner(l):
    if l[0][0][0] == l[1][1][1] == l[2][2][2] == l[3][3][3] and l[0][0][0] in ['X', 'O']:
        return l[0][0][0]
    if l[0][3][0] == l[1][2][1] == l[2][1][2] == l[3][0][3] and l[0][3][0] in ['X', 'O']:
        return l[0][3][0]
    if l[0][0][3] == l[1][1][2] == l[2][2][1] == l[3][3][0] and l[0][0][3] in ['X', 'O']:
        return l[0][0][3]
    if l[3][0][0] == l[2][1][1] == l[1][2][2] == l[0][3][3] and l[3][0][0] in ['X', 'O']:
        return l[3][0][0]
    
    for i in range(len(l)):
        if l[0][0][i] == l[1][1][i] == l[2][2][i] == l[3][3][i] and l[0][0][i] in ['X', 'O']:
            return l[0][0][i]
        if l[0][i][0] == l[1][i][1] == l[2][i][2] == l[3][i][3] and l[0][i][0] in ['X', 'O']:
            return l[0][i][0]
        if l[i][0][0] == l[i][1][1] == l[i][2][2] == l[i][3][3] and l[i][0][0] in ['X', 'O']:
            return l[i][0][0]
        
        if l[i][0][3] == l[i][1][2] == l[i][2][1] == l[i][3][0] and l[i][0][3] in ['X', 'O']:
            return l[i][0][3]
        if l[0][i][3] == l[1][i][2] == l[2][i][1] == l[3][i][0] and l[0][i][3] in ['X', 'O']:
            return l[0][i][3]
        if l[0][3][i] == l[1][2][i] == l[2][1][i] == l[3][0][i] and l[0][3][i] in ['X', 'O']:
            return l[0][3][i]
        
        for j in range(len(l[i])):
            if l[i][j][0] == l[i][j][1] == l[i][j][2] == l[i][j][3] and l[i][j][0] in ['X', 'O']:
                return l[i][j][0]
            if l[j][0][i] == l[j][1][i] == l[j][2][i] == l[j][3][i] and l[j][0][i] in ['X', 'O']:
                return l[j][0][i]
            if l[0][i][j] == l[1][i][j] == l[2][i][j] == l[3][i][j] and l[0][i][j] in ['X', 'O']:
                return l[0][i][j]
    
    return None


def play_OX_3D(moves):
    if len(moves) < 7:
        return "No winner"
    match = []
    for i in range(4):
        match.append([])
        for j in range(4):
            match[i].append(['-', '-', '-', '-'])
    
    for i in range(len(moves)):
        match[moves[i][0]][moves[i][1]][moves[i][2]] = 'X' if i % 2 else 'O'
        
        if i >= 6:
            winner = check_winner(match)
            if winner:
                return f'{winner} wins after {i + 1} moves'
    
    return 'No winner'
