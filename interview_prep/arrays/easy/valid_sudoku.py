from typing import List
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.area_size: int = 3
        self.rows_checked = []
        self.columns_checked = []
        self.areas_checked = []
        self.board = board
        rows, columns = len(board), len(board[:])
        for row_index in range(0, rows):
            for col_index in range(0, columns):
                value = board[row_index][col_index]
                if value != ".":
                    is_duplicate_in_area = self.check_3x3_area(row_index, col_index)
                    if is_duplicate_in_area:
                        return False
                    is_duplicate_in_row = self.check_row(row_index)
                    if is_duplicate_in_row:
                        return False
                    is_duplicate_in_col = self.check_column(col_index)
                    if is_duplicate_in_col:
                        return False
        return True

    @classmethod
    def check_counter(cls, counter):
        most_common = counter.most_common(2)
        for element, value in most_common:
            if element != "." and value > 1:
                return True
        return False

    def check_3x3_area(self, row_index, col_index):
        correspondent_3x3 = [int(row_index/3), int(col_index/3)]
        if correspondent_3x3 in self.areas_checked:
            return False
        x, y = correspondent_3x3
        area = []
        for row in self.board[x*3:(x+1)*3]:
            area += row[y*3:(y+1)*3]
        counter = Counter(area)
        self.areas_checked.append(correspondent_3x3)
        return Solution.check_counter(counter)
        

    def check_row(self, row_index):
        if row_index in self.rows_checked:
            return False
        counter = Counter(self.board[row_index])
        self.rows_checked.append(row_index)
        return Solution.check_counter(counter)


    def check_column(self, col_index):
        if col_index in self.columns_checked:
            return False
        counter = Counter([row[col_index] for row in self.board] )
        self.columns_checked.append(col_index)
        return Solution.check_counter(counter)
        