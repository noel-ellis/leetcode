class Solution:
    def make_pyramid(n: int, m: int):
        for i in range(0, n):
            pass

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        m = 1
        pyramid = self.make_pyramid(n, m)
        pyramid = self.cut_pyramid(pyramid, index)
        sum = self.sum_pyramid(pyramid)
        m += 1

        while sum <= maxSum:
            old_pyramid = pyramid[:]
            pyramid = self.make_pyramid(n, m)
            pyramid = self.cut_pyramid(pyramid, index)
            sum = self.sum_pyramid(pyramid)
            m += 1

        return old_pyramid[index]


def tests():
    return {'n': 4, 'index': 2, 'maxSum': 6}, {'n': 6, 'index': 1, 'maxSum': 10},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.nextGreatestLetter(**test)}\n')


main()
