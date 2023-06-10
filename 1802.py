class Solution:
    def left_side(n: int, m: int, index: int):
        pass

    def right_side(n: int, m: int, index: int):
        pass

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        m = 1
        pyramid = self.left_side(n, m, index).append(
            m).append(self.right_side(n, m, index))
        sum = self.sum_pyramid(pyramid)
        m += 1

        while sum <= maxSum:
            old_pyramid = pyramid[:]
            pyramid = self.left_side(n, m, index).append(
                m).append(self.right_side(n, m, index))
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
