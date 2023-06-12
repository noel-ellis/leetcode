class Solution:
    # try new approach: ditch while loop, choose a right starting point

    def sum_of_series(self, m: int):
        return (m * (m + 1)) // 2

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        m = 0
        sum_of_array = 0
        while sum_of_array <= maxSum:
            m += 1
            sum_of_array = 0

            sum_of_pyramid = 2*self.sum_of_series(m) - m
            delta_m_left = m - index - 1
            delta_m_right = m - n + index

            if delta_m_left > 0:
                sum_of_left_cutoff = self.sum_of_series(delta_m_left)
                sum_of_array = sum_of_pyramid - sum_of_left_cutoff
            else:
                sum_of_array = sum_of_pyramid + abs(delta_m_left)

            if delta_m_right > 0:
                sum_of_right_cutoff = self.sum_of_series(delta_m_right)
                sum_of_array -= sum_of_right_cutoff
            else:
                sum_of_array += abs(delta_m_right)

        return m-1


def tests():
    return {'n': 10, 'index': 5, 'maxSum': 10}, {'n': 6, 'index': 1, 'maxSum': 10}, {'n': 4, 'index': 2, 'maxSum': 6}, {'n': 3, 'index': 0, 'maxSum': 815094800},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.maxValue(**test)}\n')


main()
