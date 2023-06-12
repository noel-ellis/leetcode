class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0

        max_gain = 0
        min_price = prices[0]
        max_price = prices[0]
        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                max_price = 0

            if prices[i] > max_price:
                max_price = prices[i]
                if max_price - min_price > max_gain:
                    max_gain = max_price - min_price

        return max_gain


def tests():
    return {'prices': [7, 1, 5, 3, 6, 4]},  {'prices': [7, 6, 4, 3, 1]}, {'prices': [0]}, {'prices': [0, 2]}, {'prices': [2, 0]},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.maxProfit(**test)}\n')


main()
