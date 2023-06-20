class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_hash = {}
        for string in strs:
            anagram = str(sorted(list(string)))
            if anagram not in anagram_hash.keys():
                anagram_hash[anagram] = []
            anagram_hash[anagram].append(string)

        return list(anagram_hash.values())


def tests():
    return {'strs': ["eat", "tea", "tan", "ate", "nat", "bat"]},  {'strs': [""]}, {'strs': ["a"]},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.groupAnagrams(**test)}\n')


main()
