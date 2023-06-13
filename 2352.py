import copy


class Solution:
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

    def equalPairs(self, grid: list[list[int]]) -> int:
        transposed_grid = self.transpose_grid(grid)

        n = len(grid[0])
        counter = 0
        for i in range(0, n):
            for j in range(0, n):
                if grid[i] == transposed_grid[j]:
                    counter += 1

        return counter


def tests():
    return {'grid': [[3, 2, 1], [1, 7, 6], [2, 7, 7]], }, {'grid': [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], },


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.equalPairs(**test)}\n')


main()
