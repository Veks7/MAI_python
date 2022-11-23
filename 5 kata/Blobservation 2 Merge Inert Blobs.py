'''
https://www.codewars.com/kata/5f8fb3c06c8f520032c1e091/train/python
'''
class Blobservation:
    def __init__(self,matrix):
        self.matrix = matrix
        self.instructions = ''


    def read(self,instructions):
        self.instructions += instructions


    def state(self):
        # переводим в матрицу для удобства работы
        return_matrix = list(self.matrix)
        for i in range(len(return_matrix)):
            return_matrix[i] = list(return_matrix[i])
        
        # для каждого направления в инструкциях делаем следующее
        for x in self.instructions:
            # если встречаем 'S' или 'N', то транспонируем матрицу
            if x == 'S' or x == 'N':
                return_matrix = list(map(list, zip(*return_matrix)))
            
            # считаем значения элементов
            c = 1 if x == 'E' or x == 'S' else -1
            for i in range(len(return_matrix)):
                left, right = (0, len(return_matrix[i])) if x == 'E' or x == 'S' else (len(return_matrix[i]) - 1, -1)
                for j in range(left, right, c):
                    counter = 1
                    s = return_matrix[i][j]
                    prev = return_matrix[i][j]
                    if prev != 0:
                        while j + counter * c != right:
                            if prev < return_matrix[i][j + counter * c]:
                                prev = return_matrix[i][j + counter * c]
                                s += prev
                                return_matrix[i][j + counter * c] = 0
                                counter += 1
                            elif return_matrix[i][j + counter * c] == 0:
                                counter += 1
                                continue
                            else:
                                break
                        return_matrix[i][j] = s
            
            # перемещенаем нули в нужную сторону
            for i in range(len(return_matrix)):
                for j in range(left, right, c):
                    if return_matrix[i][j] == 0:
                        return_matrix[i].insert(left, return_matrix[i].pop(j))
            
            # удаляем нулевые строки
            return_matrix = self.delete_null_str(return_matrix)
            
            # переворачиваем для устранения нулевых столбцов
            return_matrix = list(map(list, zip(*return_matrix)))
            
            # удаляем нулевые строки
            return_matrix = self.delete_null_str(return_matrix)
            
            # переворачиваем в изначальный вид матрицы
            if x == 'E' or x == 'W':
                return_matrix = list(map(list, zip(*return_matrix)))
        
        # возвращаем кортежи на места списков
        for i in range(len(return_matrix)):
            return_matrix[i] = tuple(return_matrix[i])
        return_matrix = tuple(return_matrix)
        return return_matrix
    
    
    def delete_null_str(self, return_matrix):
        for i in range(len(return_matrix) - 1, -1, -1):
            s = 0
            for j in range(len(return_matrix[i])):
                s += abs(return_matrix[i][j])
            if not s:
                return_matrix.pop(i)
        return return_matrix
