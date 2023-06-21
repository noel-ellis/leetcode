import copy


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        sectors = [[], [], [], [], [], [], [], [], []]
        for i in range(0, n):
            sector_row = i // 3
            numbers_in_row = []
            numbers_in_column = []
            for j in range(0, n):
                # checking elements in a column
                if board[j][i] != '.':
                    if board[j][i] in numbers_in_column:
                        return False
                    numbers_in_column.append(board[j][i])

                if board[i][j] == '.':
                    continue
                # checking elements in a row
                if board[i][j] in numbers_in_row:
                    return False
                numbers_in_row.append(board[i][j])

                # checking elements in a sector
                sector_column = j // 3
                sector_number = 2*sector_row + (sector_row+sector_column)
                if board[i][j] in sectors[sector_number]:
                    return False
                sectors[sector_number].append(board[i][j])

        return True


def tests():
    return {'board':
            [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]},  {'board': [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]}, {'board': [[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."], [".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."], [".", ".", "4", ".", ".", ".", ".", ".", "."]]}


def main():
    solution = Solution()
    include_tests = [0, 1, 2]
    for num, test in enumerate(tests()):
        if num in include_tests:
            print(
                f'==============\ntest {num}: {test}\nresult {num}: {solution.isValidSudoku(**test)}\n')


main()
