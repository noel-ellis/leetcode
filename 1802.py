class Solution:
    def left_side(self, m: int, index: int):
        array = []
        for _ in range(index-1, -1, -1):
            if m > 1:
                m -= 1
            array.append(m)
        return array[::-1]

    def right_side(self, n: int, m: int, index: int):
        array = []
        for _ in range(index+1, n):
            if m > 1:
                m -= 1
            array.append(m)
        return array

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        array = [0]
        m = 0
        while sum(array) <= maxSum:
            m += 1
            array = self.left_side(m, index) + \
                [m] + self.right_side(n, m, index)
        return m-1


def tests():
    return {'n': 4, 'index': 2, 'maxSum': 6}, {'n': 6, 'index': 1, 'maxSum': 10}, {'n': 10, 'index': 5, 'maxSum': 10},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.maxValue(**test)}\n')


main()
