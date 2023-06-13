class Solution:
    # time complexity: O(nlogn)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for element in nums:
            if element not in hashmap.keys():
                hashmap[element] = 0
            hashmap[element] += 1

        frequencies_sorted = sorted(hashmap, key=hashmap.get, reverse=True)

        result = []
        for i in range(0, k):
            result.append(frequencies_sorted[i])

        return result


def tests():
    return {'nums': [1, 1, 1, 2, 2, 3], 'k': 2, }, {'nums': [1], 'k': 1}, {'nums': [4, 1, 2, 4, 1, 2, 2, 7, 2, 1], 'k': 3},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.topKFrequent(**test)}\n')


main()
