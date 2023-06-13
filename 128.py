class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        best_streak = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                streak = 1
                element = num + 1
                while element in nums_set:
                    streak += 1
                    element += 1
                if best_streak < streak:
                    best_streak = streak

        return best_streak


def tests():
    return {'nums': [100, 4, 200, 1, 3, 2], }, {'nums': [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], },


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.longestConsecutive(**test)}\n')


main()
