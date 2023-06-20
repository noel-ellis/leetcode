class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1]
        suffix = [1]
        products = []

        for i in range(1, n):
            prefix.append(prefix[i-1]*nums[i-1])

        for i in range(n-2, -1, -1):
            suffix.append(suffix[n-i-2]*nums[i+1])
        suffix = suffix[::-1]

        for i in range(0, n):
            products.append(prefix[i]*suffix[i])

        return products


def tests():
    return {'nums': [1, 2, 3, 4]},  {'nums': [-1, 1, 0, -3, 3]},  {'nums': [-1, 3]},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\ntest {num}: {test}\nresult {num}: {solution.productExceptSelf(**test)}\n')


main()
