'''
https://www.codewars.com//kata/51fda2d95d6efda45e00004e
'''
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
    
    def inc_progress(self, solved):
        try:
            if solved < -8 or solved > 8 or solved == 0:
                print(1 / 0)
        except:
            raise
        if self.rank < 0 and solved > 0:
            self.progress += 10 * (solved - self.rank - 1) ** 2
        elif self.rank < solved:
            self.progress += 10 * (solved - self.rank) ** 2
        elif self.rank - solved == 1 or self.rank == 1 and solved == -1:
            self.progress += 1
        elif self.rank - solved > 1:
            self.progress += 0
        elif self.rank == solved:
            self.progress += 3
        if self.progress >= 100:
            rank_update = self.progress // 100
            if self.rank < 0 and rank_update + self.rank >= 0:
                self.rank = min(8, rank_update + self.rank + 1)
            elif self.rank > 0:
                self.rank = min(8, rank_update + self.rank)
            else:
                self.rank += rank_update
            self.progress %= 100
        if self.rank == 8:
            self.progress = 0


if __name__ == '__main__':
    user = User()
    print(user.rank, '==', -8)
    print(user.progress, '==', 0)
    user.inc_progress(-7)
    print(user.progress, '==', 10)
    user.inc_progress(-5)
    print(user.progress, '==', 0)
    print(user.rank, '==', -7)
