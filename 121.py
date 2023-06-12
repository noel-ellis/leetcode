class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # task: to find maximums for every slice of array
        if len(prices) == 1:
            return 0

        pnl_stats = []
        for i in range(0, len(prices)-1):
            trade_period = prices[i:]
            pnl_stats.append(max(trade_period) - trade_period[0])
        max_profit = max(pnl_stats)

        if max_profit < 0:
            return 0
        return max_profit


def tests():
    return {'prices': [7, 1, 5, 3, 6, 4]},  {'prices': [7, 6, 4, 3, 1]}, {'prices': [0]}, {'prices': [0, 2]}, {'prices': [2, 0]},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.maxProfit(**test)}\n')


main()
