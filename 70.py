class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0, 1]
        for _ in range(0, n):
            sum = result[0] + result[1]
            result[0] = result[1]
            result[1] = sum
        return result[1]


def tests():
    return {'n': 2}, {'n': 3}, {'n': 4}, {'n': 5}, {'n': 7}


def main():
    solution = Solution()
    include_tests = [0, 1, 2, 3, 4]
    for num, test in enumerate(tests()):
        if num in include_tests:
            print(
                f'==============\ntest {num}: {test}\nresult {num}: {solution.climbStairs(**test)}\n')


main()
