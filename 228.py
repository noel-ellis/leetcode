class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if nums == []:
            return []

        result = []
        arr = []
        for num in nums:
            if arr == []:
                arr.append(num)
                continue

            if num == arr[-1] + 1:
                arr.append(num)
                continue

            if len(arr) == 1:
                result.append(str(arr[0]))
                arr = [num]
                continue

            result.append(str(arr[0]) + "->" + str(arr[-1]))
            arr = [num]

        if len(arr) == 1:
            result.append(str(arr[0]))
            return result

        result.append(str(arr[0]) + "->" + str(arr[-1]))
        return result


def tests():
    return {'nums': [0, 2, 3, 4, 6, 8, 9]},  {'nums': [0, 1, 2, 4, 5, 7]}, {'nums': [0]}, {'nums': [0, 2]},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.summaryRanges(**test)}\n')


main()
