class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash = {}
        for num in nums:
            if num not in hash.keys():
                hash[num] = 0
            hash[num] += 1

            if hash[num] > 1:
                return True

        return False


def tests():
    return {'nums': [1, 2, 3, 1]},  {'nums': [1, 2, 3, 4]}, {'nums': [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.containsDuplicate(**test)}\n')


main()
