from typing import List


class Solution:
    """
    Solutions
    """
    def rotate(self, matrix):
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
        
    # def rotate(self, matrix):
    #     matrix[:] = zip(*matrix[::-1])
    
    # def rotate(self, matrix):
    #     n = len(matrix)
    #     for i in range(n/2):
    #         for j in range(n-n/2):
    #             matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
    #                      matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

    # def rotate(self, matrix):
    #     matrix[:] = map(list, zip(*matrix[::-1]))
    
    
    # def rotate(self, matrix):
    #     n = len(matrix)
    #     for i in range(n/2):
    #         for j in range(n-n/2):
    #             for _ in '123':
    #                 matrix[i][j], matrix[~j][i], i, j = matrix[~j][i], matrix[i][j], ~j, ~i
    #             i = ~j

    # def rotate(self, matrix):
    #     matrix.reverse()
    #     for i in range(len(matrix)):
    #         for j in range(i):
    #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    #
    # MY CODE

    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     dimensional_size = len(matrix)
    #     iteration = 0
    #     while dimensional_size > 1:
    #         Solution.image_iteration(matrix, dimensional_size, iteration)
    #         dimensional_size -= 2
    #         iteration += 1
    #     print('FINmatrixL MmatrixTRIX: ', matrix)
    
    # @classmethod
    # def image_iteration(cls, matrix, dimensional_size, iteration):
    #     SUBSTITUTION_LIMIT = 4
    #     initial_position = [iteration, iteration]
    #     final_value = 0
    #     init_value = matrix[initial_position[0]][initial_position[1]]
    #     for rotate_index in range(0, SUBSTITUTION_LIMIT):
    #         for new_index in range(0, dimensional_size):
    #             final_x, final_y = Solution.get_substitution_positions(rotate_index, new_index, dimensional_size, iteration)
    #             final_value = matrix[final_x][final_y]
    #             matrix[final_x][final_y] = init_value
    #             init_value = final_value
    #         rotate_index += 1
                

    # @classmethod
    # def get_substitution_positions(cls, index, new_index, dimensional_size, iteration) -> List[int]:
    #     positions = []
    #     start_index = iteration
    #     end_index = dimensional_size - iteration - 1
    #     if index == 0:
    #         positions = [start_index + new_index, end_index]
    #     elif index == 1:
    #         positions = [end_index, end_index - new_index]
    #     elif index == 2:
    #         positions =  [end_index - new_index, start_index]
    #     elif index == 3:
    #         positions = [start_index, start_index + new_index]
    #     return positions
    