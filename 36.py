import copy


class Solution:
    def divide_in_sectors(self, grid: list[list[int]]) -> list[list[int]]:
        sectors = [[], [], [], [], [], [], [], [], []]
        for i, row in enumerate(grid):
            x = i // 3
            for j, element in enumerate(row):
                y = j // 3
                z = 2 * x + (x + y)
                sectors[z].append(element)

        return sectors

    def transpose_grid(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid[0])
        transposed_grid = copy.deepcopy(grid)
        for i in range(0, n):

            if i == n-1:
                break

            for j in range(i+1, n):
                transposed_grid[j][i] = grid[i][j]
                transposed_grid[i][j] = grid[j][i]

        return transposed_grid

    def check_rows(self, board: list[list[str]]) -> bool:
        for row in board:
            numbers_in_row = []
            for element in row:
                if element == '.':
                    continue
                if element in numbers_in_row:
                    return False
                numbers_in_row.append(element)

        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        if not self.check_rows(board):
            return False

        transposed_board = self.transpose_grid(board)
        if not self.check_rows(transposed_board):
            return False

        sectors = self.divide_in_sectors(board)
        if not self.check_rows(sectors):
            return False

        return True


def tests():
    return {'board':
            [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]},  {'board': [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]}, {'board': [[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."], [".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."], [".", ".", "4", ".", ".", ".", ".", ".", "."]]}


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\ntest {num}: {test}\nresult {num}: {solution.isValidSudoku(**test)}\n')


main()
